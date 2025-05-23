import pytest
from locators.locators import RegistrationLocators as RL, \
                            LoginModalFormLocators as LMF, \
                            MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.helpers import generate_random_email, generate_random_password

class TestRegistration:
    def find_header_field(self, driver):
        return WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MPL.HEADER_FIELD),
            message=f"Can't find element by locator {MPL.HEADER_FIELD}"
        )

    def click_login_reg_button(self,driver):
        return driver.find_element(*RL.LOGIN_AND_REG_BUTTON).click()

    def find_auth_modal_form(self, driver):
        return WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}"
        )
    
    def find_reg_form(self, driver):
        return WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}"
        )

    def click_no_acc_button(self,driver):
        return driver.find_element(*LMF.NO_ACC_REG_BUTTON).click()
    
    def fill_reg_modal_form(self, driver, new_email, new_password):
        driver.find_element(*LMF.EMAIL_REGISTRATION_INPUT).send_keys(new_email)
        driver.find_element(*LMF.EMAIL_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*LMF.EMAIL_SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*LMF.EMAIL_CREATE_ACCOUNT_BUTTON).click()

    def is_border_element_red(self, driver):
        error_element = driver.find_element(*LMF.PARENT_EMAIL_REGISTRATION_INPUT_ERROR)
        WebDriverWait(driver, 3).until(EC.visibility_of(error_element))
        border_color = error_element.value_of_css_property("border")
        return "rgb(255, 105, 114)" in border_color
    
    def is_error_text_visible(self, driver):
        return 'Ошибка' == driver.find_element(*LMF.WRONG_EMAIL_ERROR_SPAN).text
    
    def get_user_name(self, driver):
        return driver.find_element(*RL.PROFILE_NAME).text

    # Регистрация пользователя
    def test_user_registration_success(self, driver):
        email, password = generate_random_email(), generate_random_password()

        # Нажать кнопку «Вход и регистрация».
        self.click_login_reg_button(driver)
    
        # Нажать кнопку «Нет аккаунта».
        auth_modal_form = self.find_auth_modal_form(driver)
        self.click_no_acc_button(auth_modal_form)

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_modal_form = self.find_reg_form(driver)
        self.fill_reg_modal_form(reg_modal_form, email, password)
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу 
        #   около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert 'User.' == self.get_user_name(driver), "Имя пользователя не соответствует заданному!"


    @pytest.mark.parametrize(
            'email, password',
            [
                ("23423.3242@goh", generate_random_password()),
                ("god@y.co", generate_random_password())
            ],
            ids=[
                'Registration with wrong email',
                'Registration exist user'
            ]
    )
    def test_user_registration_is_imposible(self, driver, email, password):
        # Нажать кнопку «Вход и регистрация».
        self.click_login_reg_button(driver)
    
        # Нажать кнопку «Нет аккаунта».
        auth_modal_form = self.find_auth_modal_form(driver)
        self.click_no_acc_button(auth_modal_form)

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_modal_form = self.find_reg_form(driver)
        self.fill_reg_modal_form(reg_modal_form, email, password)
        
        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, 
        assert self.is_border_element_red(reg_modal_form), "Цвет Border должен быть красным!"
        #под полем Email отображается сообщение «Ошибка».
        assert self.is_error_text_visible(reg_modal_form), "Текст 'Ошибка' отсутствует!"