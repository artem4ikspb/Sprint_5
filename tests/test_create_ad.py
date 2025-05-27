import time
from selenium.webdriver.chrome.webdriver import WebDriver
from data.test_data import login_data_success, units
from locators.locators import RegistrationFormLocators as RFL, \
                            LoginModalFormLocators as LMF, \
                            MainPageLocators as MPL, \
                            AdsPageLocators as APL, \
                            ProfilePageLocators as PPL
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.helpers import get_random_unit


class TestCreateAds:
    def main_page(self, driver):
        return driver.find_element(*MPL.MAIN_PAGE)

    def login_reg_button(self,driver):
        return driver.find_element(*MPL.LOGIN_AND_REG_BUTTON)

    def create_advertisement_click(self, driver):
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(APL.CREATE_AD_BUTTON))
        button.click()
        return driver.find_element(*APL.AD_CREATE_PAGE)
    
    def open_unathorized_modal_form(self,driver):
        return WebDriverWait(driver, 3).until(EC.presence_of_element_located(APL.NEED_AUTH_MODAL_FORM))
    
    def login(self, driver, login_data):
        email = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LMF.EMAIL_LOGIN_INPUT))
        email.send_keys(login_data.get("email"))
        driver.find_element(*LMF.PASSWORD_LOGIN_INPUT).send_keys(login_data.get("password"))
        driver.find_element(*LMF.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.staleness_of(email))
    
    def fill_text_fields(self, driver, unit):
        driver.find_element(*APL.UNIT_NAME).send_keys(unit["name"])
        driver.find_element(*APL.UNIT_DESCRIPTION).send_keys(unit["description"])
        driver.find_element(*APL.UNIT_PRICE).send_keys(str(unit["price"]))

    def fill_drop_box(self, driver):
        dropdown_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(APL.CATEGORY_DROPDOWN_BUTTON))
        dropdown_button.click()
        element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(APL.CATEGORY_DROPDOWN_BUTTON_HOBBY))
        element.click()
        dropdown_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(APL.CITY_DROPDOWN_BUTTON))
        dropdown_button.click()
        element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(APL.CITY_DROPDOWN_BUTTON_KAZAN))
        element.click()

    def set_unit_condition(self, driver, unit):
        if unit.get("condition") == "new":
            return driver.find_element(*APL.CONDITION_RADIOBUTTON_NEW)
        return driver.find_element(*APL.CONDITION_RADIOBUTTON_USED)

    def publish_button_click(self, driver):
        driver.find_element(*APL.PUBLISH_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.staleness_of(driver))

    def open_user_profile(self, driver):
        driver.find_element(*MPL.AVATAR_IMAGE).click()
        return WebDriverWait(driver, 3).until(EC.presence_of_element_located(PPL.USER_PROFILE_PAGE))

    def get_ad_info_by_title(self, driver, card_name):
        commond_ads_list = driver.find_element(*PPL.USER_PROFILE_PAGE_GRID)
        card = commond_ads_list.find_element(*PPL.user_profile_ad_card(card_name))
        name = card.find_element(*PPL.USER_PROFILE_AD_NAME).text
        city = card.find_element(*PPL.USER_PROFILE_AD_CITY).text
        price_text = card.find_element(*PPL.USER_PROFILE_AD_PRICE).text
        price = int(price_text.replace("₽", "").replace(" ", "").strip())
        return name, city, price

    def get_count_ads_with_name(self, driver, card_name):
        commond_ads_list = driver.find_element(*PPL.USER_PROFILE_PAGE_GRID)
        cards = commond_ads_list.find_elements(*PPL.user_profile_ad_card(card_name))
        return len(cards)

    def is_unathorized_modal_form_shown(self, driver):
        try:
            self.open_unathorized_modal_form(driver)
        except NoSuchElementException:
            return False
        return True
        
    # Создание объявления неавторизованным пользователем
    # Что нужно сделать: 
    # Нажать кнопку «Разместить объявление».
    # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    def test_create_ad_without_auth(self, driver: WebDriver):
        self.create_advertisement_button(driver).click()
        assert self.is_unathorized_modal_form_shown(driver)



    # Создание объявления авторизованным пользователем
    # Что нужно сделать: 
    # Авторизоваться под заранее созданным пользователем.
    # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
    # Выбрать из Dropdown «Категорию» и «Город».
    # Выбрать RabioButton «Состояние товара».
    # Нажать кнопку «Опубликовать».
    # Перейти в профиль пользователя.
    # Проверить: в блоке «Мои объявления» отображается созданное объявление.
    #@pytest.mark.skip
    def test_create_ad_success(self, driver: WebDriver):
        unit = units[0]
        self.login_reg_button(driver).click()
        self.login(driver, login_data_success)
        profile_page = self.open_user_profile(driver)
        count_before_add_unit = self.get_count_ads_with_name(profile_page, unit.get('name'))
        adv_page = self.create_advertisement_click(driver)
        self.fill_text_fields(adv_page, unit)
        self.fill_drop_box(adv_page)
        self.set_unit_condition(adv_page, unit).click()
        self.publish_button_click(adv_page)
        profile_page = self.open_user_profile(driver)
        count_after_add_unit = self.get_count_ads_with_name(profile_page, unit.get('name'))
        name, city, price = self.get_ad_info_by_title(profile_page, unit.get('name'))
        assert name == unit.get('name'), f"Название товара > {name}, не соответствует ожидаемому > {unit.get('name')}"
        assert city == unit.get('city'), f"Название города > {city}, не соответствует ожидаемому > {unit.get('city')}"
        assert price == unit.get('price'), f"Цена > {price}, не соответствует ожидаемой > {unit.get('price')}"
        assert count_before_add_unit+1 == count_after_add_unit



