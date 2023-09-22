from flask_restful import Api


def init_app(app):
    api = Api(app, prefix='/api')
    api.add_resource('', '/auth/login')
