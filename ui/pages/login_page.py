import allure
from selene.support.shared import browser

from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = browser.element("#username")
    PASSWORD = browser.element("#password")
    LOGIN_BUTTON = browser.element("#doLogin")

    @allure.step("Ввод user_name")
    def fill_user_name(self, value):
        self.USER_NAME.type(value)
        return self

    @allure.step("Ввод пароля")
    def fill_password(self, value):
        self.PASSWORD.type(value)
        return self

    @allure.step("Логин")
    def login(self, name, password):
        self.fill_user_name(name)
        self.fill_password(password)
        self.LOGIN_BUTTON.click()
        return self
