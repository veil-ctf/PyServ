from pyserv import proxy

myproxy = proxy.Proxy("1.1.1.1:80")

print(myproxy.format())