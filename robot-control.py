import msvcrt
import serial
ser = serial.Serial('COM38', 9600)
while 1:
    # Poll keyboard
    if msvcrt.kbhit():
        key = msvcrt.getch()
    if key == b'f':
        ser.write(str.encode('C21FE'))
    elif key == b's':
        ser.write(str.encode('C21SE'))
