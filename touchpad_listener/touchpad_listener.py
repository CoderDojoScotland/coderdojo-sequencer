
import serial
import sonic
import glob


sonic_pi = sonic.SonicPi()
connection = serial.Serial(glob.glob('/dev/tty.usbmodem*')[0], 115200)

while True:
    line = connection.readline()
    command, argument = line.strip().split(' ', 1)
    if command == 'pad':
        number = int(argument)
        sonic_pi.run('cue :pad, number: {}'.format(number))

