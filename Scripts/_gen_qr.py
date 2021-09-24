#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import configparser
import io
import qrcode

path='/etc/rpass.conf'
config = configparser.ConfigParser()
config.sections()
config.read(path)
  
def get_namehost():
 f_namehost=subprocess.Popen("/bin/hostname", shell=True, stdout=subprocess.PIPE)
 hostname=str(f_namehost.stdout.readline())[2:-3]
 return hostname

def get_user(username):
 secret=str(config['users'][username])
 return secret
 
username="user2"

qr = qrcode.QRCode()
qr.add_data("otpauth://totp/Rpass:"+username+"@"+get_namehost()+"?secret="+get_user(username)+"&issuer=Rpass")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
