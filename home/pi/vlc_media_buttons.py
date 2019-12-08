#!/usr/bin/env python3

from evdev import InputDevice, ecodes, categorize
from select import select
import requests
from urllib.parse import urlencode
from argparse import ArgumentParser


def handle_vlc_media_buttons(input_device, http_password, debug=False):

  def vlc_action(params):
    url = 'http://localhost:8080/requests/status.xml?' + urlencode(params)
    if debug: print(url)
    request = requests.get(url, timeout=2, auth=('', http_password))
    if not request.ok:
      request.raise_for_status()

  device = InputDevice(input_device)
  device.grab()
  for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
      key_event = categorize(event)
      if key_event.keystate == key_event.key_down:
        if debug: print(key_event.keycode)
        key = key_event.scancode
        try:
          if key == ecodes.KEY_PLAYPAUSE or key == ecodes.KEY_P:
            vlc_action({ 'command': 'pl_pause' })
          elif key == ecodes.KEY_STOP:
            vlc_action({ 'command': 'pl_stop' })
          elif key == ecodes.KEY_REWIND or key == ecodes.KEY_R:
            vlc_action({ 'command': 'seek', 'val': '-30s' })
          elif key == ecodes.KEY_FASTFORWARD or key == ecodes.KEY_F:
            vlc_action({ 'command': 'seek', 'val': '+30s' })
        except Exception as e:
          print('Warning:', key_event.keycode, 'failed', e if debug else '')

if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('device', help='Keyboard input device, e.g. /dev/input/event0')
  parser.add_argument('--password', default='', help='VLC HTTP basic auth password for localhost:8080')
  parser.add_argument('--debug', nargs='?', const=True, default=False, help='Show additional information')
  args = parser.parse_args()
  handle_vlc_media_buttons(args.device, args.password, debug=args.debug)
