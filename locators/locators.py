from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.CSS_SELECTOR, "div[class='homePage_homepageStyle__WP-Y1']")
    LOGIN_AND_REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    HEADER_FIELD = (By.CSS_SELECTOR, "div.header_flexRow__Xdqv1")
    AVATAR_IMAGE = (By.CSS_SELECTOR, "button.circleSmall")


class RegistrationFormLocators:
    EMAIL_REGISTRATION_INPUT = (By.NAME, "email")
    PASSWORD_REGISTRATION_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_REGISTRATION_INPUT = (By.NAME, "submitPassword")
    EMAIL_CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    PARENT_EMAIL_REGISTRATION_INPUT = (By.XPATH, "./parent::div[@name='email']")
    PARENT_EMAIL_REGISTRATION_INPUT_ERROR = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
    WRONG_EMAIL_ERROR_SPAN = (By.XPATH, ".//span[text()='Ошибка']")

class LoginModalFormLocators:
    LOGIN_FORM_MODAL = (By.XPATH,".//div[@class='homePage_modal__zSdUB']")
    AUTH_MODAL_FORM = (By.XPATH,".//form[@class='popUp_shell__LuyqR']")
    NO_ACC_REG_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    EMAIL_LOGIN_INPUT = (By.NAME, "email")
    PASSWORD_LOGIN_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    
class AdsPageLocators:
    AD_CREATE_PAGE = (By.CSS_SELECTOR, "div[class='createListing_shell__A5EA7']")
    CREATE_AD_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    NEED_AUTH_MODAL_FORM = (By.XPATH,
        ".//div[@class='homePage_modal__zSdUB']//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    #«Название», «Описание товара», «Стоимость»
    UNIT_NAME = (By.CSS_SELECTOR, 'input[placeholder="Название"]')
    UNIT_DESCRIPTION = (By.CSS_SELECTOR, 'textarea[placeholder="Описание товара"]')
    UNIT_PRICE = (By.CSS_SELECTOR, 'input[placeholder="Стоимость"]')
    CITY_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "form > div.dropDownMenu_dropMenu__sBxhz > div.dropDownMenu_input__itKtw > button")
    CITY_DROPDOWN_BUTTON_KAZAN = (By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')][.//span[text()='Казань']]")
    CATEGORY_DROPDOWN_BUTTON = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_DROPDOWN_BUTTON_HOBBY = (By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')][.//span[text()='Технологии']]")
    CONDITION_RADIOBUTTON_USED = (By.CSS_SELECTOR, 'div[class="radioUnput_inputRegular__FbVbr"]')
    CONDITION_RADIOBUTTON_NEW = (By.CSS_SELECTOR, 'div[class="radioUnput_inputActive__eC-HY"]')
    PUBLISH_AD_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    OPEN_PROFILE_BUTTON = ()

class ProfilePageLocators:
    USER_PROFILE_PAGE = (By.CSS_SELECTOR, "div[class='profilePage_shell__8JYbq']")
    USER_PROFILE_PAGE_GRID = (By.CSS_SELECTOR, "div[class='profilePage_gridAndPaginaton__togPs']")
    USER_PROFILE_AD_NAME = (By.XPATH, ".//h2")
    USER_PROFILE_AD_CITY = (By.XPATH, ".//h3")
    USER_PROFILE_AD_PRICE = (By.XPATH, ".//div[@class='price']/h2")
    @staticmethod
    def user_profile_ad_card(title):
        return (By.XPATH, f"//div[@class='card'][.//h2[text()='{title}']]")
