#!/usr/bin/python
import os
import subprocess
import time

print "Checking for updates.. ",
command = "git pull"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode==0:
  print "Success!"
else:
  print "Failure!"

time.sleep(10)
