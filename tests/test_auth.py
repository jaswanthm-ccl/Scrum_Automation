import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

# On Windows, USERNAME is a built-in env var (e.g. jaswa).
# override=True ensures .env credentials are used for tests.
load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PAUSE_AFTER_LOGIN = os.getenv("PAUSE_AFTER_LOGIN", "true").lower() == "true"


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_login_successful()
    

    