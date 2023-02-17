from util.helper import Helper
from auth.login import LoginClass
class TestUtil:
    def test_is_user_present_correct_username(self):
        username = "tanuj"
        assert Helper.is_user_present(username)

    def test_is_user_present_incorrect_username(self):
        username = "notpresent"
        assert not Helper.is_user_present(username)

    def test_is_sorrect_password_positive_case(self):
        password = "tanuj"
        conf_password = "tanuj"
        assert Helper.is_correct_password(password=password,confirmed_password=conf_password)

    def test_password_length_possitive(self):
        password = "verylongpassword"
        assert Helper.check_password_length(password)

    def test_password_length_negative(self):
        password = "short"
        assert not Helper.check_password_length(password)

    def test_is_admin_possititve(self):
        role = "admin"
        assert Helper.is_admin(role)

    def test_is_admin_negative(self):
        role = "user"
        assert not Helper.is_admin(role)

    def test_is_website_blocked_possitive(self):
        assert not Helper.is_website_blocked("tanuj","www.amazon.com")


    
