"""MIT License
Copyright (c) 2021 veil-ctf
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

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
