import os
import re
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.login_page import LoginPage

load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
BOARD_STORY_NAME = os.getenv("BOARD_STORY_NAME", "DEMO001 Demo_test1 Story JM")


def test_open_board_from_profile_menu(page: Page) -> None:
	login_page = LoginPage(page)

	login_page.navigate(BASE_URL)
	login_page.login(USERNAME, PASSWORD)
	assert login_page.is_login_successful()

	
	login_page.open_user_menu()
	page.get_by_role("link", name="Board", exact=True).click()


	page.get_by_role("button", name=BOARD_STORY_NAME).click()

	
	page.get_by_role("button").filter(has_text=re.compile(r"^$")) .first.click()
