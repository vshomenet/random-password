#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import time
import configparser
from threading import Thread
from _gen_pass import password

path='rpass/etc/rpass.conf'
config = configparser.ConfigParser()
config.sections()
config.read(path)

def install_pass(user,pas):
 text = "bash -c \"echo -e '{pas}\\n{pas}' | passwd {user}\""
 subprocess.call(text.format(pas=pas,user=user), shell=True, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

def create_pass(user, secret):
 while True:
  old=int(pas.gen_pass(secret))
  time.sleep(1)
  new=int(pas.gen_pass(secret))
  if old != new:
   print(user, pas.gen_pass(secret))

pas=password()
for user, secret in config.items('users'):
 th = Thread(target=create_pass, args=(user, secret))
 th.start()
