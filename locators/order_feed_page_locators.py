from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    TOTAL_COMPLETED = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COMPLETED = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    IN_PROGRESS_ORDER = (By.XPATH, "//li[contains(@class, 'text_type_digits-default') and text()='{}']")