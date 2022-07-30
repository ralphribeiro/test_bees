from functools import partial

from .items import ItemPage, ItemsPage, ItemsPageCreate


def get_page_object(which: str, page: str, driver):
    """PageObjects factory

    Args:
        which (str): which
        page (str): which page
        driver (Selenium.webdriver): webdriver

    Returns:
        PageObject: PageObject
    """    
    whichs = {
        'item': {
            'create': partial(ItemsPageCreate, driver),
            'detail': partial(ItemPage, driver),
            'all': partial(ItemsPage, driver)
        },
        'deposit': {

        },
        'inventory': {

        }
    }
    return whichs[which][page]()