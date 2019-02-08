import sys, os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
from common.Read_Data import read_yml_data
from  appium import webdriver
from Page.SearchPageClass import SearchPageClass
from common.Init_driver import init_driver
from common.Init_driver import init_driver2
import  pytest
import time

def yml_data():
    data_list=[]
    data=read_yml_data("add_user").get("User")
    print(data)
    print(data.keys())
    for i in data.keys():
        data_list.append((i,data.get(i).get("name"),data.get(i).get("phone"),data.get(i).get("expect")))
    return data_list
class AddUserClass:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'TEX9K17904908260'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.el_lianxirenlist = (By.CLASS_NAME, "android.widget.TextView")
        self.el_add_button = (By.ID, "com.android.contacts:id/menu_add_contact")
        self.el_text_name = (By.XPATH, "//*[contains(@text,'姓名')]")
        self.el_text_phone = (By.XPATH, "//*[contains(@text,'电话号码')]")
        self.el_queren_button = (By.ID, "android:id/icon2")
        self.el_lianxiren_back_button = (By.ID, "com.android.contacts:id/backImg")

        #self.driver=init_driver2()
        #self.addUserObj=AddUserPageClass(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def postion_Element(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            # lambda x: x.find_element(By.ID, value=None)
            lambda x: x.find_element(*loc)
        )

    def position_Element_lists(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            lambda x: x.find_elements(*loc)
        )

    def click_Element(self, loc):
        self.postion_Element(loc).click()

    def send_data(self, loc, text):
        el_input = self.postion_Element(loc)
        el_input.clear()
        el_input.send_keys(text)
    # @pytest.mark.run(order=1)
    # def test_click_newlianxiren(self):
    #     self.click_Element(self.el_add_button)
    def isexit(self,loc):
        try:
            self.postion_Element(loc)
            return  True
        except Exception as  e:
            print("定位不到元素")
            return False
    def get_user_list(self):
        user_data=self.position_Element_lists(self.el_lianxirenlist)
        #[i.text for i in user_data]
        user_data_list=[]
        for i in user_data:
            user_data_list.append(i.text)
        return user_data_list


    @pytest.mark.parametrize("case_num,name,phone,expect",yml_data())
    def test_inupt_data(self,case_num,name,phone,expect):

        self.click_Element(self.el_add_button)
        self.send_data(self.el_text_name,name)
        self.send_data(self.el_text_phone,phone)

        self.click_Element(self.el_queren_button)
        self.isexit(self.el_lianxiren_back_button)
        self.click_Element(self.el_lianxiren_back_button)
        print("测试用例编号:",case_num)
        user_list = self.get_user_list()
        assert expect in user_list