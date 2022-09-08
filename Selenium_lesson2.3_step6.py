from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()
    pc.copy(browser.switch_to.alert.text.split(': ')[-1]) #сохранить в буфер

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # Добавил комментарий