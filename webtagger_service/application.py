from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from . import endpoints


application = Flask('main', static_folder=None, template_folder=None)
# the port for this application is set in webtagger_service/dev_server.py or webtagger_service/server.py

application.wsgi_app = DispatcherMiddleware(endpoints.estntk_v16_service, {
    # add your applications with version prefixes here
    '/1.6.7beta': endpoints.estntk_v16_service
})
