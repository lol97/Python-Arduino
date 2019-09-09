import serial

arduino = serial.Serial('com4',9600)

def ledController():
	cmd = input('type on/off/dc : ')
	cmd = str.lower(cmd)
	if(cmd == "on"):
		arduino.write('H'.encode())
		print("Lampu Nyala")
	elif(cmd == "off"):
		arduino.write('L'.encode())
		print("Lampu Mati")
	elif(cmd == "dc"):
		arduino.close()
		print("Lampu Mati")
	else:
		print("Ngetik yang bener pilih on / off / dc")

try:
	while (True):
		ledController()
except KeyboardInterrupt:
	arduino.close()
	print('has disconnected')