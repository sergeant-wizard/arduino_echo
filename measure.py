import timeit
import sys
import serial
from timeit import Timer
from time import sleep

ser = serial.Serial('/dev/ttyS4', 38400)
# ser = serial.Serial('COM5', 38400)
sleep(3.0)
length = int(sys.argv[1])
char = 'a' * length

def io():
    ser.write(char)
    ser.read(length)


t = Timer(lambda: io())
print(t.timeit(number=100) / 100)
print('done')
