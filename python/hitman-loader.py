import time

def printHitmanBar(pos, len, line):
    start = (' ' * pos)
    end = (' ' * (len - pos - 1))
    bar = "\t|" + start + line + end + '|'

    print(bar, end = "\r")
    time.sleep(0.05)

pos = 0
len = 20
while(1):
    printHitmanBar(pos, len, '█')
    pos += 1

    if pos >= len:
        while(pos > 0):
            pos -= 1
            printHitmanBar(pos, len, '|')
