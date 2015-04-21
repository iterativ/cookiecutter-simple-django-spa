# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth import get_user_model


class Migration(migrations.Migration):
    def create_admin_user(apps, schema_editor):
        User = get_user_model()
        admin_user = User(
            username="admin",
            is_active=True,
            is_superuser=True,
            is_staff=True,
            email="admin@{{ cookiecutter.project_name }}.dy"
        )
        admin_user.set_password('test')
        admin_user.save()

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
