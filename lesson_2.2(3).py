from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля
    input1 = browser.find_element(By.NAME, "firstname") 
    input1.send_keys("Sanya")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ratko")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ratko.a@mail.ru")

    # Вставляем файл из директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # Ждем несколько секунд, чтобы увидеть результаты
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
