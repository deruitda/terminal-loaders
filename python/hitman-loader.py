import time

def printHitmanBar(pos, len):
    line = '█'
    start = ('-' * pos)
    end = ('-' * (len - pos - 1))
    bar = "\t|" + start + line + end + '|'

    print(bar, end = "\r")

pos = 0
len = 50
while(1):
    printHitmanBar(pos, len)

    pos += 1

    if pos >= len:
        pos = 0

    time.sleep(0.1)
