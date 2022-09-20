from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


# 1. Гость открывает главную страницу
# 2. Переходит в корзину по кнопке в шапке сайта
# 3. Ожидаем, что в корзине нет товаров
# 4. Ожидаем, что есть текст о том что корзина пуста
@pytest.mark.secondstage
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    print('Before opening the browser')
    page.open()
    print('After opening the browser')
    link = browser.find_element(*MainPageLocators.LINK_TO_BASKET_IN_HEADER_OF_MAIN_PAGE)
    print('Successfully found element basket')
    link.click
    basket_page = BasketPage(browser, browser.current_url)
    print(browser.current_url)
    assert basket_page.is_not_element_present(*BasketPageLocators.TEXT_GOODS_IN_BASKET), 'Basket should be empty, but there ' \
                                                                                  'are goods in basket '
    # assert page.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text == 'Ваша корзина пуста'
