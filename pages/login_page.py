import allure
from selenium.webdriver.support import expected_conditions as EC

from data import LOGIN_URL, STELLAR_BURGERS_URL
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(LOGIN_URL)

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait.until(EC.url_to_be(STELLAR_BURGERS_URL))