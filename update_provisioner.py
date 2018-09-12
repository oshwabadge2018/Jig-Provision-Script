import os
import subprocess

print "Checking for updates.. ",
command = "git pull origin master"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode==0:
  print "Success!"
else:
  print "Failure!"
