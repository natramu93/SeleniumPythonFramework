import pytest
from selenium.webdriver import Chrome,Edge,Firefox
from selenium.webdriver.chrome.options import Options as co
from utilities.ConfigUtils import Config
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.gen_func import initialize_logger
from utilities.KeywordUtils import KeywordUtils

def _initialize_browser(browser):
    global choice
    if browser=='edge':
        choice = Edge(executable_path=EdgeChromiumDriverManager().install())
    elif browser =='ff':
        choice = Firefox(executable_path=GeckoDriverManager().install())
    else:
        c = co()
        c.accept_insecure_certs = True
        # c.add_argument()
        choice = Chrome(executable_path=ChromeDriverManager().install(),options=c)
    return choice

@pytest.fixture(scope='class')
def test_setup(request):
    request.cls.logger = initialize_logger(request.cls.__name__)
    request.cls.driver = _initialize_browser(request.config.getoption('--browser'))
    request.cls.driver.implicitly_wait(30)
    request.cls.driver.maximize_window()
    request.cls.config = Config('prod')
    request.cls.ku = KeywordUtils(request.cls.driver,request.cls.logger)
    # request.cls.logger = initialize_logger(request.cls)
    yield
    request.cls.driver.quit()