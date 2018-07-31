import serial

arduino = serial.Serial('com4',9600)
cond = True
def ledController():
	cmd = input("type on/off/dc")
	cmd = str.lower(cmd)
	if( cmd == "on"):
		print("Led is On")
		arduino.write('H'.encode())
	elif (cmd == 'off'):
		print("Led is On")
		arduino.write('L'.encode())
	elif (cmd == 'dc'):
		arduino.close()
		print('Bye Bye')
		cond = False
	else:
		print('Hmmmm ?')

try:
	while (cond):
		ledController()
except KeyboardInterrupt:
	arduino.close()
	print('uyyy')




