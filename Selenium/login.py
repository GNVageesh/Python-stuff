from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


web = webdriver.Chrome()
web.get('https://github.com/login')


def login_process(un, pw):
    unfield = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.ID, 'login_field')))
    unfield.clear()
    unfield.send_keys(un)
    pwfield = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    pwfield.clear()
    pwfield.send_keys(pw)
    signin_btn = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.NAME, 'commit')))
    signin_btn.click()
    logo = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div[7]/details/summary')))
    logo.click()
    signout_btn = WebDriverWait(web, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
    signout_btn.click()
    sleep(3)
    web.quit()


login_process('GNVageesh', 'vageeshgn123')
