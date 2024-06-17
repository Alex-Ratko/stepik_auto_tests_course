from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Импортируем функцию log из модуля math
from math import log

def calc(x):
    return str(log(abs(12*math.sin(x))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждем приемлимой цены на странице в 100 долларов и кликаем на кнопку Book
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book_button = browser.find_element(By.ID,"book")   
    book_button.click()

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
