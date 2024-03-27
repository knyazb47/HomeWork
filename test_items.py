from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_first(browser):
    browser.get(link)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), "Button didn't found"


