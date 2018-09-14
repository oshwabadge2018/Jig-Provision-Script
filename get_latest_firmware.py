#!/usr/bin/python
from github import Github,GithubException
import subprocess
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

token = open("GH-TOKEN", "r").read()
token = token.strip()
git = Github(token)

org = git.get_organization('oshwabadge2018')
repo = org.get_repo('ohs2018-badge-firmware')

try:
  r = repo.get_latest_release()
  print "Latest release is: %s '%s'"%(r.tag_name,r.title)
  fwver = "%s %s"%(r.tag_name,r.title)

  download_url = None
  for a in r.get_assets():
    if a.name=='firmware.bin':
      download_url = a.browser_download_url

  if not download_url == None:
    print "Downloading firmware '%s'" %(download_url)

  if os.path.isfile("firmware.bin"):
    os.remove("firmware.bin")
  print bcolors.OKBLUE
  command = "wget %s" % download_url
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  vfile = open('fwver.txt','w+')
  vfile.write(fwver)
  vfile.close()
  print bcolors.ENDC
  if process.returncode==0:
    print bcolors.OKGREEN+"Success!"+bcolors.ENDC
    time.sleep(5)
  else:
    print bcolors.FAIL+"Success!"+bcolors.ENDC
    time.sleep(10)

except GithubException:
  print "Could not find a release"
