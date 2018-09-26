import time
import serial

#load list of names

#load list of use names
namesf = open("people","r")
usedf = open("assigned","r+")

namess = namesf.read()
useds = usedf.read()

names = namess.split("\n")
used =  useds.split("\n")

#find an available name

def getName(used,names):
	for name in names:
		if name in used:
			pass
		else:
			return name
	return None

name = getName(used,names)
if name==None:
	print "Out of names!"
	time.sleep(20)
	exit(1)

first,last = name.strip().split(" ")
print "Name: %s %s"%(first,last)

ser = serial.Serial("/dev/ttyS0",115200,timeout=2)

#first = "Joe"
#last = "Schmoe"
filew = "f = open(\"d_name.py\",\"w\")\r\nf.write(\"first='\")\r\nf.write(\"%s\")\r\nf.write(\"'\\n\")\r\nf.write(\"last='\")\r\nf.write(\"%s\")\r\nf.write(\"'\\n\")\r\nf.close()\r\n\r\n" % (first,last)
ser.write(filew)
ser.flush()
ser.write("import machine\r\n")
ser.write("machine.reset()\r\n")
usedf.write(name+"\n")
usedf.close()

