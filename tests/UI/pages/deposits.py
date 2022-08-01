from page_objects import PageObject

from .page_element import MultiPageElementPolling as MultiPageElement
from .page_element import PageElementPolling as PageElement


class DepositsPage(PageObject):
    btn_new = PageElement(link_text='New deposit')
    success_destroyed_message = PageElement(
        xpath="//p[contains(.,'Deposit was successfully destroyed.')]")
    table = MultiPageElement(
        tag_name="tr")
        # xpath="//div[@id='deposits']/table/tbody/tr")

    def click_new(self) -> None:
        """ Click on new deposit button. """
        self.btn_new.click()

    def get_success_destroyed_message(self) -> str:
        """ Get successfully destroyed message. """
        return self.success_destroyed_message.text

    def get_len_table(self) -> int:
        """ Get len of deposits table. """
        return len(self.table)


class DepositsPageCreate(PageObject):
    field_name = PageElement(id_='deposit_name')
    field_address = PageElement(id_='deposit_address')
    field_city = PageElement(id_='deposit_city')
    field_state = PageElement(id_='deposit_state')
    field_zipcode = PageElement(id_='deposit_zipcode')
    btn_submit = PageElement(name='commit')

    def fill_name(self, text: str) -> None:
        """ Fill name on field name. """
        self.field_name.clear()
        self.field_name = text

    def fill_address(self, text: str) -> None:
        """ Fill address on field address. """
        self.field_address.clear()
        self.field_address = text

    def fill_city(self, text: str) -> None:
        """ Fill city on field city. """
        self.field_city.clear()
        self.field_city = text

    def fill_state(self, text: str) -> None:
        """ Fill state on field state. """
        self.field_state.clear()
        self.field_state = text

    def fill_zipcode(self, text: str) -> None:
        """ Fill zipcode on field zipcode. """
        self.field_zipcode.clear()
        self.field_zipcode = text

    def submit(self) -> None:
        """ Click on create deposit """
        self.btn_submit.click()


class DepositPage(PageObject):
    successfully_msg = PageElement(css='.container > p')
    name = PageElement(css='p:nth-child(1)')
    address = PageElement(css='p:nth-child(2)')
    city = PageElement(css='p:nth-child(3)')
    state = PageElement(css='p:nth-child(4)')
    zipcode = PageElement(css='p:nth-child(5)')
    items = PageElement(css='p:nth-child(6)')
    btn_destroy = PageElement(css='.button_to:nth-child(3) > button')
    link_edit = PageElement(link_text='Edit this deposit')

    def get_success_message(self) -> str:
        """ Get message successfully created. """
        return self.successfully_msg.text

    def get_name(self) -> str:
        """ Get name text. """
        return self.name.text

    def get_address(self) -> str:
        """ Get address text. """
        return self.address.text

    def get_city(self) -> str:
        """ Get city text. """
        return self.city.text

    def get_state(self) -> str:
        """ Get state text. """
        return self.state.text

    def get_zipcode(self) -> str:
        """ Get zipcode text. """
        return self.zipcode.text

    def get_items(self) -> str:
        """ Get items text. """
        item = self.items.text
        return item.split(': ')[-1]

    def delete(self) -> None:
        """ Click on destroy button. """
        self.btn_destroy.click()

    def edit(self) -> None:
        """ Click on edit this deposit. """
        self.link_edit.click()