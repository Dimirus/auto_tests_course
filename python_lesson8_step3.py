from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math 
def calc():
    return str(int(first) + int(second))
link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    #find first element of example
    first_el = browser.find_element(By.XPATH, '//h2/span[2]')
    first=first_el.text
    print(first)
    #find second element of example
    second_el = browser.find_element(By.XPATH, '//h2/span[4]')
    second=second_el.text
    print(second)
    #find dropdown list
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    #choose what we need
    print(calc())
    select.select_by_value(calc())
    #press a button
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла