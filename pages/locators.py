from selenium.webdriver.common.by import By

class DeskLocators:
    LOGIN_AND_REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    NO_ACC_REG_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    EMAIL_INPUT_REGISTRATION_INPUT = (By.NAME, "email")
    EMAIL_PASSWORD_REGISTRATION_INPUT = (By.NAME, "password")
    EMAIL_SUBMIT_PASSWORD_REGISTRATION_INPUT = (By.NAME, "submitPassword")
    EMAIL_CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")