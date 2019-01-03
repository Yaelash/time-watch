from selenium.webdriver.common.by import By
import argparse


class Login:
    company_number = (By.NAME, 'comp')
    employee_number = (By.NAME, 'name')
    employee_password = (By.NAME, 'pw')


class PunchScreen:
    update_punch = (By.XPATH, '/html/body/div/table[2]/tbody/tr[1]/td[2]/form/div/div/table/tbody/tr[2]/td[2]/font/a/b')


class UpdatePunchPage:
    day = (By.XPATH, "/html/body/div/span/p[1]/table/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr/td[ 11]/font\
                    [@color='white']")


class InOut:
    in_hour = (By.NAME, 'ehh0')
    in_min = (By.NAME, 'emm0')
    out_hour = (By.NAME, 'xhh0')
    out_min = (By.NAME, 'xmm0')
    update_button = (By.XPATH, '/html/body/div/span/form/table/tbody/tr[8]/td/div/div[2]/p/table/tbody/tr[9]/td/input')


class Args:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', required=True)
    parser.add_argument('-b', required=True)
    parser.add_argument('-c', required=True)
    parser.add_argument('-d', required=True)
    parser.add_argument('-e', required=True)
    parser.add_argument('-f', required=True)
    parser.add_argument('-g', required=True)

    args = parser.parse_args()

    comp_id = args.a
    emp_id = args.b
    pw = args.c
    my_in_hour = args.d
    my_in_min = args.e
    my_out_hour = args.f
    my_out_min = args.g

