from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math 

link = "http://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    #вбиваем ответ в форму
    desigion = browser.find_element(By.CSS_SELECTOR, ".form-control")
    desigion.send_keys(y)
    #ставим галку в чекбокс
    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check1.click()
    #тыкаем в радиобаттон
    radio1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio1.click()
    #жмём кнопку
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла