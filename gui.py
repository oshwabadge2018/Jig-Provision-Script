#!/usr/bin/python
import thorpy
import subprocess


commit = subprocess.check_output(['git', 'show', '--oneline', '-s']).split(" ")[0]

application = thorpy.Application((320, 415), "Badge Programmer")


vfile = open('fwver.txt','r')
fwver = vfile.read()

fwver = thorpy.OneLineText.make("Firmware Version   :  %s" % (fwver)) 
swver = thorpy.OneLineText.make("Provisioner Version:  %s" % (commit)) 

def launch(command):
  command = "xterm -fn fixed -fullscreen -e %s" % command
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()

def getNewFW():
  launch("python get_latest_firmware.py")
  pass


def getNewProv():
  launch("python update_provisioner.py")
  pass

def programDev():
  launch("python program_device.py")
  pass

def provisionDev():
launch("./provision_device.py")
  pass

division = thorpy.Line.make(size=300, type_="horizontal") 
ProgramDevice = thorpy.make_button("Program Device",func = programDev)
ProgramDevice.set_size((280,100))
ProvisionDevice = thorpy.make_button("Provision Device",func = provisionDev)
ProvisionDevice.set_size((280,100))
UpdateFirmware = thorpy.make_button("Load Latest Firmware",func=getNewFW)
UpdateFirmware.set_size((280,70))
UpdateProvisioner = thorpy.make_button("Update Provisioner",func=getNewProv)
UpdateProvisioner.set_size((280,70))



background = thorpy.Background.make(
elements=[fwver,swver,division,ProgramDevice,ProvisionDevice,UpdateFirmware,UpdateProvisioner])
thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()
