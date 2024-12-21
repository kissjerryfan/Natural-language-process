def order():
    """
        order food in Xiangjiang Restaurant.

        Args:
        None

        Returns:
        None
        """
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    driver = webdriver.Chrome()
    driver.get("https://csd2.order.place/store/112841/mode/takeaway")
    time.sleep(3)
    start = driver.find_element(By.CLASS_NAME, 'start-btn-box')
    start.click()
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    time.sleep(3)
    choose = driver.find_element(By.XPATH,
                                 '//*[@id="content"]/category-list-page/ion-content/ion-grid/ion-row/ion-col[1]')
    choose.click()

    time.sleep(3)
    add = driver.find_element(By.XPATH, '//*[@id="content"]/item-grid-scroll-page/ion-content/div/div/div[1]')
    add.click()

    time.sleep(3)
    addToOrder = driver.find_element(By.XPATH, '//*[@id="footer-box"]/div[2]/div[2]')
    addToOrder.click()
    time.sleep(3)
    bill = driver.find_element(By.XPATH, '//*[@id="content"]/item-grid-scroll-page/ion-footer/ion-button')
    bill.click()
    time.sleep(19)


