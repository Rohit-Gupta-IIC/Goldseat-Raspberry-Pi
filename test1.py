import os, subprocess
r = subprocess.Popen(["lsusb","-t"], stdout=subprocess.PIPE)
output=r.communicate()[0]	
output=str(output.decode('utf-8'))
output=output.split()
a=0
while a <len(output):
	if output[a]=="Driver=usb-storage,":
		print("Device Connected at: Port "+str(output[a-7]).strip(':'))
	a=a+1
