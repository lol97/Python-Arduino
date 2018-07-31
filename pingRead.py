import serial

arduino = serial.Serial('com4',9600)

def doSomething():
	data = int(arduino.readline())
	print(data)

try:
	while (True):
		doSomething()
except KeyboardInterrupt:
	arduino.close()
	print('has disconnected')
