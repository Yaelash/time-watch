from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class LoginPage:
    url = 'http://checkin.timewatch.co.il/punch/punch.php'

    def __init__(self, browser):
        self.browser = browser

    def navigate(self):
        self.browser.get(self.url)

    def fill_cells(self, comp, emp, pw):
        company = self.browser.find_element_by_name("comp")
        company.clear()
        company.send_keys(comp)
        employee = self.browser.find_element_by_name("name")
        employee.clear()
        employee.send_keys(emp)
        password = self.browser.find_element_by_name("pw")
        password.clear()
        password.send_keys(pw)
        password.send_keys(Keys.RETURN)
        return PunchScreen(browser=self.browser)


class PunchScreen:
    def __init__(self, browser):
        self.browser = browser

    def go_to_update_punch(self):
        self.browser.find_element_by_xpath(
            '/html/body/div/table[2]/tbody/tr[1]/td[2]/form/div/div/table/tbody/tr[2]/td[2]/font/a/b').click()
        return UpdatePunchPage(browser=self.browser)


class UpdatePunchPage:
    def __init__(self, browser):
        self.browser = browser

    def update(self):
        while True:
            try:
                day = self.browser.find_element_by_xpath(
                    "/html/body/div/span/p[1]/table/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr/td[ 11]/font\
                    [@color='white']")
            except:
                return
            day.click()
            self.browser.switch_to_window(self.browser.window_handles[1])
            page = InOutPage(browser=self.browser)
            page.in_out()
            self.browser.switch_to_window(self.browser.window_handles[0])


class InOutPage:
    def __init__(self, browser):
        self.browser = browser

    def in_out(self):
        in_hour = self.browser.find_element_by_name('ehh0')
        in_hour.send_keys(9)
        in_min = self.browser.find_element_by_name('emm0')
        in_min.send_keys(00)
        in_hour = self.browser.find_element_by_name('xhh0')
        in_hour.send_keys(19)
        in_min = self.browser.find_element_by_name('xmm0')
        in_min.send_keys(00)
        self.browser.find_element_by_xpath(
            '/html/body/div/span/form/table/tbody/tr[8]/td/div/div[2]/p/table/tbody/tr[9]/td/input').click()


def main():
    chrome = webdriver.Chrome()
    try:
        page = LoginPage(chrome)
        page.navigate()
        punch_screen = page.fill_cells(comp=****, emp=**, pw='******')
        update_time = punch_screen.go_to_update_punch()
        update_time.update()

    finally:
        sleep(5)
        chrome.close()


if __name__ == '__main__':
    main()
