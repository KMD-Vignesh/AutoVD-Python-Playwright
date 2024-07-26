from dataclasses import dataclass
from typing import Self

from library.helper.vd_play import PlayVD
from library.interface.vd_page import PageVD


@dataclass
class LoginPage(PageVD):
    def __init__(self, playVD: PlayVD) -> None:
        super().__init__(playVD=playVD)

    username_input: str = "#user-name"
    password_input: str = "#password"
    login_button: str = "#login-button"

    def login_to_app(self, username: str, password: str) -> Self:
        self.playVD.type(selector=self.username_input, fill_text=username)
        self.playVD.type(selector=self.password_input, fill_text=password)
        self.playVD.click(selector=self.login_button)
        self.playVD.log(message="Action : Logged into Application")
        return self
