import requests

class LoginErr(Exception):
    def __str__(self) -> str:
        return "Could not log in"

class Mails():
    def __init__(self, url, username, password, mail_url) -> None:
        self.url = url
        self.username = username
        self.password = password
        self.mail_url = mail_url
        self.session = requests.Session()

    def unseen_mails(self): #Not finished
        login_req = self.session.post(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}, data={"_username": self.username, "_password": self.password})
        mail_req = self.session.get(self.mail_url)
        if "data" in mail_req.text:
            print(mail_req.text)
        else:
            print("Error")