# wsgi_app.py
import os

import django.core.handlers.wsgi, newrelic.agent

newrelic.agent.initialize(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'newrelic.ini'))

application = django.core.handlers.wsgi.WSGIHandler()
application = newrelic.agent.wsgi_application()(application)

