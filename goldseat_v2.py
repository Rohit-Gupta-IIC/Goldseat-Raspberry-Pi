######### pi basic setup ##############
import subprocess as sub, sqlite3, os,sys

def goldseat(inp, oup):
	## Command to sync
	print(inp, oup)

	print(t1.communicate()[0])
	return

def intia():
	global serial
	c=sqlite3.connect("pi.db")
	c.execute('''CREATE TABLE if not exists Pi_details (Pid text(50))''')
	c.commit()

	######### block to find the uniue raspberry py id ##############
	t = sub.Popen(["cat","/proc/cpuinfo"],stdout=sub.PIPE)
	output=t.communicate()[0]
	output=(str(output.decode('utf8'))).split()
	a=0
	while a<len(output):
		if output[a]=="Serial":
			serial=str(output[a+2])
		a=a+1
	######## block to check software is binded with any other raspberry pi ########
	cu= c.cursor()
	cu.execute("select Pid from Pi_details")
	buss=str(cu.fetchall()).rstrip('\n')

	####### block to bind pi with the raspberry pi id ############
	if buss == "[]":
		c.execute("INSERT INTO Pi_details values (?)",(serial,))
		c.commit()
	cu.execute("select * from Pi_details")
	buss=str(cu.fetchall()[0][0]).rstrip('\n')
	c.close()
	return buss

def device():
	################ block to list the devices connected on usb ports ##############
	r = sub.Popen(["lsusb","-t"], stdout=sub.PIPE)
	output=r.communicate()[0]	
	output=str(output.decode('utf-8'))
	output=output.split()
	a=0
	while a <len(output):
		if output[a]=="Driver=usb-storage,":
			print("Device Connected at: Port "+str(output[a-7]).strip(':'))
		a=a+1
	return

def size():
	######### block to find the empty space on pi ###########
	t = sub.Popen(["df","/root"],stdout=sub.PIPE)
	output=t.communicate()[0]
	output=(str(output.decode('utf8'))).split()
	pi=int(output[10])
	######### block to find the size of sd card ###########
	t1 = sub.Popen(["df","/dev/sda"],stdout=sub.PIPE)
	output=t1.communicate()[0]
	output=(str(output.decode('utf8'))).split()
	sda=int(output[8])
	return pi,sda

def filep():
	os.chdir("/home/pi/")
	# block to find if image is already present on the disk or not
	pwd = os.path.dirname(os.path.realpath(__file__)).rstrip('\n')
	onlyfiles = [ f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f)) ]
	i=0
	file_p =  False
	while i < len(onlyfiles):
		if onlyfiles[i] == "goldseat.img":
			file_p= True
		i=i+1
	return file_p

def main_logic(buss):
	test = 0
 	########### Main logic starts ###############
	
	if buss == serial:
		device()
		print("device executed")
		size_pi, size_sda = size()
		#print("size executed")
		file_presence = filep()
		#print("file executed")
		# count the arguments
		arguments = len(sys.argv) - 1
		# to create backup file
		if arguments>=1 and sys.argv[1] == "-r":
			#if the img file exists then delete it
			if file_presence == True:
				_= sub.Popen(["sudo","rm","/home/pi/goldseat.img"],stdout=sub.PIPE)
			# image is create if pi has empty space equal to size of sd card plus 1 GB
			if size_pi >= (size_sda+1048576):
				print("Image backup in progress")
				t = sub.Popen(["sudo","dd","if=/dev/sda","of=/home/pi/goldseat.img","status=progress","bs=16M"],stdout=sub.PIPE)
				print("Image Backup complete")
				test = 0
			else:
				print("Image creation service cannot be started, as the pi doesnot not have enough space")
			if test ==0:
					print("Sync started")
					t1 = sub.Popen(["sudo", "sync", "/dev/sda", "/home/pi/goldseat.img"], stdout=sub.PIPE)
					print("Sync Ended")
		# to write backup file
		else:
			#if the file does not exist than we create it
			if file_presence == False:
					print("File does not already exist, kindly create the backup first")
			else:
				# 100MB space is kept on the USB
				if (size_sda+104857600) >= size_pi :
					print("Image restore in progress")
					t = sub.Popen(["sudo","dd","of=/dev/sda","if=/home/pi/goldseat.img","status=progress","bs=16M"],stdout=sub.PIPE)
					print("Image restore completed")
					test = 0
				else:
					print("Image restore service cannot be started, as the sd card doesnot not have enough space")
			if test == 0:
					print("Sync started")
					t1 = sub.Popen(["sudo", "sync", "/dev/sda", "/home/pi/goldseat.img"], stdout=sub.PIPE)
					print("Sync Ended")	
	else:
		print("Service cannot work, as the license key doesnot matches")
		print("Please launch the application from the designated machine")
	return


if __name__ == "__main__":
	buss = intia()
	if buss:
		main_logic(buss)
