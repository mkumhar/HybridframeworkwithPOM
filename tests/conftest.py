import pytest
import selenium
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture()
def setup_teardown(request):
    browser=ReadConfigurations.read_configuration("Basic info","browser")
    global driver
    driver=None
    if browser.__eq__("chrome"):
         driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
         driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
         driver = webdriver.Edge()
    else:
         print("provide a valid browser name")

    driver.maximize_window()
    app_url=ReadConfigurations.read_configuration("Basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()
