from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT = (By.XPATH, "//p[text()='{}']/parent::a")
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='{}']/parent::a//p[contains(@class, 'counter_counter__num')]")

    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")

    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")