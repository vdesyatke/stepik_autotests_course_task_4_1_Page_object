import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose language: en or ru')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == 'en' or language == 'ru':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        yield browser
        browser.quit()
    else:
        raise pytest.UsageError("--language should be en or ru")
