import requests
import approvaltests
from playwright.sync_api import Page
import pytest

URL = "https://qe-at-cgi-fi.github.io/eprime/"

def test_request():
    response = requests.get(URL)
    assert response.status_code == 200
    approvaltests.verify_html(response.text)

def this_is_sample():
    with open("sample.txt") as f:
        lines = f.readlines()
    return str(lines)

data = [
    ("to be or not be", "5", "2", "0"), 
    ("maaret's", 1, 0, 1), 
    ("to be " *1000, 2000, 1000, 0), 
    (this_is_sample(), 2, 0, 0),
    #bug: too many words
    #("to be or not to be - hamlet's dilemma", 8, 2, 1)
]
ids=["hamlet", "maaret", "long text", "file"]


@pytest.mark.parametrize("input_text, expect_1, expect_2, expect_3", data, ids=ids)
def test_playwright(page: Page, input_text, expect_1, expect_2, expect_3):
    page.goto(URL)
    page.fill("#test_field", input_text)
    page.click("#test_button")
    assert page.inner_text("#test_number_1") == str(expect_1)
    assert page.inner_text("#test_number_2") == str(expect_2)
    assert page.inner_text("#test_number_3") == str(expect_3)
    


# SESSION
# Input from file

# SESSION
# Run in GitHub Actions
# Fix the asserts to expect -style
# Refactor to classes and page objects
# pytest.ini and html report
# Fixtures for webgui in conftest.py
# Allure report
