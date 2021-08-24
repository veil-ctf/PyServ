from pyserv import login

x = login.IServ("username", "password", "url")
print(x.login())