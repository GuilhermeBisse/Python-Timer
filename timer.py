import time
import sys

def timer(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    while minutes >= 0:
        sys.stdout.write('\r')
        sys.stdout.write(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
        if seconds < 0:
            seconds = 59
            minutes -= 1
        if minutes < 0:
            minutes = 59
            hours -= 1
        if hours < 0:
            sys.stdout.write('\r')
            sys.stdout.write("Tempo acabou, betinha!")
            sys.stdout.flush()
            break
    print()

if __name__ == '__main__':
    timer(10)
