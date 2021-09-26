#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import time
import string
import random
import configparser
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

class qrcode:
 # Generate QR-code for user
 def get_qr(self,username):
  import io
  import qrcode
  path='/etc/rpass.conf'
  config = configparser.ConfigParser()
  config.sections()
  config.read(path)
 
  def get_user(username):
   secret=str(config['users'][username])
   return secret
  
  def get_namehost():
   f_namehost=subprocess.Popen("/bin/hostname", shell=True, stdout=subprocess.PIPE)
   hostname=str(f_namehost.stdout.readline())[2:-3]
   return hostname
   
  username=str(username)
  qr = qrcode.QRCode()
  qr.add_data("otpauth://totp/Rpass:"+username+"@"+get_namehost()+"?secret="+get_user(username)+"&issuer=Rpass")
  f = io.StringIO()
  qr.print_ascii(out=f)
  f.seek(0)
  print(f.read())

class users:
 #Check user in system
 def check_user(self, username):
  with open('/etc/passwd', 'r') as file:
   for line in file:
    user=line.rstrip().split(':')
    if username==user[0]:
     a=True
     break
    else:
     a=False
   file.close()
   return a
 #Add new user in config file
 def add_config(self, username, secret):
  path='/etc/rpass.conf'
  config = configparser.ConfigParser()
  config.sections()
  config.read(path)
  with open(path, 'w') as f:
   config.set('users', username , secret)
   config.write(f)
 #Remove user from config file
 def del_config(self, username):
  path='/etc/rpass.conf'
  config = configparser.ConfigParser()
  config.sections()
  config.read(path)
  with open(path, 'w') as f:
   config.remove_option('users', username)
   config.write(f)
