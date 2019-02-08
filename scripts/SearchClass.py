import sys, os
sys.path.append(os.getcwd())
from common.Read_Data import read_yml_data
from  appium import webdriver
from Page.SearchPageClass import SearchPageClass
from common.Init_driver import init_driver
import  pytest
def yml_data():
    data_list=[]
    data=read_yml_data("search_data").get("Search_Data")
    print(data)
    print(data.keys())
    for i in data.keys():
        data_list.append((i,data.get(i).get("test"),data.get(i).get("expect_data")))
    return data_list
class SearchClass:
    def setup_class(self):
        self.driver=init_driver()
        self.SearchPageObj=SearchPageClass( self.driver)

    @pytest.fixture(scope="class")
    def test_click_search_button(self):
        self.SearchPageObj.click_search_set_option()

    @pytest.mark.usefixtures("test_click_search_button")
    @pytest.mark.parametrize("num,text,expect_data",yml_data())
    def test_send_input_data(self,num,text,expect_data):
        print("yonglibianhao:",num)
        self.SearchPageObj.send_input_data(text)
        assert expect_data==456




    def teardown_class(self):
        self.SearchPageObj.click_back()
        self.driver.quit()