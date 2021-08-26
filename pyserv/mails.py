import requests
from bs4 import BeautifulSoup

class LoginErr(Exception):
    def __str__(self) -> str:
        return "Could not log in"

class Mails():
    def __init__(self, url, username, password, unseen_mail_url, mail_url) -> None:
        self.url = url
        self.username = username
        self.password = password
        self.unseen_mail_url = unseen_mail_url
        self.session = requests.Session()
        self.mail_url = mail_url

    def unseen_mails(self):
        login_req = self.session.post(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}, data={"_username": self.username, "_password": self.password})
        mail_req = self.session.get(self.unseen_mail_url).json()
        if "data" in mail_req:
            print(mail_req['data'][0]['unseen'])
        else:
            print("Error")

    def mail_content(self): #not finished
        login_req = self.session.post(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}, data={"_username": self.username, "_password": self.password})
        mail_content_req = self.session.get(self.unseen_mail_url)
        print(mail_content_req.text)
