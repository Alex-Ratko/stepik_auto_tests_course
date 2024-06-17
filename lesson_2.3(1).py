from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Импортируем функцию log из модуля math
from math import log

def calc(x):
    return str(log(abs(12*math.sin(x))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_window = browser.window_handles[0]

    # Кликаем на кнопку на первой странице
    first_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    first_button.click()

    # Ждем несколько секунд, чтобы загрузилась вторая страница и ее элементы
    time.sleep(2)

    # Переключаемся на новое окно и даем второму окну имя
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

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
