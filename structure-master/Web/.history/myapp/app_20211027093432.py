from flask import Flask
from .api.routes import api
from .site.routes import site
@app.route('/',methods=['GET'])
def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app
