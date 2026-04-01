import pytest
from appium import webdriver
from appium.options.common import AppiumOptions


def test_safari():

    options = AppiumOptions()

    options.set_capability("browserName", "Safari")
    options.set_capability("platformName", "iOS")

    options.set_capability("bstack:options", {
        "deviceName": "iPhone 14",
        "osVersion": "16",
        "realMobile": True
    })

    driver = webdriver.Remote(
        command_executor="https://sergeismirnov_ntl4h6:i7UzS3m9WzKrfzUDM5ka@hub-cloud.browserstack.com/wd/hub",
        # command_executor="https://YOUR_USERNAME:YOUR_ACCESS_KEY@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    driver.quit()