from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import elements


class LoginPage(elements.Login):
    url = 'http://checkin.timewatch.co.il/punch/punch.php'

    def __init__(self, browser):
        self.browser = browser

    def navigate(self):
        self.browser.get(self.url)

    def login(self, comp_id, emp_id, pw):
        company = self.browser.find_element(*self.company_number)
        company.clear()
        company.send_keys(comp_id)
        employee = self.browser.find_element(*self.employee_number)
        employee.clear()
        employee.send_keys(emp_id)
        password = self.browser.find_element(*self.employee_password)
        password.clear()
        password.send_keys(pw)
        password.send_keys(Keys.RETURN)
        return PunchScreen(browser=self.browser)


class PunchScreen(elements.PunchScreen):
    def __init__(self, browser):
        self.browser = browser

    def go_to_update_punch(self):
        self.browser.find_element(*self.update_punch).click()
        return UpdatePunchPage(browser=self.browser)


class UpdatePunchPage(elements.UpdatePunchPage):
    def __init__(self, browser):
        self.browser = browser

    def update(self):
        while True:
            try:
                day = self.browser.find_element(*self.day)
            except:
                return
            day.click()
            self.browser.switch_to_window(self.browser.window_handles[1])

            page = InOutPage(browser=self.browser)
            page.in_out()
            self.browser.switch_to_window(self.browser.window_handles[0])


class InOutPage(elements.InOut, elements.Args):
    def __init__(self, browser):
        self.browser = browser

    def in_out(self):
        in_hour = self.browser.find_element(*self.in_hour)
        in_hour.send_keys(self.my_in_hour)
        in_min = self.browser.find_element(*self.in_min)
        in_min.send_keys(self.my_in_min)
        out_hour = self.browser.find_element(*self.out_hour)
        out_hour.send_keys(self.my_out_hour)
        out_min = self.browser.find_element(*self.out_min)
        out_min.send_keys(self.my_out_min)
        self.browser.find_element(*self.update_button).click()


def main():
    chrome = webdriver.Chrome()
    try:
        page = LoginPage(chrome)
        page.navigate()
        punch_screen = page.login(comp_id=elements.Args.comp_id, emp_id=elements.Args.emp_id, pw=elements.Args.pw)
        update_time = punch_screen.go_to_update_punch()
        update_time.update()

    finally:
        sleep(5)
        chrome.close()


if __name__ == '__main__':
    main()
