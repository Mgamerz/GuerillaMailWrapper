__author__ = 'mgamerz'
__version__ = '0.1'
import requests
import copy


class GuerrillaAPI:

    def __init__(self):
        self.GUERRILLA_URL = 'https://api.guerrillamail.com/ajax.php'
        self.PYTHON_AGENT = 'Mgamerz_iOS_Feasibility_Test_via_Python'
        self.IP_ADDRESS = '127.0.0.1'
        self.LANG = 'en'
        self.SESSION_COOKIE = None
        self.URL_PARAMS = {'f': 'placeholder', 'agent': self.PYTHON_AGENT, 'ip': self.IP_ADDRESS, 'lang': 'en'}

        #variables
        self.EMAIL = None
        self.EMAIL_ALIAS = None

    def get_email_address(self):
        self.URL_PARAMS['f'] = 'get_email_address'
        email = requests.get(self.GUERRILLA_URL, params=self.URL_PARAMS)
        self.SESSION_COOKIE = dict(PHPSESSID=email.cookies['PHPSESSID'])
        email_json = email.json()
        self.EMAIL = email_json['email_addr']
        self.EMAIL_ALIAS = email_json['alias']
        print('Got address:', self.EMAIL)
        return

    def get_email_list(self):
        if not self.SESSION_COOKIE:
            print("ERROR: You need to get the email address first to get a session token.")
        url_params = copy.deepcopy(self.URL_PARAMS)
        url_params['f'] = 'get_email_list'
        url_params['offset'] = '0'
        email_list = requests.get(self.GUERRILLA_URL, params=url_params, cookies=self.SESSION_COOKIE)
        print(email_list.json())
        return email_list.json()['list']

    def print_email(self, mail_item):
        mail_from = mail_item['mail_from']
        mail_subject = mail_item['mail_subject']
        mail_text = mail_item['mail_excerpt']
        print('From:', mail_from)
        print('Subject:', mail_subject)
        print(mail_text)
        print('\n----------------------------------------')
        return


    def fetch_mail(self):
        pass

'''api = GuerrillaAPI()
api.get_email_address()
emails = api.get_email_list()
for mail in emails:
    api.print_email(mail)

emails = get_email_list()
#print(emails)
for mail in emails:
    print_email(mail)'''