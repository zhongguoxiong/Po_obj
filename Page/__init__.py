# lambda x: x.find_element(By.ID, value=None)
from selenium.webdriver.common.by import By

el_search_button=(By.ID,"android:id/search_src_text")
el_search_input=(By.ID,"android:id/search_src_text")
el_back_button=(By.ID,"com.android.settings:id/back")

el_lianxirenlist=(By.CLASS_NAME,"android.view.ViewGroup")
el_add_button=(By.ID,"com.android.contacts:id/menu_add_contact")
el_text_name=(By.XPATH,"//*[contains(@text,'姓名')]")
el_text_phone=(By.XPATH,"//*[contains(@text,'电话号码')]")
el_queren_button=(By.ID,"android:id/icon2")
el_lianxiren_back_button=(By.ID,"com.android.contacts:id/backImg")
