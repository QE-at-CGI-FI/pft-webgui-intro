import requests
import approvaltests
from playwright.sync_api import Page

URL = "https://qe-at-cgi-fi.github.io/eprime/"

def test_request():
    response = requests.get(URL)
    assert response.status_code == 200
    approvaltests.verify_html(response.text)

def test_playwright(page: Page):
    page.goto(URL)
    

# SESSION
# Requests or Playwright?
# webgui testing dependencies and setup after git clone
# pytest.ini for command line parameters
# Stepwise Script
# Fix the test target application
# Parametrize
# Parametrize with test name
# Input from file

# SESSION
# Fixtures for webgui in conftest.py
# Refactor to classes and page objects
# Containerize
# Run in GitHub Actions
