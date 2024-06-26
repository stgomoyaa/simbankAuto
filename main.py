# test
import serial

ser = serial.Serial("COM5", baudrate=115200, timeout=1)
while True:
   data = ser.readline()
   print(data)