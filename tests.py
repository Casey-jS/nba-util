import unittest
import db_util as db

class Tests(unittest.TestCase):

    

    def test_favorites(self):
        self.assertEquals(True, db.is_favorited('admin', 2544))
        self.assertEquals(False, db.is_favorited('admin', 67233))

    def test_search(self):
        self.assertEquals("LeBron James", db.get_search_results('bron')[0]['fullName'])

    def test_teams_get(self):
        self.assertEquals(30, len(db.get_teams()))

    def test_signup(self):
        res = db.new_user("", "")
        self.assertEquals(False, res['valid'])

    def test_usernames(self):
        ae = self.assertEquals
        ae(True, db.user_exists("admin"))
        ae(False, db.user_exists(""))

    def test_valid_combo(self):
        ae = self.assertEquals
        ae(True, db.validate_user("admin", "password"))
        ae(False, db.validate_user("", ""))
        ae(False, db.validate_user("", "password"))
        ae(False, db.validate_user("admin", "Password"))



if __name__ == '__main__':
    unittest.main()
