from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_invalid')

# class MainPageLocators():


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDABLE_ITEM_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    ADDABLE_ITEM_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    NAME_OF_ITEM_ADDED_TO_BASKET_IN_INNER_ALERT_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BASKET_AMOUNT_IN_INNER_ALERT_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    INNER_ALERT_MESSAGE_ITEM_ADDED_SUCCESS = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')


class MainPageLocators:
    LINK_TO_BASKET_IN_HEADER_OF_MAIN_PAGE = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')

class BasketPageLocators:
    TEXT_GOODS_IN_BASKET = (By.CSS_SELECTOR, '#content_inner > div.basket-title.hidden-xs > div > h2')
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')

