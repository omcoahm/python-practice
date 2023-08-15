#from playwright.sync_api import Page, sync_playwright, expect
from core.page_factory import PageFactory


def test_login_logout(pf: PageFactory) -> None:
    (pf.getLandingPage()
        .goToLandingPage()
        .login("standard_user", "secret_sauce")
        .logout())

def test_product_sorting(pf: PageFactory) -> None:
    (pf.getLandingPage()
     .goToLandingPage()
     .login("standard_user", "secret_sauce"))
    (pf.getHomePage()
     .sortByZtoA())
    (pf.getHomePage()
     .sortByAtoZ())
    (pf.getHomePage()
     .sortbyHighPrice())
    (pf.getHomePage()
     .sortbyLowPrice())    
    pf.getHomePage().logout()

def test_buyingAllProducts(pf: PageFactory) -> None:
    (pf.getLandingPage()
     .goToLandingPage()
     .login("standard_user", "secret_sauce"))
    (pf.getHomePage()
     .addToCartAllProducts())
    (pf.getCartPage()
     .checkoutCart())
    (pf.getCheckoutInformationPage()
     .inputFullNamePostalCode())
    (pf.getCheckoutFinalPage()
     .finalizeOrder())
    (pf.getBackToHomePage()
     .backToHomePage())
    (pf.getHomePage()
     .logout())