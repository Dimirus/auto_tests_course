import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/find_link_text"
formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(formula)

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    link2 = browser.find_element(By.LINK_TEXT, formula)
    link2.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    print(input3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла