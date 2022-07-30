from page_objects import PageObject, PageElement


class LoginPage(PageObject):
    input_email = PageElement(id_='user_email')
    input_password = PageElement(id_='user_password')
    btn_submit = PageElement(css='.btn')

    def fill_email(self, email: str) -> None:
        """Fill email on field email

        Args:
            email (str): email
        """
        self.input_email = email

    def fill_password(self, password: str) -> None:
        """Fill password on field password

        Args:
            password (str): password
        """
        self.input_password = password

    def submit(self) -> None:
        """Click on submit button
        """
        self.btn_submit.click()
