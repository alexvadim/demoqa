import json

import pytest
from selenium import webdriver

@pytest.mark.usefixtures("runMode")
@pytest.fixture(scope='class')
def setup(request):
     with open('setting.json', 'r') as test:
          test = json.loads(test.read())
     if test['browser'] == "chrome":
          browser = webdriver.Chrome()
     elif test ['browser'] == "firefox":
         browser = webdriver.Firefox()
     else:
         print('Некорректно указан браузер в настройках!')
     browser.imlicitly_wait(10)
     browser.set_window_size(1920, 1080)
     request.cls.browser = browser
     yield browser
     browser.close()

