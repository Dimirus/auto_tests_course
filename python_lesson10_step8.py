import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    time.sleep(0)
    # trying during 12 sec until price is $100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
    (By.ID, "price"), '$100')
    )
    # buying 
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    #get x_element
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    #calculate desigion
    y = calc(x)
    #enter the answer into the form
    desigion = browser.find_element(By.ID, "answer")
    desigion.send_keys(y)
    #find submit button and press it
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    
finally:
    #printing alert text on console
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла