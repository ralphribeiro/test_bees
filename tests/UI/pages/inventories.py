from page_objects import PageObject

from .page_element import PageElementPolling as PageElement


class InventoriesPage(PageObject):
    btn_new = PageElement(link_text='New inventory')
    success_destroyed_message = PageElement(
        xpath="//p[contains(.,'Inventory was successfully destroyed.')]")

    def click_new(self) -> None:
        """ Click on new inventory button. """
        self.btn_new.click()

    def get_success_destroyed_message(self) -> str:
        """ Get successfully destroyed message. """
        return self.success_destroyed_message.text


class InventoriesPageCreate(PageObject):
    field_item_name = PageElement(id_='inventory_item_id')
    field_deposit_name = PageElement(id_="inventory_deposit_id")
    field_item_count = PageElement(id_="inventory_item_count")
    btn_submit = PageElement(name='commit')

    def fill_item_name(self, text: str) -> None:
        """ Fill item name on field item. """
        self.field_item_name = text

    def fill_deposit_name(self, text: str) -> None:
        """ Fill deposit name on field deposit. """
        self.field_deposit_name = text

    def fill_item_count(self, text: str) -> None:
        """ Fill item count in field item count. """
        self.field_item_count = text

    def submit(self) -> None:
        """ Click on create item """
        self.btn_submit.click()


class InventoryPage(PageObject):
    successfully_msg = PageElement(css='.container > p')
    item = PageElement(css='p:nth-child(1)')
    deposit = PageElement(css='p:nth-child(2)')
    item_count = PageElement(css='p:nth-child(3)')
    btn_destroy = PageElement(css='.button_to:nth-child(3) > button')
    link_edit = PageElement(link_text='Edit this inventory')

    def get_success_message(self) -> str:
        """ Get message successfully created. """
        return self.successfully_msg.text

    def get_item_name(self) -> str:
        """ Get item text. """
        return self.item.text

    def get_deposit_name(self) -> str:
        """ Get deposit text. """
        return self.deposit.text

    def get_item_count(self) -> str:
        """ Get item count text. """
        return self.item_count.text

    def delete(self) -> None:
        """ Click on destroy button. """
        self.btn_destroy.click()

    def edit(self) -> None:
        """ Click on edit this item. """
        self.link_edit.click()
