import os
import re
from datetime import datetime

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL", "https://dev-scrum.crystalcodelabs.com")
BOARD_STORY_NAME = os.getenv("BOARD_STORY_NAME", "DEMO001 Demo_test1 Story JM")
ASSIGNEE_NAME = os.getenv("ASSIGNEE_NAME", "Jaswanth M")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
	return {
		**browser_context_args,
		"storage_state": "auth/dev_scrum_state.json",
	}


def test_create_task_using_saved_session(page: Page) -> None:
	task_name = f"demo-{datetime.now().strftime('%H%M%S')}"

	page.goto(f"{BASE_URL}/dashboard")

	page.get_by_role("link", name="Board", exact=True).click()
	page.get_by_role("button", name=BOARD_STORY_NAME).click()

	# In this board view an icon-only action opens the task actions panel.
	page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()

	page.get_by_role("button", name=re.compile(r"\+?\s*Add Task", re.IGNORECASE)).click()

	# Project/department selector
	page.locator(".MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-6.css-iol86l").first.click()
	page.get_by_role("option", name="Testing").click()

	page.locator("input[name='task_name']").fill(task_name)
	page.locator(".ql-editor").fill("demo")
	page.locator("input[name='estimated_time']").fill("5")
	page.locator("input[name='qa_estimated_time']").fill("5")

	page.get_by_role("combobox").nth(5).click()
	page.get_by_role("option", name=ASSIGNEE_NAME).click()

	page.get_by_role("button", name="Create").click()

	page.goto(f"{BASE_URL}/kanban-board")
	page.get_by_role("textbox", name="Search").fill(task_name)
	page.get_by_role("textbox", name="Search").press("Enter")

	expect(page.get_by_text(task_name).first).to_be_visible(timeout=10000)
