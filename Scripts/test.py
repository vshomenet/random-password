#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import configparser

path='rpass/etc/rpass.conf'
config = configparser.ConfigParser()
config.sections()
config.read(path)

for user, secret in config.items('users'):
 print (user)
 print (secret)

