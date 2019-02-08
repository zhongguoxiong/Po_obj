import sys, os
sys.path.append(os.getcwd())
from common.BaseClass import BaseClass
import Page
class SearchPageClass:
    def __init__(self,driver):
        self.driver=driver
        self.baseObj=BaseClass(driver)

    def click_search_set_option(self):

        self.baseObj.click_Element(Page.el_search_button)

    def send_input_data(self,text):
        self.baseObj.send_data(Page.el_search_input,text)

    def click_back(self):
        self.baseObj.click_Element(Page.el_back_button)
