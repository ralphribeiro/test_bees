from time import sleep

from page_objects import MultiPageElement, PageElement
from selenium.common.exceptions import NoSuchElementException


RETRY = 5


def find_one(self, context):
    """Find element with polling

    Args:
        context (webdriver): webdriver

    Returns:
        webdriver.element: element
    """
    retry = RETRY
    element = None
    while retry > 0:
        try:
            element = context.find_element(*self.locator)
            break
        except NoSuchElementException:
            retry -= 1
            sleep(1)
    return element


def find_many(self, context):
    """Find elements with polling

    Args:
        context (webdriver): webdriver

    Returns:
        webdriver.element: elements
    """
    retry = RETRY
    elements = None
    while retry > 0:
        try:
            elements = context.find_element(*self.locator)
            break
        except NoSuchElementException:
            retry -= 1
            sleep(1)
    return elements


"""
Monkey patching on PageElement and MultiPageElement to inject polling behavior
"""
PageElementPolling = PageElement
PageElementPolling.find = find_one

MultiPageElementPolling = MultiPageElement
MultiPageElementPolling.find = find_many
