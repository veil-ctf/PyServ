import requests
import random

class Ping:
    def __init__(self) -> None:
        self.list = ["https://1.1.1.1/", "https://ip.me/", "https://google.com/", "https://api.ipify.org/"]
    def test(self) -> bool:
        try:
            requests.get(random.choice(self.list), timeout=5)
            return True
        except Exception:
            return False
