from logging import Logger
import time
import allure
from typing import Literal, NoReturn, Self
from playwright.sync_api._generated import Download, ElementHandle, Frame, Page
import pytest

from library.composer.vd_path import PathVD
from library.model.vd_class import ValueVD
from library.model.vd_config import ConfigVD


class PlayVD:
    def __init__(
        self,
        page: Page,
        method_name: str,
        logger: Logger,
        full_test_name: str,
    ) -> None:
        self.page: Page = page
        self.logger: Logger = logger
        self.method_name: str = method_name
        self.full_test_name: str = full_test_name
        self.browser_name: str = self.page.context.browser.browser_type.name.title()

    def sleep(self, seconds: int | float) -> Self:
        time.sleep(seconds)
        return self

    def get_page(self) -> Page:
        return self.page

    def log(self, message: str) -> Self:
        self.logger.info(msg=message)
        with allure.step(title=message):
            pass
        return self

    def test_fail(self, failure_message: str) -> NoReturn:
        pytest.fail(failure_message)

    def assert_true(self, condition: bool, failure_message: str = "Assertion") -> Self:
        if not condition:
            self.test_fail(failure_message=failure_message)
        return self

    def assert_false(self, condition: bool, failure_message: str = "Assertion") -> Self:
        if condition:
            self.test_fail(failure_message=failure_message)
        return self

    def get_title(self) -> str:
        return self.get_page().title()

    def get_url(self) -> str:
        return self.get_page().url

    def get_page_content(self) -> str:
        return self.get_page().content()

    def bring_to_front(self) -> Self:
        self.get_page().bring_to_front()
        return self

    def open(self, url: str) -> Self:
        self.get_page().goto(url=url)
        short_url: str = ConfigVD.URL.find_name_url_list(value=url)
        if not short_url:
            short_url = url.split("//")[1].split(".")[0].lower()
            short_url = (
                short_url.title()
                if "www" not in short_url
                else url.split("//")[1].split(".")[1].title()
            )
        self.log(message=f"\nSetup : {self.browser_name} Opening URL - {short_url}")
        return self

    def is_present(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        for _ in range(timeout):
            if len(self.get_page().query_selector_all(selector=selector)) > 0:
                return True
            else:
                self.sleep(seconds=1)
        return False

    def find_element(
        self, selector: str, timeout: float = ValueVD.time_out()
    ) -> ElementHandle:
        if self.is_present(selector=selector, timeout=timeout):
            return self.get_page().query_selector(selector=selector)
        else:
            self.test_fail(failure_message=f"Locator Not Found - {selector}")

    def find_elements(
        self, selector: str, timeout: float = ValueVD.time_out()
    ) -> list[ElementHandle]:
        if self.is_present(selector=selector, timeout=timeout):
            return self.get_page().query_selector_all(selector=selector)
        else:
            self.test_fail(failure_message=f"Locator Not Found - {selector}")

    def tap(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).tap()
        return self

    def click(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).click()
        return self

    def right_click(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).click(button="right")
        return self

    def force_click(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).click(force=True)
        return self

    def multi_click(
        self, selector: str, click_count: int, timeout: float = ValueVD.time_out()
    ) -> Self:
        self.find_element(selector=selector, timeout=timeout).click(
            click_count=click_count
        )
        return self

    def dblclick(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).dblclick()
        return self

    def hover(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).hover()
        return self

    def scroll_into_view_if_needed(
        self, selector: str, timeout: float = ValueVD.time_out()
    ) -> Self:
        self.find_element(
            selector=selector, timeout=timeout
        ).scroll_into_view_if_needed()
        return self

    def check(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).check()
        return self

    def focus(self, selector: str, timeout: float = ValueVD.time_out()) -> Self:
        self.find_element(selector=selector, timeout=timeout).focus()
        return self

    def input_value(self, selector: str, timeout: float = ValueVD.time_out()) -> str:
        return self.find_element(selector=selector, timeout=timeout).input_value()

    def inner_html(self, selector: str, timeout: float = ValueVD.time_out()) -> str:
        return self.find_element(selector=selector, timeout=timeout).inner_html()

    def inner_text(self, selector: str, timeout: float = ValueVD.time_out()) -> str:
        return self.find_element(selector=selector, timeout=timeout).inner_text()

    def get_attribute(
        self, selector: str, attribute_name: str, timeout: float = ValueVD.time_out()
    ) -> str | None:
        return self.find_element(selector=selector, timeout=timeout).get_attribute(
            name=attribute_name
        )

    def is_checked(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        return self.find_element(selector=selector, timeout=timeout).is_checked()

    def is_disabled(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        return self.find_element(selector=selector, timeout=timeout).is_disabled()

    def is_editable(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        return self.find_element(selector=selector, timeout=timeout).is_editable()

    def is_enabled(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        return self.find_element(selector=selector, timeout=timeout).is_enabled()

    def is_hidden(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        return self.find_element(selector=selector, timeout=timeout).is_hidden()

    def is_visible(self, selector: str, timeout: float = ValueVD.time_out()) -> bool:
        return self.find_element(selector=selector, timeout=timeout).is_visible()

    def get_text(
        self, selector: str, timeout: float = ValueVD.time_out()
    ) -> str | None:
        return self.find_element(selector=selector, timeout=timeout).text_content()

    def get_text_elements(
        self, selector: str, timeout: float = ValueVD.time_out()
    ) -> list[str]:
        return [
            element.text_content()
            for element in self.find_elements(selector=selector, timeout=timeout)
        ]

    def is_text_in_elements(
        self, selector: str, element_text: str, timeout: int = ValueVD.time_out()
    ) -> bool:
        return element_text in self.get_text_elements(
            selector=selector, timeout=timeout
        )

    def is_text_contains_in_elements(
        self, selector: str, text_contains: str, timeout: int = ValueVD.time_out()
    ) -> bool:
        return any(
            text_contains in element
            for element in self.get_text_elements(selector=selector, timeout=timeout)
        )

    def find_element_with_text(
        self,
        selector: str,
        text_contains: str,
        timeout: int = ValueVD.time_out(),
    ) -> ElementHandle | None:
        for element in self.find_elements(selector=selector, timeout=timeout):
            if text_contains in element.text_content():
                return element
        return None

    def fill(
        self, selector: str, fill_text: str, timeout: float = ValueVD.time_out()
    ) -> Self:
        self.find_element(selector=selector, timeout=timeout).fill(value=fill_text)
        return self

    def type(
        self, selector: str, fill_text: str, timeout: float = ValueVD.time_out()
    ) -> Self:
        self.find_element(selector=selector, timeout=timeout).type(text=fill_text)
        return self

    def press_key(
        self, selector: str, key: str, timeout: float = ValueVD.time_out()
    ) -> Self:
        self.find_element(selector=selector, timeout=timeout).press(key=key)

    def type_enter(
        self, selector: str, fill_text: str, timeout: float = ValueVD.time_out()
    ) -> Self:
        return self.type(
            selector=selector, fill_text=fill_text, timeout=timeout
        ).press_key(selector=selector, key="Enter")

    def close(self) -> Self:
        self.get_page().close()
        self.log(message=f"\nTeardown : {self.browser_name} Closing")
        return self

    def drag_and_drop(self, source_selector: str, target_selector: str) -> Self:
        self.get_page().drag_and_drop(source=source_selector, target=target_selector)
        return self

    def allure_attach_screenshot(self, name: str = "Page | Screenshot") -> Self:
        with allure.step(title=name):
            allure.attach(
                self.get_page().screenshot(),
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )
            return self

    def switch_frame(self, frame_name: str) -> Frame | None:
        return self.get_page().frame(name=frame_name)

    def click_inside_frame(
        self, frame_name: str, selector: str, timeout: float = ValueVD.time_out()
    ) -> Self:
        self.switch_frame(frame_name=frame_name).click(
            selector=selector, timeout=timeout
        )
        return self

    def type_inside_frame(
        self,
        frame_name: str,
        selector: str,
        fill_text: str,
        timeout: float = ValueVD.time_out(),
    ) -> Self:
        self.switch_frame(frame_name=frame_name).type(
            selector=selector, text=fill_text, timeout=timeout
        )
        return self

    def allure_attach_element_screenshot(
        self, selector: str, name: str = "Element | Screenshot"
    ) -> Self:
        with allure.step(title=name):
            allure.attach(
                self.find_element(selector=selector).screenshot(),
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )
        return self

    def get_path_vd(self) -> PathVD:
        return PathVD

    def download_file(self, selector: str, timeout: float = ValueVD.time_out()) -> str:
        try:
            with self.get_page().expect_download(
                timeout=timeout * 1000
            ) as download_info:
                self.click(selector=selector, timeout=timeout)
        except Exception:
            self.test_fail(failure_message=f"No Download Triggered For - {selector}")
        download: Download = download_info.value
        download.save_as(path=PathVD.download_path() / download.suggested_filename)
        return download.suggested_filename

    def download_file_by_element(
        self,
        element_handle: ElementHandle,
        timeout: float = ValueVD.time_out_milli_seconds(),
    ) -> str:
        with self.get_page().expect_download(timeout=timeout) as download_info:
            element_handle.click(timeout=timeout)
        download: Download = download_info.value
        download.save_as(path=PathVD.download_path() / download.suggested_filename)
        return download.suggested_filename

    def is_file_downloaded(
        self,
        file_name_contains: str,
        directory_path: str | PathVD = PathVD.download_path(),
        wait_seconds: int = ValueVD.time_out(),
    ) -> PathVD | Literal[False]:
        file_path: PathVD | Literal[False] = self.get_path_vd().file_name_contains(
            directory_path=directory_path,
            file_name_contains=file_name_contains,
            wait_seconds=wait_seconds,
        )
        if file_path:
            self.log(message=f"Validation : {file_path.name} Present in Directory")
        return file_path

    def delete_file(self, file_path: str | PathVD) -> Self:
        self.get_path_vd().delete_file(file_path=file_path)
        return self
