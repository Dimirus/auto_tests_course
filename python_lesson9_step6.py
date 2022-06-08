from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math 
link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    #get access to Chromedriver
    browser = webdriver.Chrome()
    #get link of testing resource
    browser.get(link)
    #press the button
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    #switch to new window
    confirm = browser.switch_to.window(browser.window_handles[1])
    #get x_element
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    #calculate desigion
    y = calc(x)
    #enter the answer into the form
    desigion = browser.find_element(By.ID, "answer")
    desigion.send_keys(y)
    #find submit button and press it
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
    
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла