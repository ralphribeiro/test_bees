from page_objects import PageObject

from .page_element import PageElementPolling as PageElement
from .page_element import MultiPageElementPolling as MultiPageElement


class ItemsPage(PageObject):
    btn_new = PageElement(link_text='New item')
    success_destroyed_message = PageElement(
        xpath="//p[contains(.,'Item was successfully destroyed.')]")
    table = MultiPageElement(
        tag_name="tr")
        # xpath="//div[@id='items']/table/tbody/tr")

    def click_new(self) -> None:
        """ Click on new item button. """
        self.btn_new.click()

    def get_success_destroyed_message(self) -> str:
        """ Get successfully destroyed message. """
        return self.success_destroyed_message.text

    def get_len_table(self) -> int:
        """ Get len of items table. """
        return len(self.table)


class ItemsPageCreate(PageObject):
    field_name = PageElement(id_='item_name')
    field_height = PageElement(id_="item_height")
    field_width = PageElement(id_="item_width")
    field_weight = PageElement(id_="item_weight")
    btn_submit = PageElement(name='commit')

    def fill_name(self, text: str) -> None:
        """ Fill name on field name. """
        self.field_name = text

    def fill_height(self, text: str) -> None:
        """ Fill height on field height. """
        self.field_height = text

    def fill_width(self, text: str) -> None:
        """ Fill width on field width. """
        self.field_width = text

    def fill_weight(self, text: str) -> None:
        """ Fill weight on field weight. """
        self.field_weight = text

    def submit(self) -> None:
        """ Click on create item """
        self.btn_submit.click()


class ItemPage(PageObject):
    successfully_msg = PageElement(css='.container > p')
    name = PageElement(css='p:nth-child(1)')
    height = PageElement(css='p:nth-child(2)')
    width = PageElement(css='p:nth-child(3)')
    weight = PageElement(css='p:nth-child(4)')
    btn_destroy = PageElement(css='.button_to:nth-child(3) > button')
    link_edit = PageElement(link_text='Edit this item')

    def get_success_message(self) -> str:
        """ Get message successfully created. """
        return self.successfully_msg.text

    def get_name(self) -> str:
        """ Get name text. """
        return self.name.text

    def get_height(self) -> str:
        """ Get height text. """
        return self.height.text

    def get_width(self) -> str:
        """ Get width text. """
        return self.width.text

    def get_weight(self) -> str:
        """ Get weight text. """
        return self.weight.text

    def delete(self) -> None:
        """ Click on destroy button. """
        self.btn_destroy.click()

    def edit(self) -> None:
        """ Click on edit this item. """
        self.link_edit.click()
