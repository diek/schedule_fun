import webbrowser
import time


def take_break(num_breaks, tunes):
    count = 0
    print "Current time " + time.ctime()
    while count < num_breaks:
        time.sleep(2*60*60)
        webbrowser.open(tunes[count])
        count += 1

song1 = "https://www.youtube.com/watch?v=Gp-PKmbcF7c#t=206"
song2 = "https://www.youtube.com/watch?v=20S_kwNb4rg"
song3 = "https://www.youtube.com/watch?v=Bayek5lLZWY"
song_list = [song1, song2, song3]
take_break(3, song_list)
