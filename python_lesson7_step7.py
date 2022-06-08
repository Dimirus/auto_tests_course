from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math 

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest_element = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
    x = chest_element.get_attribute("valuex")
    y = calc(x)
    print(y)
    #вбиваем ответ в форму
    desigion = browser.find_element(By.CSS_SELECTOR, "#answer")
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