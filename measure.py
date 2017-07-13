import timeit
import sys
import serial
from timeit import Timer

ser = serial.Serial('/dev/ttyACM1', 38400)
length = int(sys.argv[1])
char = 'a' * length


def io():
    ser.write(char)
    ser.read(length)


t = Timer(lambda: io())
print(t.timeit(number=100) / 100)
