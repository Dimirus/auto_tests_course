from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, os 
link = "http://suninjuly.github.io/file_input.html"
try:
    #get access to Chromedriver
    browser = webdriver.Chrome()
    #get link of testing resource
    browser.get(link)
    with open("short_bio.txt", "w") as file:
        content = file.write("short bio")  # create test.txt file
    #fill the fields
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("IP@ya.ru")
    #upload the file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file.name)
    print(file_path)
    choose = browser.find_element(By.ID, "file")
    choose.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    os.remove(file.name)

# не забываем оставить пустую строку в конце файла