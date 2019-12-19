import socket
import threading
import time
from pynput.keyboard import Key,Listener


tello_address = ('192.168.10.1', 8889)


local_address = ('', 9000)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


sock.bind(local_address)

def send(message, delay):
  try:
    sock.sendto(message.encode(encoding='utf-8'), tello_address)
    print("\nSending message: " + message)
  except Exception as e:
    print("\nError sending: " + str(e))
  time.sleep(delay)

def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("\nReceived message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      print("\nError receiving: " + str(e))

receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

distance = 100
angle = 90
sec = 5

def start():
    send('command',3)

def takeoff():
    send('takeoff',sec)

def land():
    send('land',sec)

def forward():
    send('forward {}'.format(distance),sec)

def back():
   send('back {}'.format(distance),sec)

def up():
    send('up {}'.format(distance),sec)

def down():
    send('down {}'.format(distance),sec)

def cw():
    send('cw {}'.format(angle),sec)

def ccw():
    send('ccw {}'.format(angle),sec)

def left():
  send('left {}'.format(distance),sec)

def right():
  send('right {}'.format(distance),sec)

def battery():
  send('battery?', 3)


def cmd(key):
    # print("\nsending {0}".format(key))
    if key == Key.space:
      start()
    elif key == Key.shift_l:
      #print("\nTake off")
      takeoff()
    elif key == Key.shift_r:
      #print("\nLand")
      land()       
    elif key == Key.ctrl:
      #print("\nUp")
      up()
    elif key == Key.cmd:
      #print("\nDown")
      down()
    elif key == Key.up:
      #print("\nForward")
      forward()
    elif key == Key.down:
      #print("\nBack")
      back()
    elif key == Key.left:
      #print("\nLeft")
      left()
    elif key == Key.right:
      #print("\nRight")
      right()
    elif key == Key.caps_lock:
      #print("\nccw")
      ccw()
    elif key == Key.enter:
      #print("\ncw")
      cw()
    elif key == Key.tab:
      battery()
    else:
      pass

def on_release(key):
    if key == Key.esc:
        print("Drone turn off")
        socket.close
        return False

print('\r\n\r\nTello with keyboard\r')
print("\r\nTakeoff = Left-shift Land = Right-shift""\r\n       Control with arrows rotate = Caplock/Enter,  up/down = control/command\r\n")
print('Press ESC to quit.\r\n')

with Listener(on_press=cmd,on_release=on_release) as listener:
    listener.join()





