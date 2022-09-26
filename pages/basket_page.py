from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.TEXT_GOODS_IN_BASKET), 'Basket should be empty, but there are goods in basket'
        assert self.is_element_present(
            *BasketPageLocators.TEXT_BASKET_IS_EMPTY) and self.browser.find_element(
            *BasketPageLocators.TEXT_BASKET_IS_EMPTY).text[
                                                          :18] == 'Ваша корзина пуста', 'Basket should be empty, but ' \
                                                                                        'there are goods in basket '

