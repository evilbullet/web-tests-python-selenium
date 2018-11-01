import pytest
from selenium import webdriver
import config

@pytest.fixture(scope='class')
def setup(request):
    core.config.browser = webdriver.Firefox()

    def teardown():
        core.config.browser.qiut()

    request.addfunalizer(teardown)

@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass