from page_objects import PageObject, PageElement


class ItemsPage(PageObject):
    btn_new = PageElement(link_text='New item')

    def click_new(self) -> None:
        """ Click on new item button. """
        self.btn_new.click()


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
