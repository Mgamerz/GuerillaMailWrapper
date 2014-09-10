__author__ = 'Mgamerz'

import unittest
from guerrilla import GuerrillaAPI
import re


class GuerrillaTests(unittest.TestCase):
    def test_get_email(self):
        apisession = GuerrillaAPI()
        apisession.get_email_address()
        self.assertTrue(re.match(r"[^@]+@[^@]+\.[^@]+", apisession.EMAIL))
        #test

    def test_original_inbox(self):
        apisession = GuerrillaAPI()
        self.assertEquals(None, apisession.get_email_list())
        apisession.get_email_address()
        emails = apisession.get_email_list()
        self.assertNotEquals(None, apisession.get_email_list())

    def test_fetch(self):
        apisession = GuerrillaAPI()
        self.assertEquals(None, apisession.get_email_list())
        apisession.get_email_address()
        emails = apisession.get_email_list()
        self.assertNotEquals(None, apisession.get_email_list())
        for mail in emails:
            message = apisession.fetch_mail(mail['mail_id'])
            GuerrillaAPI.print_email(message)

if __name__ == '__main__':
    unittest.main()
