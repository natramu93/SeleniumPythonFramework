import pytest
from testCases.testConfig import test_setup
from pageObjects.ApplicationSubmissionPage import ApplicationSubmissionPage


@pytest.mark.usefixtures('test_setup')
class TestApplication():

    def test_title_validation(self):
        self.ku.load_url(self.config.get_value('url'))
        title = self.driver.title
        assert title == 'eMLeads | Application Submission'

    def test_fillApp(self):
        self.ku.load_url(self.config.get_value('url'))
        self.asp = ApplicationSubmissionPage(self.driver,self.logger)
        self.asp.select_service_area('11112')
        self.asp.select_incomeSource('1')
        self.asp.mobileNo_ip('1234567890')
        # print(driver.find_element(By.ID,'txtMobileNo').get_attribute('value'))
        self.asp.dob_ip('06/09/2004')
        self.asp.pan_ip(self.config.get_value('pan'))
        text = self.asp.click_verify()
        assert text == 'Activation Key is sent to 1234567890'
