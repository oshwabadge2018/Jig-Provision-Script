import thorpy
import subprocess

commit = subprocess.check_output(['git', 'show', '--oneline', '-s']).split(" ")[0]

application = thorpy.Application((320, 415), "Badge Programmer")


vfile = open('fwver.txt','r')
fwver = vfile.read()

fwver = thorpy.OneLineText.make("Firmware Version   :  %s" % (fwver)) 
swver = thorpy.OneLineText.make("Provisioner Version:  %s" % (commit)) 

division = thorpy.Line.make(size=300, type_="horizontal") 
ProgramDevice = thorpy.Clickable.make("Program Device",size = (280,100))
ProvisionDevice = thorpy.Clickable.make("Provision Device",size = (280,100))
UpdateFirmware = thorpy.Clickable.make("Load Latest Firmware",size = (280,70))
UpdateProvisioner = thorpy.Clickable.make("Update Provisioner",size = (280,70))



background = thorpy.Background.make(
elements=[fwver,swver,division,ProgramDevice,ProvisionDevice,UpdateFirmware,UpdateProvisioner])
thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()
