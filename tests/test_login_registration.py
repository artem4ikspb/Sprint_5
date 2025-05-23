import pytest
from data.test_data import red_color, login_data_success
from locators.locators import RegistrationFormLocators as RFL, \
                            LoginModalFormLocators as LMF, \
                            MainPageLocators as MPL
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.helpers import generate_random_email, generate_random_password

class TestLoginAndRegistration:
    def find_header_field(self, driver):
        return WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MPL.HEADER_FIELD),
            message=f"Can't find element by locator {MPL.HEADER_FIELD}"
        )

    def click_login_reg_button(self,driver):
        return driver.find_element(*MPL.LOGIN_AND_REG_BUTTON).click()

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
    
    def click_login_button(self, driver):
        return driver.find_element(*LMF.LOGIN_BUTTON).click()
    
    def click_logout_button(self, driver):
        return driver.find_element(*MPL.LOGOUT_BUTTON).click()

    def fill_reg_modal_form(self, driver, new_email, new_password):
        driver.find_element(*RFL.EMAIL_REGISTRATION_INPUT).send_keys(new_email)
        driver.find_element(*RFL.PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*RFL.SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(new_password)
        driver.find_element(*RFL.EMAIL_CREATE_ACCOUNT_BUTTON).click()

    def fill_login_form(self, driver, login_data):
        driver.find_element(*LMF.EMAIL_LOGIN_INPUT).send_keys(login_data.get('email'))
        driver.find_element(*LMF.PASSWORD_LOGIN_INPUT).send_keys(login_data.get('password'))

    
    def is_border_element_red(self, driver):
        error_element = driver.find_element(*RFL.PARENT_EMAIL_REGISTRATION_INPUT_ERROR)
        WebDriverWait(driver, 3).until(EC.visibility_of(error_element))
        border_color = error_element.value_of_css_property("border")
        return red_color in border_color
    
    def is_error_text_visible(self, driver):
        return 'Ошибка' == driver.find_element(*RFL.WRONG_EMAIL_ERROR_SPAN).text
    
    def is_avatar_present(self, driver):
        avatar = driver.find_element(*MPL.AVATAR_IMAGE)
        try:
            WebDriverWait(driver, 3).until(EC.visibility_of(avatar)) 
        except NoSuchElementException:
            return False
        return True

    def is_not_avatar_present(self, driver):
        avatar = driver.find_element(*MPL.AVATAR_IMAGE)
        try:
            WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(avatar)) 
        except NoSuchElementException:
            return False
        return True        
    
    def is_login_and_reg_button_present(self,driver):
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MPL.LOGIN_AND_REG_BUTTON)) 
        except NoSuchElementException:
            return False
        return True  


    def get_user_profile_name(self, driver):
        return driver.find_element(*MPL.PROFILE_NAME).text
    

    # Регистрация пользователя
    def test_user_registration_success(self, driver):
        email, password = generate_random_email(), generate_random_password()

        # Нажать кнопку «Вход и регистрация».
        self.click_login_reg_button(driver)
        auth_modal_form = self.find_auth_modal_form(driver)

        # Нажать кнопку «Нет аккаунта».
        self.click_no_acc_button(auth_modal_form)

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_modal_form = self.find_reg_form(driver)
        self.fill_reg_modal_form(reg_modal_form, email, password)
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу 
        #   около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert 'User.' == self.get_user_profile_name(driver), "Имя пользователя не соответствует заданному!"


    @pytest.mark.parametrize(
            'email, password',
            [
                ("23423.3242@goh", generate_random_password()),
                ("god@y.co", generate_random_password())
            ],
            ids=[
                'With wrong email',
                'Exist user'
            ]
    )
    def test_user_registration_is_imposible(self, driver, email, password):
        # Нажать кнопку «Вход и регистрация».
        self.click_login_reg_button(driver)
        auth_modal_form = self.find_auth_modal_form(driver)

        # Нажать кнопку «Нет аккаунта».
        self.click_no_acc_button(auth_modal_form)

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_modal_form = self.find_reg_form(driver)
        self.fill_reg_modal_form(reg_modal_form, email, password)
        
        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, 
        assert self.is_border_element_red(reg_modal_form), "Цвет Border должен быть красным!"
        #под полем Email отображается сообщение «Ошибка».
        assert self.is_error_text_visible(reg_modal_form), "Текст 'Ошибка' отсутствует!"

    # Login пользователя
    def test_login(self, driver):
        # Нажать кнопку «Вход и регистрация».
        self.click_login_reg_button(driver)
        auth_modal_form = self.find_auth_modal_form(driver)

        # Заполнить все поля формы авторизации и нажать кнопку «Войти».
        self.fill_login_form(auth_modal_form, login_data_success)
        self.click_login_button(auth_modal_form)

        #Проверить: произошёл переход на главную страницу, 
        # в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя 
        assert self.is_avatar_present(driver)
        # и имя User.
        assert 'User.' == self.get_user_profile_name(driver), "Имя пользователя не соответствует заданному!"

    # Logout пользователя
    def test_logout(self, driver):
        # Авторизоваться под заранее созданным пользователем.
        self.click_login_reg_button(driver)
        auth_modal_form = self.find_auth_modal_form(driver)
        self.fill_login_form(auth_modal_form, login_data_success)
        self.click_login_button(auth_modal_form)

        # Нажать кнопку «Выйти».
        self.click_logout_button(driver)
        # Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», 
        assert self.is_not_avatar_present(driver), "Аватар отображается после logout"

        # там теперь отображается кнопка «Вход и регистрация».
        assert self.is_login_and_reg_button_present(driver), "Кнопка регистрации не видна"