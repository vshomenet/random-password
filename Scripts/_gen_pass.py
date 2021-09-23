#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import string
import random
import hmac, base64, struct, hashlib

class password:
#Generate totp password
 def gen_pass(self, secret):
  def get_hotp_token(secret, intervals_no):
   key = base64.b32decode(secret, True)
   msg = struct.pack(">Q", intervals_no)
   h = hmac.new(key, msg, hashlib.sha1).digest()
   o = o = h[19] & 15
   h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
   return h
  x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
  while len(x)!=6:
   x='0'+x
  return x
 
# Generate secret string
 def gen_secret(self):
  def gen_string(size=10, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))
  secret=base64.b32encode(bytearray(gen_string(), 'ascii')).decode('utf-8')
  return secret
