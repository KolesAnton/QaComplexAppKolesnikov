"""Store tests related to start page """

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
import random
import string


class TestLoginPage(BaseTest):
    const_name = ''
    const_pass = ''
    const_email = ''

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\Admin\PycharmProjects\QaComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close()

    def test_empty_fields_login(self, driver):
        """
        -Open start page
        -Clear password and login fields
        -Click on Sign In button
        -Verify error message
        """
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        self.log.info("Fields were cleared")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        sign_in_button.click()
        self.log.info("Clicked on 'Sign In'")

        # Verify error message
        error_message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info('Error message match to expected')

    def test_invalid_login(self, driver):
        """
        -Open start page
        -Clear password and login fields
        -Fill fileds with invalid values
        -Click on Sign In button
        -Verify error message
        """
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("Name333")
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("Pwwewdd487")
        self.log.info("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        sign_in_button.click()
        self.log.info("Clicked on 'Sign In'")

        # Verify error message
        error_message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info('Error message match to expected')

    # Home work
    # Test_1
    def test_registration_input_username_empty_email_empty_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input name > 3 characters
        -Click on 'Sign up for OurApp'
        -Verify error message
        """
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input name > 3 characters
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        username.send_keys("UserOk")
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        self.log.info("Fields are filled with invalid values")

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")
        sleep(0.2)

        # Verify error message
        error_message_email = driver.find_element_by_xpath(
            "//div[contains(text(),'You must provide a valid email address.')]")
        error_message_password = driver.find_element_by_xpath(
            "//div[contains(text(),'Password must be at least 12 characters.')]")
        assert error_message_email.text == 'You must provide a valid email address.'
        assert error_message_password.text == 'Password must be at least 12 characters.'
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
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input valid Email
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()
        email.send_keys("UserOk@test.test")
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        self.log.info("Fields are filled with invalid values")

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")
        sleep(0.2)

        # Verify error message
        error_message_user = driver.find_element_by_xpath(
            "//div[contains(text(),'Username must be at least 3 characters.')]")
        error_message_password = driver.find_element_by_xpath(
            "//div[contains(text(),'Password must be at least 12 characters.')]")
        assert error_message_user.text == 'Username must be at least 3 characters.'
        assert error_message_password.text == 'Password must be at least 12 characters.'
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
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input password >= 12 characters
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        password.send_keys("123456789123")
        self.log.info("Fields are filled with invalid values")

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")
        sleep(0.2)

        # Verify error message
        error_message_user = driver.find_element_by_xpath(
            "//div[contains(text(),'Username must be at least 3 characters.')]")
        error_message_email = driver.find_element_by_xpath(
            "//div[contains(text(),'You must provide a valid email address.')]")
        assert error_message_email.text == 'You must provide a valid email address.'
        assert error_message_user.text == 'Username must be at least 3 characters.'
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
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input correct username and input correct email
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        username.send_keys("UserOk")
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()
        email.send_keys("UserOk@test.test")
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        self.log.info("Fields are filled with invalid values")

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")
        sleep(0.2)

        # Verify error message
        error_message_password = driver.find_element_by_xpath(
            "//div[contains(text(),'Password must be at least 12 characters.')]")
        assert error_message_password.text == 'Password must be at least 12 characters.'
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
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input correct username and password
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        username.send_keys("UserOk")
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        password.send_keys("123456789123")
        self.log.info("Fields are filled with invalid values")

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")
        sleep(0.2)

        # Verify error message
        error_message_email = driver.find_element_by_xpath(
            "//div[contains(text(),'You must provide a valid email address.')]")
        assert error_message_email.text == 'You must provide a valid email address.'
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
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input correct email and password
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()
        email.send_keys("UserOk@test.test")
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        password.send_keys("123456789123")
        self.log.info("Fields are filled with invalid values")

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")
        sleep(0.2)

        # Verify error message
        error_message_user = driver.find_element_by_xpath(
            "//div[contains(text(),'Username must be at least 3 characters.')]")
        assert error_message_user.text == 'Username must be at least 3 characters.'
        self.log.info('Error message match to expected')

    # # Test_7
    #     def test_registration_input_correct_username_email_password(self, driver):
    #         """
    #         -Open start page
    #         -Clear Username Email и Password fields
    #         -Input correct Username Email и Password
    #         -Click on 'Sign up for OurApp'
    #         -Verify
    #         """
    #         # Open start page
    #         driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    #         self.log.info("Open page")
    #
    #         # Clear required fields and Input password >= 12 characters
    #         username = driver.find_element_by_xpath("//input[@id='username-register']")
    #         username.clear()
    #         username.send_keys("UserOk17")
    #         email = driver.find_element_by_xpath("//input[@id='email-register']")
    #         email.clear()
    #         email.send_keys("UserOk17@test.test")
    #         password = driver.find_element_by_xpath("//input[@id='password-register']")
    #         password.clear()
    #         password.send_keys("1234567891231")
    #         self.log.info("Fields are filled ")
    #
    #         # Click on Sign up for OurApp button
    #         sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
    #         sleep(1)
    #         sign_up_for_ourapp.click()
    #         self.log.info("Clicked on 'Sign up for OurApp'")
    #
    #         # Open second page
    #         driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    #         self.log.info("Open second page")
    #
    #         # Verify registration
    #         text_message = driver.find_element_by_xpath(".//h2")
    #         assert text_message == driver.find_element_by_xpath(".//h2")
    #         self.log.info("registration good")

    # Test_8
    def test_registration_input_random_correct_username_email_password(self, driver):
        """
        -Open start page
        -Clear Username Email и Password fields
        -Input correct Username Email и Password
        -Click on 'Sign up for OurApp'
        -Verify
        -Log out
        """
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input correct Username Email и Password
        username = driver.find_element_by_xpath("//input[@id='username-register']")
        username.clear()
        username_random = ''.join(random.choices(string.ascii_lowercase, k=6))
        username.send_keys(username_random)
        email = driver.find_element_by_xpath("//input[@id='email-register']")
        email.clear()

        email.send_keys(f"{username_random}@test.test")
        password = driver.find_element_by_xpath("//input[@id='password-register']")
        password.clear()
        password_random = ''.join(random.choices(string.digits + string.ascii_lowercase, k=12))
        password.send_keys(password_random)
        self.log.info("Fields are filled ")
        TestLoginPage.const_name = username_random
        TestLoginPage.const_email = f"{username_random}@test.test"
        TestLoginPage.const_pass = password_random

        # Click on Sign up for OurApp button
        sign_up_for_ourapp = driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]")
        sleep(1)
        sign_up_for_ourapp.click()
        self.log.info("Clicked on 'Sign up for OurApp'")

        # Open second page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open second page")

        # Verify registration
        text_message = driver.find_element_by_xpath(".//h2")
        assert text_message == driver.find_element_by_xpath(".//h2")
        self.log.info("registration good")
        sleep(1)

        # Log Out
        log_but_button = driver.find_element_by_xpath("//button[contains(text(),'Sign Out')]")
        sleep(0.2)
        log_but_button.click()
        sleep(0.2)

    # Test_9
    def test_login(self, driver):
        """
        -Open start page
        -Clear password and login fields
        -Input correct Username Email и Password
        -Click on Sign In button
        -Verify
        """
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Clear required fields and Input correct Username Email и Password
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(TestLoginPage.const_name)
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(TestLoginPage.const_pass)
        self.log.info("Fields input coorrect data")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        sign_in_button.click()
        self.log.info("Clicked on 'Sign In'")

        # Verify login
        sleep(1)
        text_message = driver.find_element_by_xpath(".//h2")
        assert text_message == driver.find_element_by_xpath(".//h2")
        self.log.info("registration good")
