######### pi basic setup ##############
import subprocess as sub, sqlite3, os,sys
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

########### Main logic starts ###############
if buss:
	if buss == serial:
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
		######### block to find the empty space on pi ###########
		t = sub.Popen(["df","/root"],stdout=sub.PIPE)
		output=t.communicate()[0]
		output=(str(output.decode('utf8'))).split()
		size_pi=int(output[10])
		######### block to find the size of sd card ###########
		t1 = sub.Popen(["df","/dev/sda1"],stdout=sub.PIPE)
		output=t1.communicate()[0]
		output=(str(output.decode('utf8'))).split()
		size_sda=int(output[8])
		# block to find if image is already present on the disk or not
		pwd = os.path.dirname(os.path.realpath(__file__)).rstrip('\n')
		onlyfiles = [ f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f)) ]
		i=0
		file_presence =  False
		while i < len(onlyfiles):
			if onlyfiles[i] == "hello.img":
				file_presence= True
			i=i+1
		# count the arguments
		arguments = len(sys.argv) - 1
		# to create backup file
		if arguments>=1 and sys.argv[1] == "-r":
			#if the img file exists then delete it
			if file_presence == True:
				_= sub.Popen(["sudo","rm","/home/pi/hello.img"],stdout=sub.PIPE)
			# image is create if pi has empty space equal to size of sd card plus 1 GB
			if size_pi >= (size_sda+1048576):
				t = sub.Popen(["sudo","dd","if=/dev/sda1","of=/home/pi/hello.img","status=progress","bs=16M"],stdout=sub.PIPE)
			else:
				print("Image creation service cannot be started, as the pi doesnot not have enough space")
		# to write backup file
		else:
			#if the file does not exist than we create it
			if file_presence == False:
       				print("File does not already exist, kindly create the backup first")
			else:
				# 100MB space is kept on the USB
				if (size_sda+104857600) >= size_pi :
					t = sub.Popen(["sudo","dd","of=/dev/sda1","if=/home/pi/hello.img","status=progress","bs=16M"],stdout=sub.PIPE)
				else:
					print("Image restore service cannot be started, as the sd card doesnot not have enough space")	
	else:
		print("Service cannot work, as the license key doesnot matches")
		print("Please launch the application from the designated machine")
