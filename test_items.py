import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    time.sleep(30)
    button_text = button.text
    assert button_text, "Can't find basket button :("
