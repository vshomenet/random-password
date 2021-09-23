#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from _gen_pass import password
from _pass import start

# This is function only for pyinstaller
def resource_path(relative_path):
 if getattr(sys, 'frozen', False):
  base_path = sys._MEIPASS
 else:
  base_path = os.getcwd()
 return os.path.join(base_path, relative_path)
#-----------------------------------

if __name__ == '__main__':
 parser = argparse.ArgumentParser(description='random pass')
 parser.add_argument("-a", metavar='<user>', dest="sys_user", type=str, help='Add user in system and create password')
 parser.add_argument("-n", metavar='<user>', dest="user", type=str, help='Create password for user')
 parser.add_argument("-q", metavar='<user>', dest="qr_user", type=str, help='Generate QR-code for user')
 parser.add_argument("-c", metavar='<user>', dest="ch_user", type=str, help='Generate new hash for user')
 parser.add_argument("-d", metavar='<user>', dest="del_user", type=str, help='Delete user')
 parser.add_argument("-s", metavar='<command>', dest="start", type=str, help='"rpas -s start" Start main service')
 args = parser.parse_args()
 if args.sys_user != None:
  print ("Add user in system and create password")
 if args.user != None:
  print ("Create password for user")
 if args.qr_user != None:
  print ("Generate QR-code for user")
 if args.ch_user != None:
  print ("Generate new hash for user")
 if args.del_user != None:
  print ("Delete user")
 if (args.start != None and args.start=="start"):
  start()

