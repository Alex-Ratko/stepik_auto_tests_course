from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH,"//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH,"//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH,"//input[@placeholder='Input your email']")
    input3.send_keys("test@mail.com")
    
    # Используем уникальный XPath-селектор для кнопки с текстом "Submit"
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
