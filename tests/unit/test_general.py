import pytest
import requests
import json

class TestApi():

    def test_success_status_code(self, successes):
        """Check if we are able to reach the API"""
        assert successes.status_code == 200

    def test_failure_status_code(self, failures):
        """Check if specific parameters are causing intentional errors"""
        assert failures.status_code == 400

    @pytest.mark.parametrize(
        ('URL'),
        (
            ("http://127.0.0.1:5000/v1/occurrences?url=testing123&word=test"),
        )
    )
    def test_invalid_url(self, URL):
        """Check if invalid URL validation is working"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert "Invalid URL" in result['message']['url']

    @pytest.mark.parametrize(
        ('URL'),
        (
            ("http://127.0.0.1:5000/v1/occurrences?url=http://www.spanishdict.com/translate/espa%C3%B1ol&word=testing12"),
        )
    )
    def test_no_occurrences(self, URL):
        """Check if no occurrences result is correct"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result['result']['occurrences'] == 0

    @pytest.mark.parametrize(
        ('URL', 'occurrences'),
        (
            ("http://127.0.0.1:5000/v1/occurrences?url=http://www.spanishdict.com/translate/espa%C3%B1ol&word=español", 39),
        )
    )
    def test_occurrences(self, URL, occurrences):
        """Check if the correct amount of occurrences is being returned"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result['result']['occurrences'] == occurrences