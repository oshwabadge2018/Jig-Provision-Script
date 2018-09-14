#!/usr/bin/python
import os
import subprocess
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print "Checking for updates.. ",
command = "git pull"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode==0:
  print bcolors.OKGREEN+"Success!"+bcolors.ENDC
  time.sleep(5)
else:
  print bcolors.FAIL+"Failure!"+bcolors.ENDC
  time.sleep(10)
