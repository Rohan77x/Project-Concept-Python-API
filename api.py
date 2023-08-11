from flask import Flask
from flask_restful import Resource, Api

# create a flask object
app = Flask(__name__)
api = Api(app)

# creating a class for Fruits that will hold
# the accessors
class Fruits(Resource):
    def get(self):
      # returns a dictionary with fruits
        return {
            'fruits': ['Mango',
                        'Pomegranate',
                        'Orange',
                        'Litchi']
        }

# adds the resources at the root route
api.add_resource(Fruits, '/')

# if this file is being executed then run the service
if __name__ == '__main__':
      # run the service
    app.run(host='0.0.0.0', port=80, debug=True)
