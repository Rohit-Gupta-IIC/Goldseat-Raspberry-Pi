import subprocess as sub
#t = sub.Popen(["sudo","dd","if=/media/pi/UBUNTU-SERV/doc.txt","of=/home/pi/hello.img","status=progress","bs=16M"],stdout=sub.PIPE)
t = sub.Popen(["df","/root"],stdout=sub.PIPE)
output=t.communicate()[0]
output=(str(output.decode('utf8'))).split()
size_pi=int(output[10])
t1 = sub.Popen(["df","/dev/sda1"],stdout=sub.PIPE)
output=t1.communicate()[0]
output=(str(output.decode('utf8'))).split()
size_sda=int(output[8])

print(size_pi,size_sda)
if size_pi >= (size_sda+1048576):
	print("service can start")
else:
	print("not allowed")
