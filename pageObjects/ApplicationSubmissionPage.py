from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.KeywordUtils import KeywordUtils


class ApplicationSubmissionPage():
    _sa_dd_id = 'ddlarea'
    _si_dd_id = 'ddlSourceOfIncome'
    _mobile_ip = 'txtMobileNo'
    _dob_ip = 'txtDOB'
    _pan_ip = 'txtPanNo'
    _verify_btn = 'btnVerify'
    _verify_txt = '//*[@id="divOTPDetails"]/div[1]'

    def __init__(self,driver,logger):
        self.driver = driver
        self.ku = KeywordUtils(driver,logger)
        self.logger = logger

    def select_service_area(self,value):
        self.ku.select_by_value(By.ID,self._sa_dd_id,value)

    def select_incomeSource(self,value):
        self.ku.select_by_value(By.ID,self._si_dd_id,value)

    def mobileNo_ip(self,value):
        self.ku.type(By.ID, self._mobile_ip,value)

    def dob_ip(self,value):
        self.ku.type(By.ID, self._dob_ip, value)

    def pan_ip(self,value):
        self.ku.type(By.ID, self._pan_ip,value)

    def click_verify(self):
        self.ku.click(By.ID,self._verify_btn)
        text = self.driver.find_element(By.XPATH, self._verify_txt).text
        return text