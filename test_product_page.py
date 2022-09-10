from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    assert page.addable_item_name == page.item_name_in_alert_message
    assert page.addable_item_price == page.amount_of_basket_in_alert_message



    # time.sleep(100)


#     test_item_name_in_basket_is_same_as_added_item(page)
#
# def test_item_name_in_basket_is_same_as_added_item(page):
#     assert page.get_addable_item_name() == "The shellcoder's handbook"