from selene.support.shared import browser


class BasePage:
    def __init__(self):
        return

    def open(self, url):
        browser.open(url)
        return self

    def set_cookie(self, token):
        browser.driver.add_cookie({"name": "token", "value": token})
        return self
