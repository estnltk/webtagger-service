from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from . import endpoints


application = Flask('main', static_folder=None, template_folder=None)

application.wsgi_app = DispatcherMiddleware(endpoints.estntk_v16_service, {
    '/1.6.7beta': endpoints.estntk_v16_service
})
