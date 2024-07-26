import logging
import sys

from library.composer.vd_path import PathVD
from library.model.vd_config import ConfigVD

sys.path.append(".")
sys.path.append("src")
import allure
import pytest
from playwright.sync_api._generated import Page
from pytest_metadata.plugin import metadata_key

from library.helper.vd_play import PlayVD

logging.basicConfig(level=logging.INFO, format="\n%(message)s", stream=sys.stderr)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def pytest_html_report_title(report):
    report.title = f"Test Report - {ConfigVD.Project.get_project_name()}"


def pytest_configure(config):
    config.stash[metadata_key].pop("Packages")
    config.stash[metadata_key].pop("Plugins")


@allure.title(test_title="Setup / Teardown")
@pytest.fixture
def playVD(request: pytest.FixtureRequest, page: Page) -> PlayVD:  # type: ignore
    file_path: str = (
        f"src/tests/{str(object=PathVD(request.node.fspath)).split('src/tests/')[1]}"
    )
    method_name: str = request.node.name
    full_test_name: str = f"{file_path}::{method_name}"
    logger: logging.Logger = logging.getLogger(name=method_name)
    if logger.hasHandlers():
        logger.handlers.clear()
    formatter = logging.Formatter(fmt="%(message)s")
    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(fmt=formatter)
    logger.addHandler(hdlr=handler)
    logger.propagate = False
    playVD: PlayVD = PlayVD(
        page=page, method_name=method_name, logger=logger, full_test_name=full_test_name
    )
    yield playVD
    if request.node.rep_call.failed:
        # reason: str = (
        #     request.node.rep_call.longrepr
        #     if request.node.rep_call.longrepr
        #     else "Unknown reason"
        # )
        # selenium._append_json_log(message=f"Error : {reason}")
        try:
            playVD.allure_attach_screenshot(name="Failure | Screenshot")
        except Exception:
            pass
    playVD.close()
