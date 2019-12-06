# raspberry-pi-dvd-player
Use a Raspberry Pi as a DVD player

## DVD Player Setup

You will need:
- Micro SD card
- Raspberry Pi
- A USB DVD drive

1. Install [Rasbian Lite](https://www.raspberrypi.org/downloads/raspbian/) on the micro SD card
2. Purchase a MPEG2 license from [here](http://www.raspberrypi.com/mpeg-2-license-key/). You will need the serial number from your Raspberry Pi which can be found by running `cat /proc/cpuinfo`.
3. Add the serial number to `/boot/config.txt`. You will receive an email telling you what to add.
4. Install VLC:
    ```shell
    sudo apt-get install -y vlc
    ```

## Remote control setup

You will need:
- [Flirc USB dongle](https://flirc.tv/more/flirc-usb) connected to the Raspberry Pi

1. Install:
    ```shell
    sudo apt-get -y install python3-pip
    pip3 install evdev
    ```
2. Install Flirc
    ```shell
    curl apt.flirc.tv/install.sh | sudo bash 
    ```
3. Assign the keys on your remote to regular keys. Do not use the `play/pause`, `fastforward`, etc. commands.
    ```shell
    flirc_util record p # Press play/pause
    flirc_util record r # Press rewind
    flirc_util record f # Press fast forward
    flirc_util record s # Press stop
 
 TODO: Scripts to come
    
