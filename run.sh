sudo apt install sqlite3 sqlitebrowser
sudo sed -i -e 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile 
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
python3 final.py
