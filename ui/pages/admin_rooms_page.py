import time

import allure
from selene import have, be
from selene.support.shared import browser

from ui.data.model import Room
from ui.pages.base_page import BasePage


class AdminRooms(BasePage):
    CREATE_BUTTON = browser.element("#createRoom")
    ROOM_NAME = browser.element("#roomName")
    TYPE = browser.element("#type")
    ACCESSIBLE = browser.element("#accessible")
    PRICE = browser.element("#roomPrice")
    WIFI = browser.element("#wifiCheckbox")
    REFRESH = browser.element("#refreshCheckbox")
    TV = browser.element("#tvCheckbox")
    SAFE = browser.element("#safeCheckbox")
    RADIO = browser.element("#radioCheckbox")
    VIEWS = browser.element("#viewsCheckbox")
    OPTIONS = browser.all(".form-check-input")
    ROOMS_LIST = browser.element(".container")
    REPORT = browser.element("#reportLink")
    BRANDING = browser.element("#brandingLink")
    EDIT_BUTTON = browser.element(".btn-outline-primary")
    IMAGE = browser.element("#image")
    DESCRIPTION = browser.element("#description")
    UPDATE_BUTTON = browser.element("#update")
    ROOM_DETAILS_NAME = browser.element(".col-sm-10")
    ROOM_DETAILS = browser.element(".room-details>.row:nth-child(3)>.col-sm-6:nth-child(1)")

    def fill_room_name(self, value):
        self.ROOM_NAME.clear().type(value).press_enter()
        return self

    def select_room_type(self, value):
        self.TYPE.type(value)
        return self

    def select_accessible(self, value):
        self.ACCESSIBLE.type(value)
        return self

    def fill_price(self, value):
        self.PRICE.clear().type(value).press_enter()
        return self

    def select_options(self, value):
        self.OPTIONS.element_by(have.exact_text(value)).click()
        return self

    def select_wifi(self):
        self.WIFI.click()
        return self

    def select_safe(self):
        self.SAFE.click()
        return self

    def select_views(self):
        self.VIEWS.click()
        return self

    def select_tv(self):
        self.TV.click()
        return self

    def create(self):
        self.CREATE_BUTTON.click()
        return self

    @allure.step("Создание комнаты")
    def create_room(self, room: Room):
        self.fill_room_name(room.name)
        self.select_room_type(room.type)
        self.fill_price(room.price)
        self.select_wifi()
        self.select_views()
        self.select_safe()
        self.select_accessible(room.accessible)
        self.create()

        return self

    @allure.step("Проверка, что открыта админка")
    def should_have_elements(self):
        self.ROOMS_LIST.matching(be.visible)
        self.BRANDING.matching(be.visible)
        self.REPORT.matching(be.visible)
        return

    @allure.step("Открытие страницы созданной комнаты")
    def open_created_room(self, name):
        browser.element(f'#roomName{name}').click()
        return self

    @allure.step("Проверка названия комнаты")
    def check_room_name(self, value):
        self.ROOM_DETAILS_NAME.should(have.text(f"Room: {value}"))
        return self

    @allure.step("Проверка стоимости комнаты")
    def check_room_price(self, price):
        self.ROOM_DETAILS.should(have.text(f"Room price: {price}"))
        return self

    def fill_description(self):
        self.DESCRIPTION.clear().type("The best test room")

    def update(self):
        self.UPDATE_BUTTON.click()

    @allure.step("Редактирование комнаты")
    def edit(self, room: Room):
        self.EDIT_BUTTON.click()
        self.fill_room_name(room.name)
        time.sleep(2)
        self.select_room_type(room.type)
        self.fill_price(room.price)
        self.fill_description()
        self.select_views()
        self.select_tv()
        self.UPDATE_BUTTON.click()
