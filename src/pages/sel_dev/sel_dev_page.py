from dataclasses import dataclass
from typing import Literal, Self

from playwright.sync_api._generated import ElementHandle


from library.composer.vd_path import PathVD
from library.helper.vd_play import PlayVD
from library.interface.vd_page import PageVD


@dataclass
class SelDevPage(PageVD):
    def __init__(self, playVD: PlayVD) -> None:
        super().__init__(playVD=playVD)

    page_header: str = "#bindings"
    latest_version_download_link: str = "//p[contains(text(),'Latest stable version')]"
    
    all_download_links: str = "//p[@class='card-text']/a"

    def is_sel_dev_page_loaded(self) -> bool:
        is_present: bool = self.playVD.is_present(selector=self.page_header)
        if is_present:
            self.playVD.log(message="Validation : Sel Dev Page Loaded")
        return is_present

    def scroll_to_latest_version(self) -> Self:
        self.playVD.scroll_into_view_if_needed(
            selector=self.latest_version_download_link
        ).sleep(seconds=1)
        return self

    def download_link_with_text(self, text_contains: str) -> Self:
        ele_text_list: ElementHandle | None = self.playVD.find_element_with_text(
            selector=self.all_download_links, text_contains=text_contains
        )
        self.playVD.sleep(seconds=1)
        self.playVD.download_file_by_element(element_handle=ele_text_list)
        self.playVD.log(
            message=f"Validation : Text - {ele_text_list.text_content()} Present"
        ).sleep(seconds=1)
        return self

    def check_file_download(self, file_name_contains: str) -> Self:
        downloaded_file_path: PathVD | Literal[False] = (
            self.playVD.is_file_downloaded(file_name_contains=file_name_contains)
        )
        self.playVD.assert_true(condition=downloaded_file_path, failure_message="Downloaded File Not in Directory")
        self.playVD.delete_file(file_path=downloaded_file_path).sleep(seconds=2)
        return self
