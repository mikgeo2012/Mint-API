from flask import Flask
from flask_restful import Api
from app.api import HealthCheck

app = Flask(__name__)
api = Api(app)

api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True)