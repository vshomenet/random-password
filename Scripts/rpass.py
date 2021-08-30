#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import time
import configparser # For read config file
import argparse     # For parse input argument almaz -h

#from cmd import Cmd
#from multiprocessing import Process, freeze_support
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
 parser.add_argument("-s", dest="command", type=str, help='Support command config,....')
 args = parser.parse_args()








