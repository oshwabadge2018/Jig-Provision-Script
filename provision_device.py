import time
import serial

ser = serial.Serial("/dev/ttyS0",115200,timeout=2)

first = "Joe"
last = "Schmoe"
filew = "f = open(\"d_name.py\",\"w\")\r\nf.write(\"first='\")\r\nf.write(\"%s\")\r\nf.write(\"'\\n\")\r\nf.write(\"last='\")\r\nf.write(\"%s\")\r\nf.write(\"'\\n\")\r\nf.close()\r\n\r\n" % (first,last)
ser.write(filew)
ser.flush()
ser.write("import machine\r\n")
ser.write("machine.reset()\r\n")
