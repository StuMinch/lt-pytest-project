import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

@pytest.mark.parametrize(
    "url, expected_title",
    [
        ("https://sony.com", "Sony Group Portal - Home"),
        ("https://lambdatest.com", "Power Your Software Testing with AI and Cloud | LambdaTest"),
    ],
)
def test_page_title(driver, url, expected_title):
    driver.get(url)
    status = "passed" if driver.title == expected_title else "failed"
    driver.execute_script("lambda-status={}".format(status))
    assert driver.title == expected_title, f"Page title mismatch. Expected: {expected_title}, Actual: {driver.title}"
    driver.quit()
