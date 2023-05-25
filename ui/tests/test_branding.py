from ui.data.model import Contact
from ui.pages.branding_page import Branding
from ui.pages.front_page import FrontPage

contact = Contact(name="Sunny Valley", address="Scotts Valley, CA 95066", email="test@test.test", phone="+18314381500")


def test_edit_contact_info(open_browser_with_cookie):
    branding = Branding()
    front_page = FrontPage()
    branding.go_branding_page()
    branding.update_contact_info(contact)

    # THEN

    branding.close_alert()
    branding.go_front_page()
    front_page.check_contact_info(contact)
