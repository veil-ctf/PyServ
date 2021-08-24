from pyserv import login, proxy

proxy = proxy.Proxy("1.1.1.1:80")
formatted_proxy = proxy.format()
print(formatted_proxy)

myiserv = login.IServ("username", "password", "url")

login_myiserv = myiserv.login()

print(login_myiserv)