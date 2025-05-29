from selenium.webdriver.chrome.webdriver import WebDriver
from data.test_data import login_data_success, units
from locators.locators import LoginModalFormLocators as LMF, \
                            MainPageLocators as MPL, \
                            AdsPageLocators as APL, \
                            ProfilePageLocators as PPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


URL = 'https://qa-desk.stand.praktikum-services.ru/'


class TestCreateAds:
    # Создание объявления неавторизованным пользователем
    # Что нужно сделать: 
    # Нажать кнопку «Разместить объявление».
    # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    def test_create_ad_without_auth(self, driver: WebDriver):
        driver.get(URL)
        button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(APL.CREATE_AD_BUTTON),
            message=f"Can't find element by locator {APL.CREATE_AD_BUTTON}")
        button.click()
        modal_form = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(APL.NEED_AUTH_MODAL_FORM),
            message=f"Can't find element by locator {APL.NEED_AUTH_MODAL_FORM}")
        assert modal_form

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
        driver.get(URL)
        button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(MPL.LOGIN_AND_REG_BUTTON),
            message=f"Can't find element by locator {MPL.LOGIN_AND_REG_BUTTON}")
        button.click()
    
        login_modal_form = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(LMF.LOGIN_FORM_MODAL),
            message=f"Can't find element by locator {LMF.LOGIN_FORM_MODAL}")
        login_modal_form.find_element(*LMF.EMAIL_LOGIN_INPUT).send_keys(login_data_success.get("email"))
        login_modal_form.find_element(*LMF.PASSWORD_LOGIN_INPUT).send_keys(login_data_success.get("password"))
        login_modal_form.find_element(*LMF.LOGIN_BUTTON).click()
        WebDriverWait(login_modal_form, 3).until(EC.staleness_of(login_modal_form))

        driver.find_element(*APL.CREATE_AD_BUTTON).click()
        adv_page = WebDriverWait(driver, 3).until(EC.presence_of_element_located(APL.AD_CREATE_PAGE))
        adv_page.find_element(*APL.UNIT_NAME).send_keys(unit["name"])
        adv_page.find_element(*APL.UNIT_DESCRIPTION).send_keys(unit["description"])
        adv_page.find_element(*APL.UNIT_PRICE).send_keys(str(unit["price"]))

        dropdown_button = adv_page.find_element(*APL.CATEGORY_DROPDOWN_BUTTON)
        dropdown_button.click()
        element = WebDriverWait(adv_page, 3).until(
            EC.element_to_be_clickable(APL.CATEGORY_DROPDOWN_BUTTON_HOBBY),
            message=f"Can't find element by locator {APL.CATEGORY_DROPDOWN_BUTTON_HOBBY}")
        element.click()
        dropdown_button = adv_page.find_element(*APL.CITY_DROPDOWN_BUTTON)
        dropdown_button.click()
        element = WebDriverWait(adv_page, 3).until(
            EC.element_to_be_clickable(APL.CITY_DROPDOWN_BUTTON_KAZAN),
            message=f"Can't find element by locator {APL.CITY_DROPDOWN_BUTTON_KAZAN}")
        element.click()
        if unit.get("condition") == "new":
            adv_page.find_element(*APL.CONDITION_RADIOBUTTON_NEW).click
        else: adv_page.find_element(*APL.CONDITION_RADIOBUTTON_USED).click
        adv_page.find_element(*APL.PUBLISH_AD_BUTTON).click()
        WebDriverWait(adv_page, 3).until(EC.staleness_of(adv_page))
        # driver.find_element(*MPL.MAIN_PAGE)

        driver.find_element(*MPL.AVATAR_IMAGE).click()
        profile_page = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(PPL.USER_PROFILE_PAGE),
            message=f"Can't find element by locator {PPL.USER_PROFILE_PAGE}")

        commond_ads_list = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(PPL.USER_PROFILE_PAGE_GRID),
            message=f"Can't find element by locator {PPL.USER_PROFILE_PAGE_GRID}")
        card = commond_ads_list.find_element(*PPL.user_profile_ad_card(unit.get('name')))
        name = card.find_element(*PPL.USER_PROFILE_AD_NAME).text
        city = card.find_element(*PPL.USER_PROFILE_AD_CITY).text
        price_text = card.find_element(*PPL.USER_PROFILE_AD_PRICE).text
        price = int(price_text.replace("₽", "").replace(" ", "").strip())

        assert name == unit.get('name'), f"Название товара > {name}, не соответствует ожидаемому > {unit.get('name')}"
        assert city == unit.get('city'), f"Название города > {city}, не соответствует ожидаемому > {unit.get('city')}"
        assert price == unit.get('price'), f"Цена > {price}, не соответствует ожидаемой > {unit.get('price')}"



