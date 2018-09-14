import time
import serial

ser = serial.Serial("/dev/ttyS0",115200,timeout=2)
ser.write("1+1\n")
print ser.readline()
print ser.readline()
time.sleep(10)

