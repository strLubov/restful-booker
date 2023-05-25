import allure
from selene.support.shared import browser

from ui.data.model import Contact
from ui.pages.base_page import BasePage


class Branding(BasePage):
    UPDATE = browser.element("#updateBranding")
    NAME = browser.element("#contactName")
    ADDRESS = browser.element("#contactAddress")
    PHONE = browser.element("#contactPhone")
    EMAIL = browser.element("#contactEmail")
    ALERT = browser.element(".col-12")
    CLOSE_ALERT = browser.element(".col-12 .btn-outline-primary")
    LINK_FRONT_PAGE = browser.element("#frontPageLink")
    LINK_BRANDING_PAGE = browser.element("#brandingLink")

    def fill_name(self, value):
        self.NAME.clear().type(value).press_enter()
        return self

    def fill_address(self, value):
        self.ADDRESS.clear().type(value).press_enter()
        return self

    def fill_phone(self, value):
        self.PHONE.clear().type(value).press_enter()
        return self

    def fill_email(self, value):
        self.EMAIL.clear().type(value).press_enter()
        return self

    def update(self):
        self.UPDATE.click()
        return self

    @allure.step("Заполнение контактной информции об отеле в админке")
    def update_contact_info(self, model: Contact):
        self.fill_name(model.name)
        self.fill_address(model.address)
        self.fill_phone(model.phone)
        self.fill_email(model.email)
        self.update()

    @allure.step("Закрытие окна подтверждения")
    def close_alert(self):
        self.CLOSE_ALERT.click()
        return self

    @allure.step("Переход на главную страницу из админки")
    def go_front_page(self):
        self.LINK_FRONT_PAGE.click()
        return self

    @allure.step("Переход на страницу брендинга")
    def go_branding_page(self):
        self.LINK_BRANDING_PAGE.click()
        return self
