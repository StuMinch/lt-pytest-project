import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

remote_url = "https://hub.lambdatest.com/wd/hub"

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.browser_version = 'dev'

    lt_options = {}
    lt_options['user'] = os.environ.get("LT_USERNAME")
    lt_options['accessKey'] = os.environ.get("LT_ACCESS_KEY")
    lt_options['build'] = 'Pytest'
    lt_options['visual'] = True
    lt_options['video'] = True
    lt_options['w3c'] = True
    lt_options['network'] = True
    lt_options['platformName'] = 'Windows 10'
    lt_options['plugin'] = 'python-pytest'
    options.set_capability('lt:options', lt_options)

    driver = webdriver.Remote(command_executor=remote_url, options=options)
    yield driver