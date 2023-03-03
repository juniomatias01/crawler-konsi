from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from controller.benefits_controller import benefits_blue_print

app = Flask(__name__)
app.register_blueprint(benefits_blue_print)


SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Crawler Benefits API"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)

