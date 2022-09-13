from .pages.product_page import ProductPage
import time
import pytest

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# @pytest.mark.parametrize('link_nr', list(range(0,10)))
@pytest.mark.parametrize('link_nr', [0,1,2,3,4,5,6,pytest.param(7, marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket(browser, link_nr):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_nr}"
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()

    assert page.addable_item_name == page.item_name_in_alert_message
    assert page.addable_item_price == page.amount_of_basket_in_alert_message






#     test_item_name_in_basket_is_same_as_added_item(page)
#
# def test_item_name_in_basket_is_same_as_added_item(page):
#     assert page.get_addable_item_name() == "The shellcoder's handbook"