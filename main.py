from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

class g(Resource):
    def get(self):
        return {'you\'ve received a new message': 'gucci gang gucci gang gucci gang guuci gang'}

class ingest(Resource):
    def post(self, data):
        return {'the data': data}

api.add_resource(Hello, '/')
api.add_resource(g, '/gg')
api.add_resource(ingest, '/ingest')


if __name__ == '__main__':
    app.run(debug=True)
