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

class IServ():
    def __init__(
        self, 
        username: str,
        password: str,
        url: str
        ):
        """[summary]

        Args:
            username (str): IServ username
            password (str): IServ password
            url (str): IServ server url (can be \"https://schoolsite.*/iserv/app/login\" or \"https://schoolsite.*/\")
        """
        self.username = username
        # Bad solution but it will work for now
        self.url = url
        if not "/serv/app/login" in self.url:
            if "/iserv/app/login" in str(self.url):
                self.url = url
            else:
                try:
                    if url[-1] == "/":
                        self.url += "iserv/app/login"
                    elif url[-1] != "/":
                        self.url += "/iserv/app/login"
                except Exception as e:
                    print("Exception occured: "+str(e))
        self.password = password
        self.session = requests.Session()
    def login(
        self
        ):
        """[summary]

        Returns:
            True: If the request was successful
            False: If the request was not successful
        """
        login_req = self.session.post(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}, data={"_username": self.username, "_password": self.password})
        if "displayName" in login_req.text: return True
        else: return False