#!/usr/bin/python
import os
import subprocess

print "Checking for updates.. ",
command = "git pull"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode==0:
  print "Success!"
else:
  print "Failure!"
  exit(-1)
command = "chmod a+x *.py"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()

