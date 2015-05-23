import unittest
from TestBase import BaseClass
from selenium.webdriver.firefox.webdriver import WebDriver

class Group:
    def __init__(self, group_name, group_header, group_footer):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer

class Application():
    def __init__(self):
        #class GroupTestBase(BaseClass):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)




    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def login(self, user_name, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % user_name)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()










    def create_group(self, Group):
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.group_footer)
        wd.find_element_by_name("submit").click()

    def delete_group(self):
        wd = self.wd
        self.wd.find_element_by_link_text("groups").click()
        self.wd.find_element_by_css_selector("span.group").click()
        if not self.wd.find_element_by_name("selected[]").is_selected():
            self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()

    def click_group_page(self):
        wd = self.wd
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def off(self):
        self.delete_group()
        self.wd.find_element_by_link_text("Logout").click()
        self.wd.quit()