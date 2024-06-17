from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Импортируем функцию log из модуля math
from math import log

def calc(x):
    return str(log(abs(12*math.sin(x))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем текстовое значение переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)

    # Вычисляем результат функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_field.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    robot_checkbox.click()

    # Скроллим страницу до конца
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    robots_rule_radiobutton.click()

    # Скрываем подвал страницы
    browser.execute_script("document.querySelector('footer').style.display = 'none';")

    # Находим кнопку "Submit" и кликаем на неё
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # Ждем несколько секунд, чтобы увидеть результаты
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
