from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

driver = webdriver.Chrome(service=Service(), options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 20)  # 等待最多 20 秒

def deadline():
    driver.get("https://moodle.hku.hk/")

    try:
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "btn-lambda-login")))
        login_button.click()
    except TimeoutException:
        print("未能找到 Login 按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        portal_login_button = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "HKU Portal user login")))
        portal_login_button.click()
    except TimeoutException:
        print("未能找到 HKU Portal user login 按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys("u3641280@connect.hku.hk")

        login_button = driver.find_element(By.ID, "login_btn")
        login_button.click()
    except TimeoutException:
        print("未能找到邮箱输入框或 LOG IN 按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        password_field = wait.until(EC.presence_of_element_located((By.ID, "passwordInput")))
        password_field.send_keys("B5STbX2910")

        login_button = driver.find_element(By.ID, "submitButton")
        login_button.click()
    except TimeoutException:
        print("未能找到密码输入框或登录按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        continue_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        continue_button.click()
    except TimeoutException:
        print("未能找到继续按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        yes_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        yes_button.click()
    except TimeoutException:
        print("未能找到是按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        calendar_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Full calendar")))
        calendar_button.click()
    except TimeoutException:
        print("未能找到 Full calendar 按钮，请检查页面加载速度或选择器是否正确")
        return

    try:
        calendar = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "calendarwrapper")))

        event_days = driver.find_elements(By.CSS_SELECTOR, "td.hasevent")

        deadlines = []

        for day in event_days:
            date = day.get_attribute("data-day")

            events = day.find_elements(By.CSS_SELECTOR, "li[data-region='event-item']")
            for event in events:
                event_name = event.find_element(By.CLASS_NAME, "eventname").text
                deadlines.append(f"{date} November 2024: {event_name}")

        print("本月所有的DDL事件：")
        for deadline in deadlines:
            print(deadline)

    except TimeoutException:
        print("未能找到日历中的事件，请检查页面加载速度或选择器是否正确")


if __name__ == "__main__":
    deadline()