<kbd><h1 align="center">
<img width="500" src="https://i.imgur.com/UTXOx8r.png">
</h1>

<h4 align="center"> PyServ is a python library for logging into iserv, scraping tasks, downloading unread mails and doing other useful things
</h4>

## Content:

<ul>
<li><a href="#Installation">Installation</a>:
<ol>
    <li><a href="#Windows">Windows</a>
    <li><a href="#Linux">Linux</a>
</ol>
<li><a href="#Supporting">Supporting</a>
<ol>
    <li><a href="#Monero">Monero</a>
    <li><a href="#Bitcoin">Bitcoin</a>
    <li><a href="#Ethereum">Ethereum</a>
</ol>
<li><a href="#Usage">Usage</a>
<li><a href="#Contributing">Contributing</a>
<li><a href="#License">License</a>
</ul>

## Installation

Install PyServ using the `setup.py` file:

### Windows

<kbd>
.\setup.bat
</kbd>

### Linux

<kbd>
chmod +x setup.sh && ./setup.sh
</kbd>

## Supporting

If you like this project and want to support it, you can donate crypto:

###### Monero (XMR): ```86oxMS9ESAFNo7NsZBQCpDDPmCXnToLiHfBidUv2iKLD7E5vXBynhiGEfMi61ZqSaTiT8uz3duCoqFYbqMx9RTLs85PkwAG```

###### Bitcoin: ```bc1qew4k0ws8w50m26svsz2sq6lxg6rrv3hxsrpm92```

###### Ethereum: ```0xDEbDf9ea09fa7fA129ab63F018D58F7EacC55a69```


## Usage

```python
from pyserv import login

iserv = login.IServ("username", "password", "url") # Initialize IServ object "python.login.IServ"

iserv.login() # Returns True if login was successfull, False if not
```

For more info on the usage, please take a look at the `test.py` file, it contains some of PyServs features. We may or may not create a documentation in the future.

## Contributing

##### PyServ is still under development and needs as many helpers as we can get, you dont even need to be a programmer, you can also change things in this file ```(README.md)``` or do other useful things! if you wanna contribute, here are the 5 simple steps to do that:

1. Fork it
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License

PyServ uses the MIT License:

```
MIT License

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
SOFTWARE.
```
</kbd>
