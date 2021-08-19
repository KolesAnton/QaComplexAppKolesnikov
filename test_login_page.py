"""Store tests related to start page """

import pytest
from selenium import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginHelpers
from helpers.profile_page import ProfileHelpers


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(5)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        base_helper = BaseHelpers(driver)
        base_helper.find_by_contains_text(ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click()

    @pytest.fixture(scope="function")
    def register(self, driver):
        login_helper = LoginHelpers(driver)
        registered_user = login_helper.register_user(username=f"user{self.variety}",
                                                     email=f"mail{self.variety}@mail.com",
                                                     password=f"PwWWddd{self.variety}")
        login_helper.find_by_contains_text(ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click()
        return registered_user

    def test_invalid_login(self, driver):
        """
        - Open start page
        - Clear password and login fields
        - Fill fields with invalid values
        - Click on Sign In button
        - Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Login as user
        login_helper.login(username="Nameee33", password="Pwd676")

        # Verify error message
        login_helper.verify_error_message(text=LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message match to expected")

    def test_register(self, driver, logout):
        """
        - Open start page
        - Fill email, login and password fields
        - Click on Sign Up button
        - Verify register success
        """
        login_helper = LoginHelpers(driver)
        profile_helper = ProfileHelpers(driver)

        # Fill email, login and password fields
        username_value = login_helper.register_user(username=f"user{self.variety}",
                                                    email=f"mail{self.variety}@mail.com",
                                                    password=f"PwWWddd{self.variety}")[0]
        self.log.info("User was registered")

        # Verify register success
        profile_helper.verify_hello_message(username_value)
        self.log.info("Registration was success and verified")

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear password and login fields
        - Click on Sign In button
        - Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear password and login fields
        login_helper.login(username="", password="")

        # Verify error message
        login_helper.verify_error_message(text=LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message match to expected")

    def test_login(self, register, driver, logout):
        """
        - Open start page
        - Fill login and password
        - Click Sign In button
        - Verify the result
        """
        login_helper = LoginHelpers(driver)
        profile_helper = ProfileHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        username_value, _, password_value = register

        # Clear password and login fields
        login_helper.login(username=username_value, password=password_value)

        # Verify register success
        profile_helper.verify_hello_message(username_value)
        self.log.info("Registration was success and verified")

    # !!!!!!!!! Home work !!!!!!!!!
    # Test_1
    def test_registration_input_username_empty_email_empty_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input name > 3 characters
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Fill username, clear email and password fields
        username_value = login_helper.register_user(email="", username=f"user{self.variety}", password="")[0]
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Verify error message
        error_message_email = driver.find_element_by_xpath(LoginPageConstants.INVALID_EMAIL_REGISTER_MESSAGE_XPATH)
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.INVALID_PASSWORD_REGISTER_MESSAGE_XPATH)
        assert error_message_email.text == LoginPageConstants.INVALID_EMAIL_REGISTER_MESSAGE_TEXT
        assert error_message_password.text == LoginPageConstants.INVALID_PASSWORD_REGISTER_MESSAGE_TEXT
        self.log.info('Error message match to expected')

    # Test_2
    def test_registration_empty_username_input_email_empty_password(self, driver):
        """
        -Open start page
        -Clear Username,Email,Password fields
        -Input valid Email
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Fill email, clear username and password fields
        username_value = login_helper.register_user(email=f"mail{self.variety}@mail.com", username="", password="")[0]
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Verify error message
        error_message_user = driver.find_element_by_xpath(LoginPageConstants.INVALID_USERNAME_REGISTER_MESSAGE_XPATH)
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.INVALID_PASSWORD_REGISTER_MESSAGE_XPATH)
        assert error_message_user.text == LoginPageConstants.INVALID_USERNAME_REGISTER_MESSAGE_TEXT
        assert error_message_password.text == LoginPageConstants.INVALID_PASSWORD_REGISTER_MESSAGE_TEXT
        self.log.info('Error message match to expected')

    # Test_3
    def test_registration_empty_username_empty_email_input_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input password >= 12 characters
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Fill password, clear username and email fields
        username_value = login_helper.register_user(email="", username="", password=f"PPaswd{self.variety}")[0]
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Verify error message
        error_message_user = driver.find_element_by_xpath(LoginPageConstants.INVALID_USERNAME_REGISTER_MESSAGE_XPATH)
        error_message_email = driver.find_element_by_xpath(LoginPageConstants.INVALID_EMAIL_REGISTER_MESSAGE_XPATH)
        assert error_message_email.text == LoginPageConstants.INVALID_EMAIL_REGISTER_MESSAGE_TEXT
        assert error_message_user.text == LoginPageConstants.INVALID_USERNAME_REGISTER_MESSAGE_TEXT
        self.log.info('Error message match to expected')

    # Test_4
    def test_registration_input_username_input_email_empty_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input correct username and input correct email
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Fill username and email, clear password fields
        username_value = login_helper.register_user(username=f"user{self.variety}",
                                                    email=f"mail{self.variety}@mail.com", password="")[0]
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Verify error message
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.INVALID_PASSWORD_REGISTER_MESSAGE_XPATH)
        assert error_message_password.text == LoginPageConstants.INVALID_PASSWORD_REGISTER_MESSAGE_TEXT
        self.log.info('Error message match to expected')

    # Test_5
    def test_registration_input_username_empty_email_input_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input correct username and password
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Fill username and password, clear email fields
        username_value = login_helper.register_user(username=f"user{self.variety}", email="",
                                                    password=f"PPaswd{self.variety}")[0]
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Verify error message
        error_message_email = driver.find_element_by_xpath(LoginPageConstants.INVALID_EMAIL_REGISTER_MESSAGE_XPATH)
        assert error_message_email.text == LoginPageConstants.INVALID_EMAIL_REGISTER_MESSAGE_TEXT
        self.log.info('Error message match to expected')

    # Test_6
    def test_registration_empty_username_input_email_input_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input correct email and password
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Fill email and password, clear username fields
        username_value = login_helper.register_user(username="", email=f"mail{self.variety}@mail.com",
                                                    password=f"PPaswd{self.variety}")[0]
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Verify error message
        error_message_user = driver.find_element_by_xpath(LoginPageConstants.INVALID_USERNAME_REGISTER_MESSAGE_XPATH)
        assert error_message_user.text == LoginPageConstants.INVALID_USERNAME_REGISTER_MESSAGE_TEXT
        self.log.info('Error message match to expected')
