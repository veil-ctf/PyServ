#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2;
  exit 1;
else
	echo "Installing via pip..";
	pip3 install . || python3 setup.py install;
	echo "PyServ should be installed now. Running small test..";
	python3 -c "from pyserv import login;iserv=login.IServ(\"username\", \"password\", \"https://google.com/\");print(\"\033[32mPyServ installed properly!\") if iserv.login() == False else print(\"\033[91mCould not install PyServ, please try again or open an issue on github.\")" || echo "Something broke, please open an issue on github.";
fi
