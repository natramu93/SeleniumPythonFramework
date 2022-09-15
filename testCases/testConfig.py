import pytest
from selenium.webdriver import Chrome
from utilities.ConfigUtils import Config
from webdriver_manager.chrome import ChromeDriverManager
from utilities.gen_func import initialize_logger
from utilities.KeywordUtils import KeywordUtils


@pytest.fixture(scope='class')
def test_setup(request):
    request.cls.logger = initialize_logger(request.cls.__name__)
    request.cls.driver = Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver.implicitly_wait(30)
    request.cls.driver.maximize_window()
    request.cls.config = Config('prod')
    request.cls.ku = KeywordUtils(request.cls.driver,request.cls.logger)
    # request.cls.logger = initialize_logger(request.cls)
    yield
    request.cls.driver.quit()