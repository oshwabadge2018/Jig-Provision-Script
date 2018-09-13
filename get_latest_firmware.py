from github import Github,GithubException
import subprocess
import os

token = open("GH-TOKEN", "r").read()
token = token.strip()
print token
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
  command = "wget %s" % download_url
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  vfile = open('fwver.txt','w+')
  vfile.write(fwver)
  vfile.close()
  if process.returncode==0:
    print "Success!"
  else:
    print "Failure!"

except GithubException:
  print "Could not find a release"
