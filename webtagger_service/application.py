from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from .endpoints import app


application = Flask('main', static_folder=None, template_folder=None)

application.wsgi_app = DispatcherMiddleware(app, {
    '/1.6.7beta': app
})
