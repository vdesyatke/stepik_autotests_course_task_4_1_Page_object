from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
from .pages.main_page import MainPage
from .pages.locators import BasePageLocators
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('link_nr', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link_nr):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_nr}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket(quiz_solve=True)
    assert page.addable_item_name == page.item_name_in_alert_message
    assert page.addable_item_price == page.amount_of_basket_in_alert_message


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket(quiz_solve=False)
    assert page.is_not_element_present(*ProductPageLocators.INNER_ALERT_MESSAGE_ITEM_ADDED_SUCCESS, 20)


def test_guest_cant_see_success_message(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.INNER_ALERT_MESSAGE_ITEM_ADDED_SUCCESS)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket(quiz_solve=False)
    assert page.is_disappeared(*ProductPageLocators.INNER_ALERT_MESSAGE_ITEM_ADDED_SUCCESS)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_not_element_present(
        *BasketPageLocators.TEXT_GOODS_IN_BASKET), 'Basket should be empty'
    assert basket_page.is_element_present(
        *BasketPageLocators.TEXT_BASKET_IS_EMPTY) and basket_page.browser.find_element(
        *BasketPageLocators.TEXT_BASKET_IS_EMPTY).text[
                                                      :18] == 'Ваша корзина пуста', 'Basket should be empty'


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        login_link = page.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(1)
        login_page = LoginPage(browser, browser.current_url)
        # assert login_page.should_be_login_page(), 'Seems like this is not login page'
        login_page.should_be_login_page()
        email = str(time.time()) + '@fakemail.org'
        password = '9023719528'
        login_page.register_new_user(email=email, password=password)
        assert login_page.is_element_present(*BasePageLocators.USER_ICON), 'No user icon found, seems like no user logged in'

    def test_user_cant_see_success_message(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.INNER_ALERT_MESSAGE_ITEM_ADDED_SUCCESS)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket(quiz_solve=False)
        assert page.addable_item_name == page.item_name_in_alert_message
        assert page.addable_item_price == page.amount_of_basket_in_alert_message
