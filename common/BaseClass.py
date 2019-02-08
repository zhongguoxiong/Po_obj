from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def __init__(self,driver):
        self.driver=driver

    def postion_Element(self,loc,timeout=10,poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            #lambda x: x.find_element(By.ID, value=None)
            lambda x: x.find_element(*loc)
        )

    def position_Element_lists(self,loc,timeout=10,poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            lambda x: x.find_elements(*loc)
        )

    def click_Element(self,loc):
        self.postion_Element(loc).click()

    def send_data(self,loc,text):
        el_input=self.postion_Element(loc)
        el_input.clear()
        el_input.send_keys(text)