from __future__ import annotations
from typing import Union
from playwright.sync_api import Page

from pages.home_page import HomePage


class LandingPage:
    def __init__(self, page: Page):
        self.page = page
        self.usernameInput = page.locator("#user-name")
        self.passwordInput = page.locator("#password")
        self.loginButton = page.locator("#login-button")

    def goToLandingPage(self) -> LandingPage:
        self.page.goto("https://www.saucedemo.com")
        return LandingPage(self.page)
    
    def login(self, username, password) -> HomePage:
        self.usernameInput.fill(username)
        self.passwordInput.fill(password)
        self.loginButton.click()
        return HomePage(self.page)