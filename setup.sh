#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2;
  exit 1;
else
	echo "Installing via pip..";
	pip3 install . || python3 setup.py install;
fi
