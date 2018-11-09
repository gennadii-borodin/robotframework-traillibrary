# -*- coding: utf-8 -*-

"""
Auxiliary module for access some of Test Rail API calls

"""

from collections import namedtuple
from TRailLibrary.testrail import APIClient

class TestRailAdaptor(object):
    """
        Test Rail instance adaptor

    """
    class _Decor(object):
        @classmethod
        def connect_if_disconnected(cls, func_to_connect):
            """
                Creates instance of TestRail client if not connected
            """
            def _wrapper(self, *args, **kwargs):
                if self.client is None:
                    self.connect_to_testrail()
                return func_to_connect(self, *args, **kwargs)
            return _wrapper

    def __init__(self, url, user, api_key): #, **kwargs):
        self.client = None
        self.url = url
        self.user = user
        self.passwd = api_key
        self.project = None
        self.plan = None
        self.suites = None
        self.config_groups = None
        self.active_run = None

    def connect_to_testrail(self):
        """
            Creates TestRail client instance
        """
        self.client = APIClient(self.url)
        self.client.user = self.user
        self.client.password = self.passwd

    def select_project(self, new_project_name):
        """
        Change current project and update project reladed info.
        The plan property will be cleared

        """
        self.project = self._get_project(new_project_name)
        self.plan = None
        self.suites = self._get_suites(self.project.id)
        self.config_groups = self._get_configs(self.project.id)

    def select_plan(self, new_plan_name):
        """
            Change current plan

        """
        if self.project is not None:
            self.plan = self._get_plan(self.project.id, new_plan_name)
        else:
            raise ValueError('Project property is empty. Please select project first')

    def set_active_run(self, run_name, config=None):
        """
            Sets a plan/config combination as active. So there is no need
            to find combination each time
        """
        self.active_run = self._get_run(run_name, config)

    def create_run(self, name, description, test_suite, config_sets=None,
                   include_all=True, case_ids=None):
        """
        Creates test run in Test Rail
        """
        if self.plan.runs is not None:
            for run in self.plan.runs:
                if getattr(run, 'name') == name:
                    print('Test Run already created. No actions needed')
                    return
        suite_ids = [x.id for x in self.suites if getattr(x, 'name') == test_suite]
        run_header = {}
        runs = []
        all_config_ids = []
        for config_set in config_sets:
            config_ids = []
            run = {}
            for k, v in config_set.items():
                for group in self.config_groups:
                    if getattr(group, 'name') == k:
                        for config in group.configs:
                            if config.name == v:
                                config_ids.append(config.id)
                                all_config_ids.append(config.id)
            run['description'] = description

            if case_ids:
                run['include_all'] = False
                run['case_ids'] = case_ids
            else:
                run['include_all'] = include_all

            run['config_ids'] = config_ids
            runs.append(run)
        run_header['suite_id'] = suite_ids[0]
        run_header['name'] = name
        run_header['config_ids'] = list(set(all_config_ids))
        run_header['runs'] = runs

        result = self.client.send_post(
            'add_plan_entry/' + str(self.plan.id),
            run_header
        )
        return result
    @_Decor.connect_if_disconnected
    def add_case_result(self, case_id, status, run_name, config=None, **kwargs):
        """
            Adds executiom result to run/config
        """
        run = self._get_run(run_name, config)
        body = {}

        for key in kwargs:
            body[key] = kwargs[key]

        status_id = 5
        if status == 'PASS':
            status_id = 1
        body['status_id'] = status_id
        
        try:
            result = self.client.send_post(
                'add_result_for_case/{run_id}/{case_id}'.format(run_id=run.id, case_id=case_id),
                body
            )
        except Exception as e:
            raise ValueError('Cannot add result for case [{id}]. ' 
                             'Check if the case exists'.format(id=case_id)) from e

        return result

    @_Decor.connect_if_disconnected
    def _get_project(self, name):
        response = self.client.send_get(
            'get_projects'
            )
        objects = [obj for obj in response if obj['name'] == name]
        if not objects:
            raise ValueError("Can't find project '{name}'".format(name=name))
        project = namedtuple('Project', sorted(objects[0]))
        prj = project(**objects[0])
        return prj

    @_Decor.connect_if_disconnected
    def _get_plan(self, project_id, plan_name):
        response = self.client.send_get(
            'get_plans/{project_id}'.format(project_id=project_id)
            )
        objects = [obj for obj in response if obj['name'] == plan_name]
        if not objects:
            raise ValueError("Can't find plan '{name}'".format(name=plan_name))
        plan = namedtuple('Plan', sorted(objects[0]))
        plan = namedtuple('Plan', plan._fields + ('runs',))
        plan_id = objects[0]['id']
        objects[0]['runs'] = self.__get_runs(plan_id)
        pln = plan(**objects[0])
        return pln

    @_Decor.connect_if_disconnected
    def _get_suites(self, project_id):
        response = self.client.send_get(
            'get_suites/{project_id}'.format(project_id=project_id)
            )
        suite = namedtuple('Suite', sorted(response[0]))
        suites = []
        for item in response:
            s_i = suite(**item)
            suites.append(s_i)
        return suites
    @_Decor.connect_if_disconnected
    def _get_configs(self, project_id):
        response = self.client.send_get(
            'get_configs/{project_id}'.format(project_id=project_id)
            )
        try:
            config = namedtuple('Config', sorted(response[0]['configs'][0]))
        except AttributeError:
            return None
        config_group = namedtuple('ConfigGroup', ['id', 'name', 'project_id', 'configs'])
        c_groups = []
        for c_group in response:
            configs = []
            for cfg in c_group['configs']:
                conf = config(**cfg)
                configs.append(conf)
            group = config_group(c_group['id'], c_group['name'], c_group['project_id'], configs)
            c_groups.append(group)
        return c_groups

    @_Decor.connect_if_disconnected
    def __get_runs(self, plan_id):
        response = self.client.send_get(
            'get_plan/{plan_id}'.format(plan_id=plan_id)
            )
        try:
            Run = namedtuple('Run', sorted(response['entries'][0]['runs'][0]))
        except AttributeError:
            return None
        runs = []
        for enrty in response['entries']:
            for run in enrty['runs']:
                r_i = Run(**run)
                runs.append(r_i)
        return runs

    @_Decor.connect_if_disconnected
    def _get_run(self, run_name, config=None):
        run_set = [x for x in self.plan.runs if x.name == run_name]
        if not config and run_set:
            return run_set[0]
        elif config and run_set:
            config_string = ', '.join(list(config.values()))
            run = [x for x in run_set if x.config == config_string]
            return run[0]
