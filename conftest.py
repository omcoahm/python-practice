import pytest
from playwright.sync_api import Page
from core.page_factory import PageFactory

@pytest.fixture(scope="function")
def pf(page: Page):
    page_factory = PageFactory(page)
    yield page_factory