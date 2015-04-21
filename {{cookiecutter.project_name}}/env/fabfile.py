# -*- coding: utf-8 -*-
#
# ITerativ GmbH
# http://www.iterativ.ch/
#
# Copyright (c) 2012 ITerativ GmbH. All rights reserved.
#
# Created on May 10, 2012
# @author: Daniel Egger <daniel.egger@gmail.com>, Daniel Egger <daniel.egger@gmail.com>

from fabric.api import env
from stage.stage import *
from vagrant.vagrant import *

env.rsync_exclude.remove('*.dat')
env.rsync_exclude = env.rsync_exclude + ['media/']

from deployit.fabrichelper.common import *


class RandomData(BaseTask):
    """
    Reset database
    """
    name = "randomdata"

    @warning
    @calc_duration
    def run(self, no_input=False):
        with cd(env.remote_path()):
            self.virtualenv('python -u manage.py randomdata')
        self.adjust_rights(env.www_server_uid)


random_data = RandomData()
