class LoginPageConstants:
    """Store constants related to Login Page"""

    # Sign Up
    SIGN_UP_USERNAME_XPATH = "//input[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = "//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = "//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = "//button[contains(text(),'Sign up for OurApp')]"
    # SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"

    # Sign In
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = 'Sign In'
    #SIGN_IN_BUTTON_XPATH = ".//button[contains(text(), 'Sign In')]"

    # Messages
    INVALID_LOGIN_MESSAGE_TEXT = 'Invalid username / password'
    # INVALID_LOGIN_MESSAGE_XPATH = f"// div[contains(text(), '{INVALID_LOGIN_MESSAGE_TEXT}')]"
    INVALID_USERNAME_REGISTER_MESSAGE_TEXT = 'Username must be at least 3 characters.'
    INVALID_USERNAME_REGISTER_MESSAGE_XPATH = "//div[contains(text(),'Username must be at least 3 characters.')]"
    INVALID_EMAIL_REGISTER_MESSAGE_TEXT = 'You must provide a valid email address.'
    INVALID_EMAIL_REGISTER_MESSAGE_XPATH = "//div[contains(text(),'You must provide a valid email address.')]"
    INVALID_PASSWORD_REGISTER_MESSAGE_TEXT = 'Password must be at least 12 characters.'
    INVALID_PASSWORD_REGISTER_MESSAGE_XPATH = "//div[contains(text(),'Password must be at least 12 characters.')]"


