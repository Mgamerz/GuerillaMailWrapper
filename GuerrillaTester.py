__author__ = 'Mgamerz'

import unittest
import guerrilla
import re


class GuerrillaTests(unittest.TestCase):
    def test_get_email(self):
        apisession = guerrilla.GuerrillaAPI()
        apisession.get_email_address()
        self.assertTrue(re.match(r"[^@]+@[^@]+\.[^@]+", apisession.EMAIL))
        #test

    def test_original_inbox(self):
        apisession = guerrilla.GuerrillaAPI()
        self.assertEquals(None, apisession.get_email_list())
        apisession.get_email_address()
        emails = apisession.get_email_list()
        self.assertNotEquals(None, apisession.get_email_list())

if __name__ == '__main__':
    unittest.main()
