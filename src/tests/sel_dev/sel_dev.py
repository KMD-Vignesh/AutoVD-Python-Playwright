import pytest
from library.helper.vd_play import PlayVD
from pages.sel_dev.sel_dev_page import SelDevPage

from library.model.vd_config import ConfigVD


@pytest.mark.vignesh
@pytest.mark.sel_dev
def test_download_ie_driver(playVD: PlayVD) -> None:
    sel_dev_page = SelDevPage(playVD=playVD)
    sel_dev_page.open_app(url=ConfigVD.URL.get(key="SelDev")).assert_true(
        condition=sel_dev_page.is_sel_dev_page_loaded()
    ).scroll_to_latest_version().download_link_with_text(
        text_contains="64 bit Windows IE"
    ).check_file_download(file_name_contains="IEDriverServer")