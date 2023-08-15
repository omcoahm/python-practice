from playwright.sync_api import Page

class CheckoutInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.openBurgerMenu = page.locator("#react-burger-menu-btn")
        self.continueButton = page.locator('input[data-test="continue"]')
        self.firstNameInput = page.locator('input[data-test="firstName"]')
        self.lastNameInput = page.locator('input[data-test="lastName"]')
        self.postalCodeInput = page.locator('input[data-test="postalCode"]')
        
    def inputFullNamePostalCode(self):
        self.firstNameInput.fill("Testing")
        self.lastNameInput.fill("Reseting")
        self.postalCodeInput.fill("72000000")
        self.continueButton.click()