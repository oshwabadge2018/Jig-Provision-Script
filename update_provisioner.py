#!/usr/bin/python
import os
import subprocess
import time

print "Checking for updates.. ",
command = "git pull"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
time.sleep(10)
if process.returncode==0:
  print "Success!"
else:
  print "Failure!"
  exit(-1)

