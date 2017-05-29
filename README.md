# word-finder
Python API developed using [Flask](http://flask.pocoo.org/), [Flask-Restful](https://flask-restful.readthedocs.io/en/0.3.5/) &amp; [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/). It contains a function that returns the amount of occurrences of a word in a given web page. This method wil crawl the page and it only searches for the word in the visible content of the page(the <body> tag), ignoring any other occurrence that might be in the page's metadata or scripts/style tags. You can think of it as an immitation of the "CTRL+F" command.

##### /v1/occurrences
Endpoint for the crawl function.
- Parameters:
  - **url**: The page's URL to search for the word. 
  - **word**: The word to search for occurrences in the given page.
- Return:
  - A JSON object containing either the amount of occurrences of the word found in the page or an error message. 