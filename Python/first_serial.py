import serial

arduino = serial.Serial('com4',9600)
def do_something():
	if(arduino.inWaiting()>0):
		data = arduino.readline()
		data = int(data);
		print(data)

try:
    while True:
        do_something()
except KeyboardInterrupt:
        print('uy')
        arduino.close()
