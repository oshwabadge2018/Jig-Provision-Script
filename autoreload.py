import os
import subprocess
import time

while True:
  command = "python ui.py"
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  time.sleep(2)
