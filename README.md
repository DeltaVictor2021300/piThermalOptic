# piThermalOptic
Drivers for Pi based Thermal Optic in development

## Setup
Download the Pi imager and flash the 64 bit lite image to your SD card
make sure you enable SSH and pre configure your network settings
https://www.raspberrypi.com/software/

Once you have shelled into your system update it
```
sudo apt-get update
sudo apt-get upgrade
```

Install git and clone the repository
```
sudo apt-get install git
git clone https://github.com/DeltaVictor2021300/piThermalOptic.git
```

Install python and pip
```
sudo apt-get install python3
sudo apt-get install python3-pip
```

Setup the python virtual environment
```
python3 -m venv .env
source .env/bin/activate
```

Install adafruit drivers
```
pip3 install Adafruit-Blinka
pip3 install adafruit-circuitpython-rgb-display
```

Install driver dependecies
```
sudo apt-get install fonts-dejavu
pip install pillow
sudo apt-get install libopenjp2-7 libatlas-base-dev
pip install opencv-python
```

Run ```sudo raspi-config``` and enable the spi interface

Reboot the system ```sudo reboot```

Modify bashrc so it executes the code on boot
```
nano ~/.bashrc
```
Add this line to the bottom of the file
```
source $HOME/.env/bin/activate
python3 $HOME/piThermalOptic/piOptic.py
```
