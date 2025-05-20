import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    # chrome_options = webdriver.ChromeOptions() # создали объект для опций
    # # chrome_options.add_argument('--headless') # добавили настройку
    # chrome_options.add_argument('--window-size=1024,768')
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.get('https://qa-desk.stand.praktikum-services.ru/')
    # yield driver
    # driver.quit()

    with webdriver.Chrome() as driver:
        driver.set_window_size(1024, 768)
        driver.implicitly_wait(0.5)
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        yield driver