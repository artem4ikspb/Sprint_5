from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import DeskLocators as DL
from pages.base_page import BasePage

class DeskRegHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_registration_btn(self):
        btn = self.find_element(*DL.LOGIN_AND_REG_BUTTON)
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located(DL.NO_ACC_REG_BUTTON),
        #     message=f"Can't find element by locator {DL.NO_ACC_REG_BUTTON}"
        # )
        return btn.click()
    
    def click_no_account_btn(self):
        return self.find_element(*DL.NO_ACC_REG_BUTTON).click()
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located(DL.EMAIL_INPUT_REGISTRATION_INPUT),
        #     message=f"Can't find element by locator {DL.EMAIL_INPUT_REGISTRATION_INPUT}"
        # )

    # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
    def enter_new_email_and_pass(self, email: str, password: str) -> None:
        self.find_element(*DL.EMAIL_INPUT_REGISTRATION_INPUT).send_keys(email)
        self.find_element(*DL.EMAIL_PASSWORD_REGISTRATION_INPUT).send_keys(password)
        self.find_element(*DL.EMAIL_SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(password)

    def click_create_new_account(self):
        self.find_element(*DL.EMAIL_CREATE_ACCOUNT_BUTTON).click()

    def get_profile_name(self) -> str:
        return self.find_element(*DL.PROFILE_NAME).text


