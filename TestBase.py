from selenium.webdriver.firefox.webdriver import WebDriver


class Profinity:
    long_word_20 = 'felixfelixfelixfelix'
    short_word_3 = 'qwe'
    correct_email = 'wqerty@gmail.ru'
    correct_data = 'test'
    symbol = """!"#$%&'()*+,-./09:;<=>?@[]^_`{}|~ """
    correct_phone_number = +3888091234521


class UserLogin:
    name = 'admin'
    password = 'secret'


class BaseClass():

    def __init__(self):
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




