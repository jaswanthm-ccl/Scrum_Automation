"""
Test Data Module
Contains test data and constants used across tests
"""
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


class TestData:
    """Test data constants and methods"""
    
    # Valid credentials - update with actual credentials
    VALID_USERNAME = "test_user"
    VALID_PASSWORD = "test_password123"
    
    # Invalid credentials
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "wrong_password"
    
    # Task data
    TASK_TITLE = "Test Task - " + str(datetime.now().timestamp())
    TASK_DESCRIPTION = "This is a test task description"
    TASK_PRIORITY = "High"
    TASK_ASSIGNEE = "John Doe"
    
    # Leave management data
    LEAVE_TYPE = "Sick Leave"
    START_DATE = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    END_DATE = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    LEAVE_REASON = "Need to attend to personal matters"
    
    # Client dependency data
    CLIENT_NAME = "Client " + fake.company()
    DEPENDENCY_DESCRIPTION = "Database connection and API integration required"
    DEPENDENCY_PRIORITY = "High"
    
    @staticmethod
    def generate_unique_task_title():
        """Generate a unique task title"""
        return f"Task - {fake.word()} - {datetime.now().timestamp()}"
    
    @staticmethod
    def generate_unique_email():
        """Generate a unique email address"""
        return fake.email()
    
    @staticmethod
    def generate_unique_username():
        """Generate a unique username"""
        return f"user_{fake.uuid4()[:8]}"
    
    @staticmethod
    def generate_random_password():
        """Generate a random password"""
        return fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    @staticmethod
    def get_future_date(days=5):
        """Get a date in the future"""
        return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    
    @staticmethod
    def get_past_date(days=5):
        """Get a date in the past"""
        return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    
    @staticmethod
    def generate_test_data_dict():
        """Generate a complete test data dictionary"""
        return {
            "username": TestData.generate_unique_username(),
            "email": TestData.generate_unique_email(),
            "password": TestData.generate_random_password(),
            "task_title": TestData.generate_unique_task_title(),
            "task_description": fake.text(max_nb_chars=100),
            "priority": fake.random_element(["Low", "Medium", "High", "Critical"]),
            "assignee": fake.name(),
        }
