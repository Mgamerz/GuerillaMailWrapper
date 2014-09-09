__author__ = 'Mgamerz'

import unittest
import guerrilla
import re


class GuerrillaTests(unittest.TestCase):
    def test_get_email(self):
        apisession = guerilla.GuerrillaAPI()
        apisession.get_email_address()
        self.assertTrue(re.match(r"[^@]+@[^@]+\.[^@]+", apisession.EMAIL))
        #test


if __name__ == '__main__':
    unittest.main()
