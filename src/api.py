from flask import Flask
from flask_restful import Resource, Api, reqparse

# Initialize the api.
app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)

@api.resource('/v1/occurrences')
class OccurrencesCrawler(Resource):
    """Handler for this endpoint of the API."""
    def get(self):
        """Return the number of occurrences of the given word in the given URL"""

        # Parse the url and word parameters.
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, help='An URL to crawl for the occurrences of the search word.')
        parser.add_argument('word', required=True, help='A word to search for in the given URL.')
        args = parser.parse_args()
        url = args['url']
        word = args['word']

        # Initialize the function result.
        result = {}
        return result

if __name__ == '__main__':
    app.run(debug=True)