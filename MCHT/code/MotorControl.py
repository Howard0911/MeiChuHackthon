import directionControl as DirCon
import sys, termios, tty, os, time

speed =255
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
button_delay = 0.1
while True:
	try:
		char = getch()
		if (char == "w"):
			print("Forward!")
			DirCon.Forward(speed)
			time.sleep(button_delay)
		elif (char == "a"):
			print("Left pressed")
			DirCon.LeftTurn()
			time.sleep(button_delay)
		elif (char == "s"):
			print("Backward!")
			DirCon.Backward(speed)
			time.sleep(button_delay)
		elif (char == "d"):
			print("Right pressed")
			DirCon.RightTurn
			time.sleep(button_delay)
		elif (char == "p"):
			print("Parking")
			time.sleep(button_delay*2)
			print("Parking achieve")
		elif (char == "t"):
			print("Terminated")
			DirCon.Stop()
			time.sleep(button_delay)
			break
		else:
			DirCon.Stop()
	except:
			DirCon.Stop()




