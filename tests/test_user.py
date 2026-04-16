import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"storage_state": "auth\\dev_scrum_state.json"}


def test_example(page: Page) -> None:
    page.goto("https://dev-scrum.crystalcodelabs.com/dashboard")
    users_link = page.get_by_role("link", name="Users")
    expect(users_link).to_be_visible()
    users_link.click()

    search_box = page.get_by_role("textbox", name="Search")
    expect(search_box).to_be_visible()
    search_box.click()
    search_box.fill("jasw")
    expect(search_box).to_have_value("jasw")

    page.get_by_role("button").nth(4).click()
    page.get_by_role("button", name="clear input").click()
    expect(search_box).to_have_value("")

    role_dropdown = page.get_by_role("button", name="Open").first
    expect(role_dropdown).to_be_visible()
    role_dropdown.click()

    employee_option = page.get_by_role("option", name="Employee")
    expect(employee_option).to_be_visible()
    employee_option.click()

    page.get_by_role("button").nth(4).click()
    expect(search_box).to_be_visible()

