# -*- coding: utf-8 -*-
#
# ITerativ GmbH
# http://www.iterativ.ch/
#
# Copyright (c) 2012 ITerativ GmbH. All rights reserved.
#
# Created on Jul 20, 2012
# @author: Daniel Egger <daniel.egger@gmail.com>

from fabric.api import env
from deployit.fabrichelper.servicebase import UwsgiService, NginxService, CeleryService
from deployit.fabrichelper.environments import EnvTask


class VagrantEnv(EnvTask):
    """
    Use vagrant environment
    """

    name = "vagrant"

    def run(self):
        env.hosts = ['192.168.33.10']
        env.server_names = ['127.0.0.1', '10.*', '192.168.*']
        env.user = 'vagrant'
        env.key_filename = "~/.vagrant.d/insecure_private_key"
        env.use_dev_pip = True
        env.env_name = 'vagrant'
        env.services = [UwsgiService, NginxService, CeleryService]
        env.project_name = '{{ cookiecutter.project_name }}'
        env.puppet_branch_name = 'ubuntu1204'
        env.settings_module = '{{ cookiecutter.project_name }}.settings.vagrant'
        env.debug = True
        env.puppet_temp_dir = '/home/vagrant/puppettmp'
        env.puppet_dir = '/home/vagrant/puppet'
        env.requirements_file = 'requirements/base.txt'


test_local_env = VagrantEnv()
