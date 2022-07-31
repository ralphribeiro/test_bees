from functools import partial

from .items import ItemPage, ItemsPage, ItemsPageCreate
from .deposits import DepositPage, DepositsPage, DepositsPageCreate


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
            'create': partial(DepositsPageCreate, driver),
            'detail': partial(DepositPage, driver),
            'all': partial(DepositsPage, driver)
        },
        'inventory': {

        }
    }
    return whichs[which][page]()