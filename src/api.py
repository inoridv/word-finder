from flask import Flask
from flask_restful import Resource, Api

# Initialize the api.
app = Flask(__name__)
api = Api(app)

@api.resource('/v1/occurrences')
class OccurrencesCrawler(Resource):
    """Handler for this endpoint of the API."""
    def get(self):
        """Return the number of occurrences of the given word in the given URL"""
        return

if __name__ == '__main__':
    app.run(debug=True)