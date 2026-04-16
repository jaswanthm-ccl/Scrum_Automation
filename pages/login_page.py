from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # ONLY locators here
        self.email_input = page.locator("input[name='email']").first
        self.password_input = page.locator("input[type='password']")
        self.login_button = page.locator("button[type='submit']:has-text('Sign in')").first

    def navigate(self, base_url):
        self.page.goto(f"{base_url}/login")
        self.page.wait_for_load_state("networkidle")

    
    def login(self, email: str, password: str):
       self.email_input.wait_for(state="visible")
       self.password_input.first.wait_for(state="visible")

       max_len = self.password_input.first.evaluate("el => el.maxLength")
       if isinstance(max_len, int) and max_len > 0 and len(password) > max_len:
           raise ValueError(
               f"Password length ({len(password)}) exceeds UI limit ({max_len}). "
               "The site truncates extra characters."
           )

       self.email_input.fill(email)
       self.password_input.first.fill(password)

       typed_email = self.email_input.input_value()
       typed_password = self.password_input.first.input_value()
       if typed_email != email:
           raise ValueError(
               f"Email input mismatch. Expected '{email}', but field has '{typed_email}'."
           )
       if typed_password != password:
           raise ValueError(
               f"Password input mismatch. Expected length {len(password)}, "
               f"but field has length {len(typed_password)}."
           )

       self.login_button.click()

    def is_login_successful(self):
        """
        Check if login is successful.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        try:
            self.page.wait_for_function(
                "() => !window.location.pathname.includes('/login')",
                timeout=10000,
            )
            return True
        except PlaywrightTimeoutError:
            return False

    def open_user_menu(self):
        """Click the post-login profile icon (CircleIcon) to open the user menu."""
        menu_container = self.page.locator(
            "[role='menu'], .MuiMenu-paper, .MuiPopover-paper, .MuiDrawer-paper, nav"
        ).first

       
        if menu_container.count() > 0 and menu_container.is_visible():
            return

        selectors = [
            "button:has(svg[data-testid='CircleIcon'])",
            "[role='button']:has(svg[data-testid='CircleIcon'])",
            "svg[data-testid='CircleIcon']",
            "svg[style*='cursor: pointer']",
        ]

        for selector in selectors:
            locator = self.page.locator(selector).first
            if locator.count() == 0:
                continue

            try:
                locator.wait_for(state="visible", timeout=5000)
                locator.click(timeout=5000, force=True)
                menu_container.wait_for(
                    state="visible", timeout=5000
                )
                return
            except PlaywrightTimeoutError:
                continue


        circle_icon = self.page.locator("svg[data-testid='CircleIcon']").first
        if circle_icon.count() > 0:
            circle_icon.evaluate(
                """
                el => {
                    const target = el.closest('button,[role="button"],svg') || el;
                    target.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
                }
                """
            )
            menu_container.wait_for(
                state="visible", timeout=5000
            )
            return

        raise RuntimeError("Could not click profile CircleIcon to open the user menu.")