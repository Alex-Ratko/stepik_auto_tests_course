from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

# Импортируем функцию log из модуля math
from math import log

def calc(x):
    return str(log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Кликаем на кнопку на первой странице
    first_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    first_button.click()

    # Кликаем на кнопку в модальном окне
    confirm = browser.switch_to.alert
    confirm.accept()

    # Получаем икс и решаем формулу
    x_element = browser.find_element(By.ID, "input_value") 
    x = int(x_element.text)
    y = y = calc(x)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_field.send_keys(y)

    # Находим кнопку "Submit" и кликаем на неё
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # Ждем несколько секунд, чтобы увидеть результаты
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
