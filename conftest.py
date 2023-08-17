import pytest
from playwright.sync_api import Page, BrowserContext
from core.page_factory import PageFactory

@pytest.fixture(scope="function")
def pf(page: Page, context: BrowserContext, request):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page_factory = PageFactory(page)
    yield page_factory
    if request.session.testsfailed != 0:
        context.tracing.stop(path = f"report/{request.node.name.split('[')[0]}.zip")