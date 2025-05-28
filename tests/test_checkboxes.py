import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("expected_state", [True])
def test_checkbox(driver, expected_state):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    for checkbox in checkboxes:
        if checkbox.is_selected() != expected_state:  # Only click if state is incorrect
            checkbox.click()

    for checkbox in checkboxes:
        assert checkbox.is_selected() == expected_state, f"Checkbox state mismatch: Expected {expected_state}"

    status = "passed" if all(checkbox.is_selected() == expected_state for checkbox in checkboxes) else "failed"
    driver.execute_script(f"lambda-status={status}")
    driver.quit()
