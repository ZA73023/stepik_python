from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector('[type="text"]')
    for element in elements:
        element.send_keys("Тути Тути Тути")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()



