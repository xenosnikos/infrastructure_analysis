from flask import Flask
from flask_restful import Api

from controllers.infrastructure_analysis import InfrastructureAnalysis

app = Flask(__name__)
api = Api(app)

api.add_resource(InfrastructureAnalysis, "/v2/infrastructureAnalysis")

if __name__ == "__main__":
    app.run()
