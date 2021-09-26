#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import os
import time
import configparser
from threading import Thread
from _class import password

class start:
 def __init__(self):

  path='/etc/rpass.conf'
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
     install_pass(user,new)
     
  while True:
   pas=password()
   for user, secret in config.items('users'):
    th = Thread(target=create_pass, args=(user, secret))
    th.start()
