import pytest
from data.test_data import red_color
from locators.locators import RegistrationFormLocators as RFL, \
                            LoginModalFormLocators as LMF, \
                            MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.helpers import generate_random_email

URL = 'https://qa-desk.stand.praktikum-services.ru/'


class TestRegistration:
   
    # Регистрация пользователя
    def test_user_registration_success(self, driver):
        email, password = generate_random_email(), 'pa$$w0rd'
        driver.get(URL)

        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*MPL.MAIN_PAGE)

        driver.find_element(*MPL.LOGIN_AND_REG_BUTTON).click()        
        auth_modal_form = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}")

        # Нажать кнопку «Нет аккаунта».
        auth_modal_form.find_element(*LMF.NO_ACC_REG_BUTTON).click()
        reg_modal_form = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}")

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_modal_form.find_element(*RFL.EMAIL_REGISTRATION_INPUT).send_keys(email)
        reg_modal_form.find_element(*RFL.PASSWORD_REGISTRATION_INPUT).send_keys(password)
        reg_modal_form.find_element(*RFL.SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(password)
        reg_modal_form.find_element(*RFL.EMAIL_CREATE_ACCOUNT_BUTTON).click()

        # Проверить: произошёл переход на главную страницу, в правом верхнем углу 
        #   около кнопки «Разместить объявление» 
        driver.find_element(*MPL.MAIN_PAGE)
        avatar = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MPL.AVATAR_IMAGE),
            message= f"Can't find element by locator {LMF.AUTH_MODAL_FORM}") 
        assert avatar

        # отображается аватар пользователя и имя User.
        profile_name = driver.find_element(*MPL.PROFILE_NAME).text
        assert 'User.' == profile_name, "Имя пользователя не соответствует заданному!"

    @pytest.mark.parametrize(
            'email, password',
            [
                ("23423.3242@goh", 'pa$$w0rd'),
                ("god@y.co", 'pa$$w0rd')
            ],
            ids=[
                'With wrong email',
                'Exist user'
            ]
    )
    def test_user_registration_is_imposible(self, driver, email, password):
        driver.get(URL)

        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*MPL.MAIN_PAGE)

        driver.find_element(*MPL.LOGIN_AND_REG_BUTTON).click()        
        auth_modal_form = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}")

        # Нажать кнопку «Нет аккаунта».
        auth_modal_form.find_element(*LMF.NO_ACC_REG_BUTTON).click()
        reg_modal_form = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}")

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»
        reg_modal_form.find_element(*RFL.EMAIL_REGISTRATION_INPUT).send_keys(email)
        reg_modal_form.find_element(*RFL.PASSWORD_REGISTRATION_INPUT).send_keys(password)
        reg_modal_form.find_element(*RFL.SUBMIT_PASSWORD_REGISTRATION_INPUT).send_keys(password)
        reg_modal_form.find_element(*RFL.EMAIL_CREATE_ACCOUNT_BUTTON).click()
        
        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, 
        error_element = WebDriverWait(reg_modal_form, 3).until(
            EC.presence_of_element_located(RFL.PARENT_EMAIL_REGISTRATION_INPUT_ERROR))
        border_color = error_element.value_of_css_property("border")
        assert red_color in border_color, "Цвет Border должен быть красным!"

        #под полем Email отображается сообщение «Ошибка».
        err_text = reg_modal_form.find_element(*RFL.WRONG_EMAIL_ERROR_SPAN).text
        assert 'Ошибка' == err_text, "Текст 'Ошибка' отсутствует!"
