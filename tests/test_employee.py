import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {"storage_state": "auth/dev_scrum_state.json"}


def test_create_employee(page: Page) -> None:
    page.goto("https://dev-scrum.crystalcodelabs.com/dashboard")

    employees_link = page.get_by_role("link", name="Employees")
    expect(employees_link).to_be_visible()
    employees_link.click()

    add_new_button = page.get_by_role("button", name="Add New")
    expect(add_new_button).to_be_visible()
    add_new_button.click()

    first_name = page.locator('input[name="first_name"]')
    first_name.fill("demo")

    page.get_by_role("button", name="Open").first.click()
    page.get_by_role("option", name="India").click()

    page.get_by_role("button", name="Choose date").click()
    page.get_by_role("gridcell", name="15").click()

    contact_number = page.locator('input[name="contact_no"]')
    contact_number.fill("1234567890")

    page.locator(
        ".MuiAutocomplete-root.MuiAutocomplete-hasPopupIcon.css-lct14i > .MuiBox-root > .MuiFormControl-root > .MuiInputBase-root"
    ).click()
    page.get_by_role("option", name="Jaswanth M", exact=True).click()

    page.get_by_role("textbox").nth(5).fill("0123")

    page.locator('input[name="official_email"]').fill("demo@gmail.com")
    page.locator('input[name="personal_email"]').fill("demo@gmail.com")
    page.locator('input[name="password"]').fill("Demo@1234")

    page.get_by_role("combobox").nth(2).click()
    page.get_by_role("option", name="QA").click()

    page.locator('input[name="present_address"]').first.fill("demo address")
    page.get_by_role("checkbox", name="Same as Present Address").check()

    page.get_by_role("button", name="Create").click()

    for permission_name in [
        "client",
        "employee",
        "project",
        "task note",
        "project status",
        "task",
        "role",
        "dashboard",
        "kanban board",
        "admin",
        "task log",
        "task status",
        "tech stack",
        "user",
        "attendance",
        "country",
        "permission",
        "activity",
        "backlog",
        "announcement",
    ]:
        page.get_by_role("checkbox", name=permission_name, exact=True).check()