from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_AND_REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    HEADER_FIELD = (By.CSS_SELECTOR, "header_flexRow__Xdqv1")

class RegistrationLocators:
    LOGIN_AND_REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")

class LoginModalFormLocators:
    LOGIN_FORM_MODAL = (By.XPATH,".//div[@class='homePage_modal__zSdUB']")
    AUTH_MODAL_FORM = (By.XPATH,".//form[@class='popUp_shell__LuyqR']")

    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    NO_ACC_REG_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")

    EMAIL_REGISTRATION_INPUT = (By.NAME, "email")

    PARENT_EMAIL_REGISTRATION_INPUT = (By.XPATH, "./parent::div[@name='email']")
    PARENT_EMAIL_REGISTRATION_INPUT_ERROR = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
    WRONG_EMAIL_ERROR_SPAN = (By.XPATH, ".//span[text()='Ошибка']")

    EMAIL_PASSWORD_REGISTRATION_INPUT = (By.NAME, "password")
    EMAIL_SUBMIT_PASSWORD_REGISTRATION_INPUT = (By.NAME, "submitPassword")

    EMAIL_CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")