__author__ = 'mgamerz'

import requests
import copy

GUERRILLA_URL = 'https://api.guerrillamail.com/ajax.php'
PYTHON_AGENT = 'Mgamerz_iOS_Feasibility_Test_via_Python'
IP_ADDRESS = '127.0.0.1'
LANG = 'en'
SESSION_COOKIE = None
URL_PARAMS = {'f': 'placeholder', 'agent': PYTHON_AGENT, 'ip': IP_ADDRESS, 'lang': 'en'}

#variables
EMAIL = None
EMAIL_ALIAS = None


def get_email_address():
    URL_PARAMS['f'] = 'get_email_address'
    email = requests.get(GUERRILLA_URL, params=URL_PARAMS)
    global SESSION_COOKIE, EMAIL, EMAIL_ALIAS
    SESSION_COOKIE = dict(PHPSESSID=email.cookies['PHPSESSID'])
    email_json = email.json()
    EMAIL = email_json['email_addr']
    EMAIL_ALIAS = email_json['alias']
    print('Got address:', EMAIL)
    return


def get_email_list():
    if not SESSION_COOKIE:
        print("ERROR: You need to get the email address first to get a session token.")
    url_params = copy.deepcopy(URL_PARAMS)
    url_params['f'] = 'get_email_list'
    url_params['offset'] = '0'
    email_list = requests.get(GUERRILLA_URL, params=url_params, cookies=SESSION_COOKIE)
    print(email_list.json())
    return email_list.json()['list']


def print_email(mail_item):
    mail_from = mail_item['mail_from']
    mail_subject = mail_item['mail_subject']
    mail_text = mail_item['mail_excerpt']
    print('From:', mail_from)
    print('Subject:', mail_subject)
    print(mail_text)
    print('\n----------------------------------------')
    return


def fetch_mail():
    pass


get_email_address()
emails = get_email_list()
#print(emails)
for mail in emails:
    print_email(mail)
