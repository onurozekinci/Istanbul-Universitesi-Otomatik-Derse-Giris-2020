from selenium import webdriver
import time
import os
import getpass
import datetime
from selenium.webdriver.chrome.options import Options

class GetLecture:
    def __init__(self,iuser,ipassword,iders,igün,isaat):
        self.iuser=iuser
        self.ipassword=ipassword
        self.iders = iders
        self.igün = igün
        self.isaat = isaat
    
    def uygula(self):
        username = getpass.getuser()
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=C:/Users/{}/AppData/Local/Google/Chrome/User Data/".format(username))
        browser = webdriver.Chrome(executable_path=r"{}\drivers\chromedriver\chromedriver.exe".format(os.getcwd()),chrome_options=options)
        browser.get("https://oys.istanbul.edu.tr/login")
        time.sleep(3)
        try:
            user = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input")
            user.send_keys("0")
            user.clear()
            user.send_keys("{}".format(self.iuser))
            password = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input")
            password.send_keys("0")
            password.clear()
            password.send_keys("{}".format(self.ipassword))
            giris = browser.find_element_by_tag_name("button")
            giris.click()
            time.sleep(3)
            browser.get("https://oys.istanbul.edu.tr/dersler/takvim")
            time.sleep(3)
            ders=browser.find_element_by_partial_link_text("{}".format(self.iders))
            ders.click()
            sonclick=browser.find_element_by_tag_name("a")
            sonclick.click()
            time.sleep(40)
            browser.quit()
        except:
            browser.get("https://oys.istanbul.edu.tr/dersler/takvim")
            time.sleep(3)
            ders=browser.find_element_by_partial_link_text("{}".format(self.iders))
            ders.click()
            sonclick=browser.find_element_by_tag_name("a")
            sonclick.click()
            time.sleep(40) 
            browser.quit()
        
