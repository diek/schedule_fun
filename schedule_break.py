import webbrowser
import time

count = 0
print "Current time " + time.ctime()
while count < 3:
    time.sleep(2)
    print count
    # webbrowser.open("https://www.youtube.com/watch?v=20S_kwNb4rg")
    count += 1
