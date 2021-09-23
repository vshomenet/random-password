#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import time
import hmac, base64, struct, hashlib

class password:
 def __init__(self):
 
  def get_hotp_token(secret, intervals_no):
   key = base64.b32decode(secret, True)
   msg = struct.pack(">Q", intervals_no)
   h = hmac.new(key, msg, hashlib.sha1).digest()
   o = o = h[19] & 15
   h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
   return h
  def get_totp_token(secret):
   x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
   while len(x)!=6:
    x='0'+x
   return x

  secret = 'LSDJFHGVBDNCKFHD'
  while 1<2:
   old=int(get_totp_token(secret))
   time.sleep(1)
   if old != int(get_totp_token(secret)):
  #print(get_totp_token(secret))
    pas=str(get_totp_token(secret))
    user="manager"
    text = "bash -c \"echo -e '{pas}\\n{pas}' | passwd {user}\""
    subprocess.call(text.format(pas=pas,user=user), shell=True, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))



