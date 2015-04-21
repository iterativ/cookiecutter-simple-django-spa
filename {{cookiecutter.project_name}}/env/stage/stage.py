# -*- coding: utf-8 -*-
#
# ITerativ GmbH
# http://www.iterativ.ch/
#
# Copyright (c) 2012 ITerativ GmbH. All rights reserved.
#
# Created on Mar 13, 2012
# @author: maersu <me@maersu.ch>

from fabric.api import env
from deployit.fabrichelper.servicebase import UwsgiService, NginxService, CeleryService, NewReclicService
from deployit.fabrichelper.environments import EnvTask


class StageEnv(EnvTask):
    """
    Use stage environment
    """
    name = "stage"

    def run(self):
        env.hosts = ['gurten.iterativ.ch']
        env.env_name = 'stage'
        env.services = [UwsgiService, NginxService, CeleryService, NewReclicService]
        env.project_name = '{{ cookiecutter.project_name }}'
        env.remote_virtualenv = '/srv/www/{{ cookiecutter.project_name }}/stage/{{ cookiecutter.project_name }}-env'
        env.server_names = ['{{ cookiecutter.project_name }}.gurten.iterativ.ch']
        env.settings_module = '{{ cookiecutter.project_name }}.settings.stage'
        env.nginx_no_follow = True
        env.requirements_file = 'requirements/dev.txt'
        env.puppet_branch_name = 'ubuntu1204'
        # env.newrelic_key = ''
        # env.not_allowed_tasks = ['resetload', 'delete']
        # env.newrelic_application_id = ''
        # env.newrelic_x_api_key = ''


stage_env = StageEnv()
