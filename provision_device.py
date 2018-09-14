import time
import serial

ser = serial.Serial("/dev/ttyS0",115200)
ser.write("1+1\n")
print ser.readline()
time.sleep(10)

