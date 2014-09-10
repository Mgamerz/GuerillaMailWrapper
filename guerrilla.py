__author__ = 'mgamerz'
__version__ = '0.1'
import requests
import copy


class GuerrillaAPI:

    def __init__(self):
        self.GUERRILLA_URL = 'https://api.guerrillamail.com/ajax.php'
        self.PYTHON_AGENT = 'PythonWrapperGM'
        self.IP_ADDRESS = '127.0.0.1'
        self.LANG = 'en'
        self.SESSION_COOKIE = None
        self.URL_PARAMS = {'f': 'placeholder', 'agent': self.PYTHON_AGENT, 'ip': self.IP_ADDRESS, 'lang': 'en'}

        #variables
        self.EMAIL = None
        self.EMAIL_ALIAS = None

    def get_email_address(self):
        self.URL_PARAMS['f'] = 'get_email_address'
        #self.SESSION_COOKIE = dict(PHPSESSID='8oiuab186urudli5gh32pkb8t7')
        #email = requests.get(self.GUERRILLA_URL, params=self.URL_PARAMS, cookies=self.SESSION_COOKIE)
        email = requests.get(self.GUERRILLA_URL, params=self.URL_PARAMS)
        self.SESSION_COOKIE = dict(PHPSESSID=email.cookies['PHPSESSID'])
        email_json = email.json()
        self.EMAIL = email_json['email_addr']
        self.EMAIL_ALIAS = email_json['alias']
        return

    def get_email_list(self):
        if not self.SESSION_COOKIE:
            print("ERROR: You need to get the email address first to get a session token.")
            return
        url_params = copy.deepcopy(self.URL_PARAMS)
        url_params['f'] = 'get_email_list'
        url_params['offset'] = '0'
        email_list = requests.get(self.GUERRILLA_URL, params=url_params, cookies=self.SESSION_COOKIE)
        return email_list.json()['list']

    @staticmethod
    def print_email(mail_item):
        mail_from = mail_item['mail_from']
        mail_subject = mail_item['mail_subject']
        mail_text = mail_item['mail_excerpt']
        if 'mail_body' in mail_item:
            mail_text = mail_item['mail_body']
        print('From:', mail_from)
        print('Subject:', mail_subject)
        print(mail_text)
        print('\n----------------------------------------')
        return

    def fetch_mail(self, mail_id):
        """
        Fetches the full information about an email.
        :param id: The ID of the email.
        :return: A json array containing the email, or None if it was not found.
        """
        if not self.SESSION_COOKIE:
            print("ERROR: You need to get the email address first to get a session token.")
            return
        url_params = copy.deepcopy(self.URL_PARAMS)
        url_params['f'] = 'fetch_email'
        url_params['email_id'] = mail_id
        email = requests.get(self.GUERRILLA_URL, params=url_params, cookies=self.SESSION_COOKIE)
        if not email:
            print('RETURNED FALSE!')
            return
        return email.json()
        #print(email.text)
        #return email_list.json()['list']

