import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize(
    "url, expected_title",
    [
        ("http://localhost:5000", "Login Page"),
        ("https://lambdatest.com", "Power Your Software Testing with AI and Cloud | LambdaTest"),
    ],
)
def test_page_title(driver, url, expected_title):
    driver.get(url)
    status = "passed" if driver.title == expected_title else "failed"
    driver.execute_script("lambda-status={}".format(status))
    assert driver.title == expected_title, f"Page title mismatch. Expected: {expected_title}, Actual: {driver.title}"
    driver.quit()
