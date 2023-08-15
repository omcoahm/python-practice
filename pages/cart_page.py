from playwright.sync_api import Page

class CartOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.openBurgerMenu = page.locator("#react-burger-menu-btn")
        self.checkoutButton = page.locator('button[data-test="checkout"]')

    def checkoutCart(self):
        self.checkoutButton.click()