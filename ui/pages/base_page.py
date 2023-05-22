from selene.support.shared import browser
from selene import have, command


class BasePage:
    def __init__(self):
        return

    def open(self, url):
        browser.open(url)

        return self

    def set_cookie(self, token):
        browser.driver.add_cookie({"name": "token", "value": token})
