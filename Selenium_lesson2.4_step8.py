from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
def open(x):
    return browser.get(x)

try:
    browser = webdriver.Chrome()
    open(" http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])  # сохранить в буфер

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # Добавил комментарий