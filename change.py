import subprocess
import random
import time
from twisted.internet import task
from twisted.internet import reactor

# subprocess.call(["defaults", "write", "com.apple.Desktop", "background" ])
images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg' , '6.jpg']

timeout = 10.0

SCRIPT = """
osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/paulmartin/Desktop/Background/{}" '
""".format(random.choice(images))

def set_desktop_background():
    subprocess.Popen(SCRIPT, shell=True)
    # time.sleep(10)

# l = task.LoopingCall(set_desktop_background)
# l.start(timeout)

# reactor.run()

if __name__ == '__main__':
	# while True:
	set_desktop_background()
		# time.sleep(10)
