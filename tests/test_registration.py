import time
import pytest
from pages.locators import DeskLocators as DL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from utils.helpers import generate_random_email, generate_random_password

class TestRegistration:

    # Регистрация пользователя
    def test_user_registration_success(self, driver):
        new_email, new_password = generate_random_email(), generate_random_password()
        # driver.get('https://qa-desk.stand.praktikum-services.ru/')
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*DL.LOGIN_AND_REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(DL.NO_ACC_REG_BUTTON),
            message=f"Can't find element by locator {DL.NO_ACC_REG_BUTTON}"
        )
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*DL.NO_ACC_REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(DL.EMAIL_INPUT_REGISTRATION_INPUT),
            message=f"Can't find element by locator {DL.EMAIL_INPUT_REGISTRATION_INPUT}"
        )

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        driver.find_element(*DL.EMAIL_INPUT_REGISTRATION_INPUT).send_keys(new_email)
        driver.find_element(*DL.EMAIL_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*DL.EMAIL_SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*DL.EMAIL_CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((DL.EXIT_BUTTON),  "Выйти"))
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу 
        #   около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert 'User.' == driver.find_element(*DL.PROFILE_NAME).text

    # Регистрация пользователя c email не по маске  *******@*******.***
    def test_user_registration_with_bad_mask(self, driver):
        new_email, new_password = "23423.3242@goh", generate_random_password()
        # driver.get('https://qa-desk.stand.praktikum-services.ru/')
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*DL.LOGIN_AND_REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(DL.NO_ACC_REG_BUTTON),
            message=f"Can't find element by locator {DL.NO_ACC_REG_BUTTON}"
        )
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*DL.NO_ACC_REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(DL.EMAIL_INPUT_REGISTRATION_INPUT),
            message=f"Can't find element by locator {DL.EMAIL_INPUT_REGISTRATION_INPUT}"
        )

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        driver.find_element(*DL.EMAIL_INPUT_REGISTRATION_INPUT).send_keys(new_email)
        driver.find_element(*DL.EMAIL_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*DL.EMAIL_SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*DL.EMAIL_CREATE_ACCOUNT_BUTTON).click()

        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        child = driver.find_element(*DL.EMAIL_INPUT_REGISTRATION_INPUT)
        div_class = child.find_element(By.XPATH, "..").get_attribute("class")
        assert "inputError" in div_class


    @pytest.mark.skip
    # Регистрация уже существующего пользователя
    def test_user_registration_exist_user(self, driver):
        pass