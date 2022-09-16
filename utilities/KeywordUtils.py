import datetime

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class KeywordUtils():
    def __init__(self,driver,logger):
        self.driver = driver
        self.action = ActionChains(driver)
        self.wait = WebDriverWait(driver,30)
        self.logger = logger

    def load_url(self,url):
        self.logger.debug(f'Page before loading: {self.driver.current_url}')
        self.driver.get(url)
        self.logger.debug(f'Load URL: {url}')
        self.logger.debug(f'Page after loading: {self.driver.current_url}')

    def find_element(self,by,loc):
        self.logger.debug(f'Finding elemnt by: {by} locator: {loc}')
        try:
            self.wait.until(ec.presence_of_element_located((by,loc)))
            self.logger.debug(f'Element found in html')
            e = self.driver.find_element(by,loc)
        except:
            self.logger.debug('Element not found')
            self.driver.get_screenshot_as_file(f'screenshots/{datetime.datetime.now().strftime("%Y-%m-%d %H-%M")}-{by}-{loc}.png')
            e = None
        return e

    def click(self,by,loc): # click(By.ID,'mobilenoip')
        self.logger.debug(f'Click on element by {by} locator {loc}')
        e = self.find_element(by,loc)
        try:
            self.wait.until(ec.element_to_be_clickable(e))
            e.click()
        except:
            self.driver.execute_script('argument[0].click()', e)
            self.logger.debug('Click by JavaScript command')

    def select_by_value(self,by,loc,value):
        self.logger.debug(f'Select element by:{by}, loc:{loc}, by value "{value}"')
        e = self.find_element(by,loc)
        self.wait.until(ec.visibility_of(e))
        try:
            dd = Select(e)
            dd.select_by_value(value)
        except:
            self.logger.debug('Select element failed')

    def type(self,by,loc,value):
        self.logger.debug(f'Type {value} into {by}, {loc}')
        try:
            self.wait.until(ec.visibility_of_element_located((by, loc)))
            el = self.find_element(by,loc)
            el.clear()
            el.send_keys(value)
        except:
            self.logger.debug('Type data failed')

    def mouse_over(self,by,loc):
        e = self.find_element(by,loc)
        self.action.move_to_element(e).perform()

