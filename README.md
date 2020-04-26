# Goldseat Raspberry Pi Backup Management System

The repository is a python3 based Raspberry Pi utility which creates the backup of a given Pi SD card, which then could be copied and unpacked to an unlimited number of Pi's

### Dependencies
1. Python3
2. SQLite3
3. SQLite3 Browser
4. Gnome-Panel

### USP
1. Creates backup of the whole of the SD card, hence duplicating all the software, settings, and projects.
2. The software can be accessed on to your mobile using a WiFi mechanism.
3. The backup and restore speed can go up to 16 MB/s
4. System used 2GB VRAM, hence accelerating the overall software performance and throughput
5. The system is secured by the Login-ID mechanism, once a device is locked by that can not be accessed without authorization

### Setup
in the shell execute the following commands
``` shell
git clone https://github.com/Rohit-Gupta-IIC/Goldseat-Raspberry-Pi.git
cd Goldseat-Raspberry-Pi
sudo chmod 777 run.sh
./run.sh
```

### Process to Execute
The software can be used by using the following commands

1. Use the following command to create the backup of the desired device
``` shell
python3 goldseat_v2.py -r
```
2. Use the following command to unpack the so created backup file to the desired device
``` shell
python3 goldseat_v2.py 
```
