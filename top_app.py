from flask import Flask
from api.views import router, main

def create_app():
    app = Flask(__name__)
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
    app.register_blueprint(main)
    app.register_blueprint(router, url_prefix="/api/v1.0")
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
