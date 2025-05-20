import time
import pytest
from pages.locators import DeskLocators as DL
from pages.desk_registration_page import DeskRegHelper 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from utils.helpers import generate_random_email, generate_random_password

class TestRegistration2(DeskRegHelper):

    # Регистрация пользователя
    def test_user_registration_success2(self, driver):
        new_email, new_password = generate_random_email(), generate_random_password()
        reg_page = DeskRegHelper(driver)
        reg_page.go_to_site()
        # Нажать кнопку «Вход и регистрация».
        reg_page.click_login_registration_btn()
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located(DL.NO_ACC_REG_BUTTON),
        #     message=f"Can't find element by locator {DL.NO_ACC_REG_BUTTON}"
        # )
        # Нажать кнопку «Нет аккаунта».
        reg_page.click_no_account_btn()

        # driver.find_element(*DL.NO_ACC_REG_BUTTON).click()
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located(DL.EMAIL_INPUT_REGISTRATION_INPUT),
        #     message=f"Can't find element by locator {DL.EMAIL_INPUT_REGISTRATION_INPUT}"
        # )

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_page.enter_new_email_and_pass(new_email, new_password)
        # driver.find_element(*DL.EMAIL_CREATE_ACCOUNT_BUTTON).click()
        # WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((DL.EXIT_BUTTON),  "Выйти"))
        
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу 
        #   около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert 'User.' == reg_page.get_profile_name()