import pytest
from library.helper.vd_play import PlayVD
from pages.sauce_lab.main_page import MainPage

from library.model.vd_config import ConfigVD


@pytest.mark.vignesh
@pytest.mark.add_cart
def test_add_cart_badge_validation(playVD: PlayVD) -> None:
    main_page = MainPage(playVD=playVD)
    main_page.open_app(url=ConfigVD.URL.get(key="SauceLab")).login_to_app(
        username=ConfigVD.Credentials.get(key="UserName"),
        password=ConfigVD.Credentials.get(key="Password"),
    ).assert_true(condition=main_page.is_main_page_loaded()).add_cart_product(
        product_name="Sauce Labs Bike Light"
    ).assert_true(condition=main_page.get_product_count_badge() == 1).add_cart_product(
        product_name="Sauce Labs Backpack"
    ).assert_true(condition=main_page.get_product_count_badge() == 2).add_cart_product(
        product_name="Sauce Labs Onesie"
    ).assert_true(condition=main_page.get_product_count_badge() == 3)


@pytest.mark.vignesh
@pytest.mark.add_cart
def test_add_cart_badge_validation_fail(playVD: PlayVD) -> None:
    main_page = MainPage(playVD=playVD)
    main_page.open_app(url=ConfigVD.URL.get(key="SauceLab")).login_to_app(
        username=ConfigVD.Credentials.get(key="UserName"),
        password=ConfigVD.Credentials.get(key="Password"),
    ).assert_true(condition=main_page.is_main_page_loaded()).add_cart_product(
        product_name="Sauce Labs Bike Light"
    ).assert_true(
        condition=main_page.get_product_count_badge() == 5,
        failure_message=f"{main_page.get_product_count_badge()} == 5",
    )
