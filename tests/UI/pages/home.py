from page_objects import PageObject

from .page_element import PageElementPolling as PageElement


class HomePage(PageObject):
    successfully_login_msg = PageElement(
        xpath="//p[contains(.,'Signed in successfully.')]")
    btn_logout = PageElement(link_text='Logout')

    def logout(self) -> None:
        """ Click on logout """
        self.btn_logout.click()

    def get_success_login_message(self) -> str:
        """ Get message successfully created. """
        return self.successfully_login_msg.text
