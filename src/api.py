from flask import Flask
from flask_restful import Resource, Api, reqparse
from bs4 import BeautifulSoup
import requests, re

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

                 # Request the given page and handle errors.
        try :
            webpage = requests.get(url)
        except requests.exceptions.RequestException as e:
            result["message"] = {"url" : str(e)}
            return result, 400

        if r.status_code == 404:
        	result["message"] = {"url" : "Given page was not found."}
        	return result, 400
        # Get page content.
        soup = BeautifulSoup(webpage.text)

        # Only the content in the body should be considered.
        content = soup.body.extract()

        # Remove all HTML tags whose content might result in a false positive.
        [element.decompose() for element in content(['style', 'script', '[document]', 'head', 'title'])]

        # Gather the text without HTML Tags and convert it to lowercase.
        pagetext = content.get_text().lower()

        # Search for the occurrences of the given word using regex.
        occurrences = [needle.start() for needle in re.finditer(str(word).lower(), pagetext)]

        # Return the occurrences found.
        if not occurrences:
        	result["result"] = {"occurrences" : 0}
        	return result, 200

        result["result"] = {"occurrences" : occurrences}
        return result, 200

if __name__ == '__main__':
    app.run(debug=True)