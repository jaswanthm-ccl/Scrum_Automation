"""
Client Dependency Page - Page Object Model using Playwright
Contains all locators and methods for client dependency management
"""
from playwright.sync_api import Page


class ClientDependencyPage:
    """Page Object for Client Dependency functionality using Playwright"""
    
    # Locators
    DEPENDENCY_TITLE = "h1, .page-title, [data-testid='dependency-title']"
    ADD_DEPENDENCY_BUTTON = "button:has-text('Add'), button:has-text('New Dependency')"
    CLIENT_NAME_INPUT = "input[name='clientName'], input[placeholder*='Client']"
    DEPENDENCY_DESCRIPTION_INPUT = "textarea[name='description'], textarea[placeholder*='Description']"
    PRIORITY_SELECT = "select[name='priority'], [data-testid='priority']"
    SAVE_DEPENDENCY_BUTTON = "button:has-text('Save'), button:has-text('Add Dependency')"
    DEPENDENCIES_LIST = ".dependency-item, [data-testid='dependency']"
    EDIT_DEPENDENCY_BUTTON = "button:has-text('Edit')"
    DELETE_DEPENDENCY_BUTTON = "button:has-text('Delete')"
    
    def __init__(self, page: Page):
        """Initialize the ClientDependencyPage with Playwright page"""
        self.page = page
    
    def goto_dependencies(self, base_url: str = "https://scrum.crystalcodelabs.com"):
        """Navigate to client dependencies page"""
        self.page.goto(f"{base_url}/client-dependencies")
    
    def is_dependency_page_visible(self) -> bool:
        """Check if client dependency page is displayed"""
        try:
            title = self.page.query_selector(self.DEPENDENCY_TITLE)
            return title is not None
        except:
            return False
    
    def click_add_dependency(self):
        """Click the add dependency button"""
        self.page.click(self.ADD_DEPENDENCY_BUTTON)
        self.page.wait_for_load_state("networkidle")
    
    def enter_client_name(self, client_name: str):
        """Enter client name"""
        self.page.fill(self.CLIENT_NAME_INPUT, client_name)
    
    def enter_dependency_description(self, description: str):
        """Enter dependency description"""
        self.page.fill(self.DEPENDENCY_DESCRIPTION_INPUT, description)
    
    def set_priority(self, priority: str):
        """Set dependency priority"""
        self.page.select_option(self.PRIORITY_SELECT, priority)
    
    def save_dependency(self):
        """Save the dependency"""
        self.page.click(self.SAVE_DEPENDENCY_BUTTON)
        self.page.wait_for_load_state("networkidle")
    
    def add_dependency(self, client_name: str, description: str, priority: str):
        """Add a new client dependency"""
        self.click_add_dependency()
        self.enter_client_name(client_name)
        self.enter_dependency_description(description)
        self.set_priority(priority)
        self.save_dependency()
    
    def get_dependencies_count(self) -> int:
        """Get the number of dependencies"""
        dependencies = self.page.query_selector_all(self.DEPENDENCIES_LIST)
        return len(dependencies)
    
    def edit_dependency(self, index: int = 0):
        """Edit a dependency"""
        buttons = self.page.query_selector_all(self.EDIT_DEPENDENCY_BUTTON)
        if len(buttons) > index:
            buttons[index].click()
    
    def delete_dependency(self, index: int = 0):
        """Delete a dependency"""
        buttons = self.page.query_selector_all(self.DELETE_DEPENDENCY_BUTTON)
        if len(buttons) > index:
            buttons[index].click()
