from dataclasses import dataclass
from typing import Self

from library.helper.vd_play import PlayVD
from pages.sauce_lab.login_page import LoginPage


@dataclass
class MainPage(LoginPage):
    def __init__(self, playVD: PlayVD) -> None:
        super().__init__(playVD=playVD)

    main_page_header: str = "//div[@class='header_label']/div[text()='Swag Labs']"
    product_count_xpath: str = "//span[@class='shopping_cart_badge']"
    

    def is_main_page_loaded(self) -> bool:
        is_present: bool = self.playVD.is_present(selector=self.main_page_header)
        if is_present:
            self.playVD.log(message="Validation : Main Page Loaded")
            self.playVD.allure_attach_screenshot()
        return is_present

    def add_cart_product(self, product_name: str) -> Self:
        product_xpath: str = f"//div[text()='{product_name}']/../../..//button"
        
        self.playVD.scroll_into_view_if_needed(selector=product_xpath).sleep(seconds=1)
        self.playVD.click(selector=product_xpath).sleep(seconds=1)
        self.playVD.log(message=f"Action : {product_name} Added To Cart")
        return self

    def get_product_count_badge(self) -> int:
        product_count: int = int(
            self.playVD.get_text(selector=self.product_count_xpath)
        )
        self.playVD.scroll_into_view_if_needed(selector=self.main_page_header).sleep(seconds=1)
        self.playVD.allure_attach_element_screenshot(selector=self.product_count_xpath)
        self.playVD.log(
            message=f"Validation : Shopping Cart Badge Count = {product_count}"
        )
        return product_count
