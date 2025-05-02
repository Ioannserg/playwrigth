from checkout_page import CheckoutPage
from inventore_page import InventoryPage
from login_page import LoginPage


def test_site(browser):
    page = browser.new_page()
    login = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login.login("standard_user", "secret_sauce")
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('Ioann', 'Sergeeich', '123123123')

    return "Тест завершен"

