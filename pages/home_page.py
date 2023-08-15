from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.openBurgerMenu = page.locator("#react-burger-menu-btn")
        self.openCartButton = page.locator('div[id=shopping_cart_container]')
        self.allItemsButton = page.locator("All items")
        self.aboutButton = page.locator("About")
        self.logoutButton = page.get_by_text("Logout")
        self.resetAppStateButton = page.get_by_text("Reset App State")
        self.productSortingButton = page.locator('select[data-test="product_sort_container"]')
        self.addToCartSauceBackPackButton = page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]')
        self.addToCartSauceLightButton = page.locator('button[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.addToCartSauceBoltTshirtButton = page.locator('button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.addToCartSauceJacketButton = page.locator('button[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
        self.addToCartSauceOnesieButton = page.locator('button[data-test="add-to-cart-sauce-labs-onesie"]')
        self.addToCartTshirtRedButton = page.locator('button[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

    def logout(self):
        self.openBurgerMenu.click()
        self.logoutButton.click()

    def about(self):
        self.aboutButton.click()

    def resetState(self):
        self.resetAppStateButton.click()
    
    def sortByAtoZ(self):
        self.productSortingButton.select_option(value="az")

    def sortByZtoA(self):
        self.productSortingButton.select_option(value="za")

    def sortbyLowPrice(self):
        self.productSortingButton.select_option(value="lohi")
    
    def sortbyHighPrice(self):
        self.productSortingButton.select_option(value="hilo")

    def addToCartAllProducts(self):
        self.addToCartSauceBackPackButton.click()
        self.addToCartSauceLightButton.click()
        self.addToCartSauceBoltTshirtButton.click()
        self.addToCartSauceJacketButton.click()
        self.addToCartSauceOnesieButton.click()
        self.addToCartTshirtRedButton.click()
        self.openCartButton.click()