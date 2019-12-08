# raspberry-pi-dvd-player
Use a Raspberry Pi as a DVD player

Features:
- Automatically play a DVD as soon as it is inserted
- Skips trailers, etc. by default
- Entirely console and framebuffer based playback (i.e. no X11/Wayland) so very low power and quick to boot
- Use any existing IR remote to play/pause/rewind/forward
- Turns screen on automatically when a DVD is inserted
- DVD splash screen
- Silent boot

## DVD Player Setup

You will need:
- A micro SD card
- A Raspberry Pi (I've tested on a Pi Zero and Pi Zero W)
- A USB DVD drive

1. Install [Rasbian Lite](https://www.raspberrypi.org/downloads/raspbian/) on the micro SD card

2. Purchase a MPEG2 license from [here](http://www.raspberrypi.com/mpeg-2-license-key/). You will need the serial number from your Raspberry Pi which can be found by running `cat /proc/cpuinfo`.

3. Add the serial number to `/boot/config.txt`. You will receive an email telling you what to add.

4. Install VLC:
```shell
sudo apt-get install -y vlc
```

5. Copy [`dvd-play.service`](/etc/systemd/system/dvd-play.service) to `/etc/systemd/system/`.

6. Add a udev rules to start/stop this service when a DVD is inserted/ejected by copying [`90-dvd.rules`](etc/udev/rules.d/90-dvd.rules) to `/etc/udev/rules.d/`.

## Remote control setup

You will need:
- [Flirc USB dongle](https://flirc.tv/more/flirc-usb) connected to the Raspberry Pi

1. Install Flirc

```shell
curl apt.flirc.tv/install.sh | sudo bash 
```

2. Assign the keys on your remote to regular keys. Do not use the `play/pause`, `fastforward`, etc. commands.

```shell
flirc_util record p # Press play/pause
flirc_util record r # Press rewind
flirc_util record f # Press fast forward
flirc_util record s # Press stop
```
 
3. Install Python dependencies:

```
sudo apt-get install -y python3-pip
pip3 install evdev
```

4. Copy [`vlc_media_buttons.py`](home/pi/vlc_media_buttons.py) to `/home/pi`.

5. Copy [`dvd-remote.service`](etc/systemd/system/dvd-remote.service) to `/etc/systemd/system/`.

6. Enable the service:

```shell
sudo systemctl enable dvd-remote 
```

 ## Automatically turn on the screen when a DVD is inserted
 
 (HDMI-CEC compatible screen only.)
 
 1. To prevent the screen turning on when the Pi boots, add the following to `/boot/config.txt`:
 
 ```
 hdmi_ignore_cec_init=1
 ```
 
 2. Install `cec-utils`:
 
 ```shell
 sudo apt-get install -y cec-utils
 ```
 
 3. Copy [`turn-on-screen.service`](/etc/systemd/system/turn-on-screen.service) to `/etc/systemd/system/`.

## DVD background and quiet boot

1. Copy [`dvd.jpg`](usr/share/backgrounds/dvd.jpg) to `/usr/share/backgrounds/`. You may need to create the directory.

2. Install `fim`:

```shell
sudo apt-get install -y fim
```

3. Copy [`dvd-background.service`](etc/systemd/system/) to `/etc/systemd/system/`.

4. Enable the service:

```shell
sudo systemctl enable dvd-background
```

5. To show a blank screen when booting the following to the first line of `/boot/cmdline.txt`:

```
loglevel=3 quiet logo.nologo vt.global_cursor_default=0
```

6. To hide boot output while the Raspberry Pi boots change `console=tty1` to `console=tty3` in `/boot/cmdline.txt`.
