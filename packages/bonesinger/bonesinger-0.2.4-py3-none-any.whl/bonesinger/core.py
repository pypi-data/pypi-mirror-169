from .executors import StepExecutor
from .step import RunStep
from .pipeline import Pipeline
from .util import strong_key_format, merge_dicts
import tempfile
import os
from git import Repo
import traceback


def matrix_iterator(matrix):
    def prod(lst):
        res = 1
        for x in lst:
            res *= x
        return res

    keys = sorted(matrix.keys())
    values_list = [matrix[key] for key in keys]
    count_of_elements = prod([len(values) for values in values_list])
    for i in range(count_of_elements):
        matrix_value = {}
        for j in range(len(keys)):
            matrix_value[keys[j]] = values_list[j][i % len(values_list[j])]
        yield matrix_value


def sanitize_url(text):
    # find url in text and replace it with "***url***"
    # to hide it from logs
    import re
    url_regex = re.compile(
        r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+')
    return url_regex.sub('***url***', text)


class Core:
    def __init__(self,
                 executor: StepExecutor,
                 matrix: dict,
                 prefix: str,
                 debug: bool,
                 pipeline_records: list,
                 on_success_records: dict,
                 on_failure_records: dict,
                 pipeline_template: list,
                 security_options: dict):
        self.pipeline_template = pipeline_template
        self.executor = executor
        self.matrix = matrix
        self.prefix = prefix
        self.debug = debug
        self.pipelines = self.parse_pipelines(pipeline_records)
        self.on_success_script = self.make_task_list(on_success_records)
        self.on_failure_script = self.make_task_list(on_failure_records)
        self.security_options = security_options

    def make_task_list(self, records) -> list:
        """make list of Step objects from records"""
        tasks = []
        if records is None:
            return tasks
        for record in records:
            name = record["name"]
            run = record["run"]
            tasks.append(RunStep(core=self,
                                 name=name,
                                 run=run,
                                 pipeline=None))
        return tasks

    def is_debug_mode(self):
        return self.debug

    def compile_pipeline_record(self, name, template, subst):
        def subst_value(value):
            if isinstance(value, str):
                return strong_key_format(value, subst)
            elif isinstance(value, list):
                return [subst_value(x) for x in value]
            elif isinstance(value, dict):
                return {key: subst_value(value[key]) for key in value}
            else:
                return value

        rec = subst_value(template)
        rec['name'] = name

        return rec

    def pipeline_from_record(self, record):
        name = record["name"]
        watchdog = record.get("watchdog", 0)
        success_info = record.get("success_info", None)
        workspace = record.get("workspace", None)

        gitdata = None
        if workspace is None:
            workspace = tempfile.mkdtemp()

        if "git" in record:
            git = record["git"]
            giturl = git["url"]
            gitbranch = git.get("branch", "master")
            gitcommit = git.get("commit", None)
            gitname = git.get("name", None)
            gitdata = {"url": giturl, "branch": gitbranch,
                       "commit": gitcommit, "name": gitname}
            #workspace = os.path.join(workspace, name)

        if "use_template" in record:
            template_name = record["use_template"]
            template = self.find_pipeline_template(template_name)
            subst = {}
            for key in record["args"]:
                subst[key] = record["args"][key]
            return self.pipeline_from_record(
                self.compile_pipeline_record(template=template,
                                             subst=subst,
                                             name=name))
        else:
            return Pipeline(
                core=self,
                name=name,
                step_records=record["steps"],
                watchdog=watchdog,
                success_info=success_info,
                workspace=workspace,
                gitdata=gitdata)

    def parse_pipelines(self, list_of_pipeline_records):
        pipelines = []
        for pipeline_record in list_of_pipeline_records:
            pipelines.append(self.pipeline_from_record(pipeline_record))
        return pipelines

    def find_pipeline(self, name: str):
        for pipeline in self.pipelines:
            if pipeline.name == name:
                return pipeline
        raise Exception("Pipeline not found: " + name)

    def find_pipeline_template(self, name):
        for template in self.pipeline_template:
            if template["name"] == name:
                return template
        raise Exception("Pipeline template not found: " + name)

    def create_build_directory_and_change_it(self):
        temporary_directory = tempfile.mkdtemp()
        os.chdir(temporary_directory)
        self.workspace = temporary_directory

    def execute_entrypoint(self, entrypoint: str):
        self.create_build_directory_and_change_it()
        pipeline = self.find_pipeline(entrypoint)
        for matrix_value in matrix_iterator(self.matrix):
            try:
                if self.debug:
                    print(
                        f"Execute pipeline {pipeline.name} for matrix value: {matrix_value}")
                pipeline.execute(executor=self.executor,
                                 matrix_value=matrix_value,
                                 prefix=self.prefix,
                                 subst={})
            except Exception as e:
                print("Exception: " + str(e))
                print("Traceback: " + traceback.format_exc())
                self.on_failure(pipeline, matrix_value, e)
                break

            self.on_success(pipeline, matrix_value)

    def on_success(self, pipeline, matrix_value):
        if self.security_options["hide_links"]:
            pipeline.success_info = sanitize_url(pipeline.success_info)

        if self.debug:
            print("Success: " + pipeline.name)
            print("Matrix value: " + str(matrix_value))
            print("Success info: " + str(pipeline.success_info))
        for task in self.on_success_script:
            task.execute(pipeline_name=pipeline.name,
                         executor=self.executor,
                         matrix=matrix_value,
                         prefix=self.prefix,
                         subst={"pipeline_name": pipeline.name,
                                "success_info": pipeline.success_info,
                                **pipeline.pipeline_subst})

    def on_failure(self, pipeline, matrix_value, exception):
        if self.security_options["hide_links"]:
            pipeline.success_info = sanitize_url(pipeline.success_info)

        error_message = str(exception)
        for task in self.on_failure_script:
            task.execute(pipeline_name=pipeline.name,
                         executor=self.executor,
                         matrix=matrix_value,
                         prefix=self.prefix,
                         subst={"pipeline_name": pipeline.name,
                                "error_message": error_message,
                                **pipeline.pipeline_subst})
