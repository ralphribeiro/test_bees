from functools import partial

from .items import ItemPage, ItemsPage, ItemsPageCreate
from .deposits import DepositPage, DepositsPage, DepositsPageCreate
from .inventories import InventoryPage, InventoriesPage, InventoriesPageCreate

def get_page_object(which: str, page: str, driver):
    """PageObjects factory

    Args:
        which (str): which (choices: item, deposit, inventory)
        page (str): which page (choices: create, detail, all)
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
            'create': partial(InventoriesPageCreate, driver),
            'detail': partial(InventoryPage, driver),
            'all': partial(InventoriesPage, driver)

        }
    }
    return whichs[which][page]()