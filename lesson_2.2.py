from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получем значение двух чисел
    x_element = browser.find_element(By.ID, "num1") 
    y_element = browser.find_element(By.ID, "num2")
    x = int(x_element.text)
    y = int(y_element.text)
    n = x + y

    # Получаем значение из списка
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(n)) # переводим результат в строку перед выбором 


    # Отправляем заполненную форму
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # Ждем несколько секунд, чтобы увидеть результаты
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
