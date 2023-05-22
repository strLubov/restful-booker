from ui.data.guest import Guest
from ui.data.model import Contact
from ui.pages.base_page import BasePage
from selene.support.shared import browser
from selenium.webdriver import ActionChains
from selene.core.command import *  # noqa
#from ui import command as ui_command
from selenium.common.exceptions import NoSuchElementException
from selene import have, be
import allure

class FrontPage(BasePage):

    BOOK_THIS_ROOM = browser.element(".hotel-room-info .btn-outline-primary") #переписать селектор на первого потомка
    FIRST_NAME = browser.element(".room-firstname")
    LAST_NAME = browser.element(".room-lastname")
    EMAIL = browser.element(".room-email")
    PHONE = browser.element(".room-phone")
    BOOK_BUTTON = browser.element(".book-room")
    CALENDAR_MONTH = browser.element(".rbc-month-view")
    CHECKIN_DATE = browser.element(
        ".rbc-month-row:nth-of-type(3) .rbc-row-bg .rbc-day-bg:nth-of-type(2)")
    CHECKOUT_DATE = browser.element(
        ".rbc-month-row:nth-of-type(3) .rbc-row-bg .rbc-day-bg:nth-of-type(4)")
    CONFIRMATION_MODAL = browser.element(".confirmation-modal")
    CONFIRMATION_MODAL_BUTTON = browser.element(".room-booking-form .btn-outline-primary")
    CONTACT_NAME = browser.element(".col-sm-5>p:nth-child(1)")
    CONTACT_ADDRESS = browser.element(".col-sm-5>p:nth-child(2)")
    CONTACT_PHONE = browser.element(".col-sm-5>p:nth-child(3)")
    CONTACT_EMAIL = browser.element(".col-sm-5>p:nth-child(4)")



    def select_room(self):
        self.BOOK_THIS_ROOM.click()
        return self

    def fill_last_name(self, value):
        self.LAST_NAME.type(value)
        return self

    def fill_first_name(self, value):
        self.FIRST_NAME.type(value)
        return self

    def fill_email(self, value):
        self.EMAIL.type(value)
        return self

    def fill_phone(self, value):
        self.PHONE.type(value)
        return self

    def click_book(self):
        self.BOOK_BUTTON.click()
        return self

    def fill_guest(self, guest: Guest):
        self.fill_first_name(guest.first_name)
        self.fill_last_name(guest.last_name)
        self.fill_email(guest.email)
        self.fill_phone(guest.phone)

    def book(self):
        self.BOOK_BUTTON.click()

    def select_checkin_and_checkout_date(self):
        self.CHECKIN_DATE.perform(ui_command.drag_to(self.CHECKOUT_DATE))

    # def select_date(self):
    #     action = ActionChains(driver=browser.driver)
    #     action.click_and_hold(self.CHECKIN_DATE()).move_by_offset(xoffset=100, yoffset=100).release().perform()
    #
    # def should_confirmation_modal(self):
    #     # проверяем, что модальное окно появилось
    #     try:
    #         self.CONFIRMATION_MODAL.click()
    #     except NoSuchElementException:
    #         print("Modal window was not found")
    #         quit()
    #
    #     # закрываем модальное окно
    #     self.CONFIRMATION_MODAL_BUTTON.click()
    #
    #     # проверяем, что модальное окно было закрыто
    #     if self.CONFIRMATION_MODAL.is_displayed():
    #         print("Modal window was not closed")
    #     else:
    #         print("Modal window was successfully closed")

    @allure.step("Проверка контактной информации на главной странице")
    def check_contact_info(self, model: Contact):
        self.CONTACT_NAME.should(have.text(model.name))
        self.CONTACT_EMAIL.should(have.text(model.email))
        self.CONTACT_PHONE.should(have.text(model.phone))
        self.CONTACT_ADDRESS.should(have.text(model.address))
        return self





