from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/execute_script.html"
try:
    #get access to Chromedriver
    browser = webdriver.Chrome()
    #get link of testing resource
    browser.get(link)
    #get x_element
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    #calculate desigion
    y = calc(x)
    #enter the answer into the form
    desigion = browser.find_element(By.CSS_SELECTOR, ".form-control")
    desigion.send_keys(y)
    #tick the checkbox
    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check1.click()
    #find the radiobutton
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    #scroll page
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    #tick the radiobutton
    radiobutton.click()
    #find the button
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    #scroll page
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #click the button
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла