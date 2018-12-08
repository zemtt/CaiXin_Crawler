from selenium import webdriver
import time

class Spider(object):
    def __init__(self, usn, psw, wbd):
        self.username = usn
        self.password = psw
        self.driver = wbd
    
    def login(self):
        self.driver.get('http://u.caixin.com/user/login.html')
        elem = self.driver.find_element_by_css_selector(
            '#phone-login > p:nth-child(1) > input[type="text"]'
        )
        elem.send_keys(self.username)
        elem = self.driver.find_element_by_css_selector(
            '#password_pc'
        )
        elem.send_keys(self.password)
        elem = self.driver.find_element_by_css_selector(
            '#loginBt'
        )
        elem.click()
    
    def open_page(self, url):
        self.driver.get(url)


driver = webdriver.Chrome()
a = Spider('15501222719', 'iwantAplus1228!', driver)
a.login()
a.open_page('http://finance.caixin.com/2018-11-30/101354154.html')
input()