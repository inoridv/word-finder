import pytest
import requests

# Static data fixtures.

@pytest.fixture(params = [
        "http://127.0.0.1:5000/v1/occurrences?url=http://www.spanishdict.com/translate/espa%C3%B1ol&word=español",
        "http://127.0.0.1:5000/v1/occurrences?url=http://www.spanishdict.com/translate/espa%C3%B1ol&word=testing12",
    ])
def successes(request):
    """Get the API's result using the specified parameters"""
    page = requests.get(request.param)
    yield page

@pytest.fixture(params = [
        "http://127.0.0.1:5000/v1/occurrences?url=http://www.asf235saft321TESTct.com/test&word=testing12",
        "http://127.0.0.1:5000/v1/occurrences?url=testing123&word=test",
    ])
def failures(request):
    """Get the API's result using the specified parameters"""
    page = requests.get(request.param)
    yield page