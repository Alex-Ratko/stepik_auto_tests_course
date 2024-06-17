from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение из сундука
    box = x_element = browser.find_element(By.ID, "treasure")
    x = box.get_attribute("valuex")

    # Вычисляем результат функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_field.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    robots_rule_radiobutton.click()

    # Отправляем заполненную форму
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # Ждем несколько секунд, чтобы увидеть результаты
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
