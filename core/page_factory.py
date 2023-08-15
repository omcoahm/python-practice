from playwright.sync_api import Page
from pages.cart_page import CartOverviewPage
from pages.checkout_final_page import CheckoutFinalPage
from pages.checkout_page import CheckoutInformationPage
from pages.home_page import HomePage
from pages.landing_page import LandingPage
from pages.return_to_home_page import ReturnToHomePage

class PageFactory():
    def __init__(self, page: Page):
        self.page = page

    def getLandingPage(self) -> LandingPage:
        return LandingPage(self.page)

    def getHomePage(self):
        return HomePage(self.page)
    
    def getCartPage(self):
        return CartOverviewPage(self.page)
    
    def getCheckoutInformationPage(self):
        return CheckoutInformationPage(self.page)
    
    def getCheckoutFinalPage(self):
        return CheckoutFinalPage(self.page)
    
    def getBackToHomePage(self):
        return ReturnToHomePage(self.page)
