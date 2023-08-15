from playwright.sync_api import Page

class ReturnToHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.openBurgerMenu = page.locator("#react-burger-menu-btn")
        self.backHomeButton = page.locator('button[data-test="back-to-products"]')
    
    def backToHomePage(self):
        self.backHomeButton.click()