import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru, fr, es")
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(user_language)
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()