import webbrowser
import time
import random


def get_songs():
    songs = []
    fname = 'song_list.txt'
    with open(fname) as fh:
        for line in fh:
            songs.append(line)
    return songs


def take_break(num_breaks):
    count = 0
    tunes = get_songs()
    num_tunes = len(tunes) - 1
    while count < num_breaks:
        # time.sleep(2*60*60)
        time.sleep(5)
        song_index = random.randint(0, num_tunes)
        print "Break time " + time.ctime()
        webbrowser.open(tunes[song_index])
        count += 1


requested_breaks = int(raw_input('How many breaks should the dude get? '))
take_break(requested_breaks)
