#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import configparser
from _rpass import start
from _class import qrcode, users, password

# This is function only for pyinstaller
def resource_path(relative_path):
 if getattr(sys, 'frozen', False):
  base_path = sys._MEIPASS
 else:
  base_path = os.getcwd()
 return os.path.join(base_path, relative_path)
#-----------------------------------

usr=users()
pas=password()
qr=qrcode()

if __name__ == '__main__':
 parser = argparse.ArgumentParser(description='"Random Pass" Generate random password for users in system Linux on based "Google Authenticator"')
 parser.add_argument("-a", metavar='<username>', dest="add_user", type=str, help='Add user in system, create password and generate QR-code')
 parser.add_argument("-c", metavar='<username>', dest="pass_user", type=str, help='Create new password for user and generate QR-code')
 parser.add_argument("-d", metavar='<username>', dest="del_user", type=str, help='Delete user from system')
 parser.add_argument("-s", metavar='<command>', dest="start", type=str, help='"rpas -s start" Start main service')
 args = parser.parse_args()
 if args.add_user != None:
  username=args.add_user
  if usr.check_user(username)==False:
   secret=pas.gen_secret()
   usr.add_config(username,secret)
   qr.get_qr(username)
   print("User "+username+" successfully created in the system\nPlease scan the QR-code")
  else:
   print("The user is already in the system. To create or change a password for a user, run the\nrpass -c "+username)
 if args.pass_user != None:
  username=args.pass_user
  if usr.check_user(username)==True:
   secret=pas.gen_secret()
   usr.add_config(username,secret)
   qr.get_qr(username)
   print("Password encryption algorithm changed for user "+username+"\nPlease scan the new QR-code")
  else:
   print("The user not found in the system. To add user in system, run the\nrpass -a "+username)
 if args.del_user != None:
  username=args.del_user
  if usr.check_user(username)==True:
   usr.del_config(username)
   print ("User "+username+" removed successfully from the system")
  else:
   print("The user not found in the system. To add user in system, run the\nrpass -a "+username)
 if (args.start != None and args.start=="start"):
  start()

