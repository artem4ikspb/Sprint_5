from data.test_data import login_data_success
from locators.locators import LoginModalFormLocators as LMF, \
                            MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://qa-desk.stand.praktikum-services.ru/'


class TestLoginAndRegistration:

    # Login пользователя
    def test_login(self, driver):
        # Нажать кнопку «Вход и регистрация».
        driver.get(URL)
        driver.find_element(*MPL.MAIN_PAGE)

        driver.find_element(*MPL.LOGIN_AND_REG_BUTTON).click()        
        auth_modal_form = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}")
        
        # Заполнить все поля формы авторизации и нажать кнопку «Войти».
        auth_modal_form.find_element(*LMF.EMAIL_LOGIN_INPUT).send_keys(login_data_success.get('email'))
        auth_modal_form.find_element(*LMF.PASSWORD_LOGIN_INPUT).send_keys(login_data_success.get('password'))
        auth_modal_form.find_element(*LMF.LOGIN_BUTTON).click()

        #Проверить: произошёл переход на главную страницу, 
        # в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя
        driver.find_element(*MPL.MAIN_PAGE)
        avatar = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MPL.AVATAR_IMAGE),
            message= f"Can't find element by locator {LMF.AUTH_MODAL_FORM}") 
        assert avatar

        # и имя User.
        profile_name = driver.find_element(*MPL.PROFILE_NAME).text
        assert 'User.' == profile_name, "Имя пользователя не соответствует заданному!"

    # Logout пользователя
    def test_logout(self, driver):
        driver.get(URL)
        driver.find_element(*MPL.MAIN_PAGE)

        # Авторизоваться под заранее созданным пользователем.
        driver.find_element(*MPL.LOGIN_AND_REG_BUTTON).click()        
        auth_modal_form = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LMF.AUTH_MODAL_FORM),
            message=f"Can't find element by locator {LMF.AUTH_MODAL_FORM}")

        auth_modal_form.find_element(*LMF.EMAIL_LOGIN_INPUT).send_keys(login_data_success.get('email'))
        auth_modal_form.find_element(*LMF.PASSWORD_LOGIN_INPUT).send_keys(login_data_success.get('password'))
        auth_modal_form.find_element(*LMF.LOGIN_BUTTON).click()

        # Нажать кнопку «Выйти».
        driver.find_element(*MPL.MAIN_PAGE)
        logout_button= WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MPL.LOGOUT_BUTTON),
            message= f"Can't find element by locator {MPL.LOGOUT_BUTTON}") 
        logout_button.click()

        # Проверить: аватар пользователя и имя User больше не отображается 
        # в правом верхнем углу около кнопки «Разместить объявление», 
        avatar= WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(MPL.AVATAR_IMAGE),
            message= f"Can't find element by locator {MPL.AVATAR_IMAGE}") 
        assert avatar, "Аватар отображается после logout, но не должен"

        # там теперь отображается кнопка «Вход и регистрация».
        log_reg_button= WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MPL.LOGIN_AND_REG_BUTTON),
            message= f"Can't find element by locator {MPL.LOGIN_AND_REG_BUTTON}")
        assert log_reg_button, "Кнопка регистрации не видна"