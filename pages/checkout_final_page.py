from playwright.sync_api import Page

class CheckoutFinalPage:
    def __init__(self, page: Page):
        self.page = page
        self.openBurgerMenu = page.locator("#react-burger-menu-btn")
        self.finishOrderButton = page.locator('button[data-test="finish"]')
    
    def finalizeOrder(self):
        self.finishOrderButton.click()