sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y
sudo apt install sqlite3 sqlitebrowser -y
sudo apt-get install --no-install-recommends gnome-panel -y
sudo sed -i -e 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile 
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
{
echo '#!/usr/bin/env xdg-open'
echo '[Desktop Entry]'
echo 'Version=1.0'
echo 'Icon[en_IN]=gnome-panel-launcher'
echo 'Name[en_IN]=Goldseat Read'
echo 'Type=Application'
echo 'Terminal=true'
echo 'Exec=python3 /home/pi/goldseat/goldseat_v2.cpython-37.pyc -r'
echo 'Name=Goldseat Read'
echo 'Icon=gnome-panel-launcher'
echo 'StartupNotify=true'
} > /home/pi/Desktop/Goldseat-Read.desktop

{
echo '#!/usr/bin/env xdg-open'
echo '[Desktop Entry]'
echo 'Version=1.0'
echo 'Icon[en_IN]=gnome-panel-launcher'
echo 'Name[en_IN]=Goldseat Write'
echo 'Type=Application'
echo 'Terminal=true'
echo 'Exec=python3 /home/pi/goldseat/goldseat_v2.cpython-37.pyc'
echo 'Name=Goldseat Write'
echo 'Icon=gnome-panel-launcher'
echo 'StartupNotify=true'
} > /home/pi/Desktop/Goldseat-Write.desktop
