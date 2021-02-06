import time

def printHitmanBarMany(lines, len):
    bar = [' '] *  len
    for lineIndex in lines:
        if lineIndex > 0:
            bar[lineIndex] = '█'
        
        if lineIndex < 0:
            bar[-lineIndex] = '|'
    
    bar_str = ""
    for x in bar:
        bar_str += x

    print(bar_str, end = "\r")
    time.sleep(0.05)

def printMany():
    bar_len = 20
    lines = [0, 3, 6, 9, 12, 15, 18]
    num_lines = len(lines)
    while(1):
        printHitmanBarMany(lines, bar_len)
        for i in range(num_lines):
            lines[i] += 1

            if(lines[i] >= bar_len): #if the line index is at the max, set it to negative indicating it's moving backwards
                lines[i] = -(bar_len - 1)

        

printMany()

def printHitmanBar(pos, len, line):
    start = (' ' * pos)
    end = (' ' * (len - pos - 1))
    bar = "\t|" + start + line + end + '|'

    print(bar, end = "\r")
    time.sleep(0.05)

def printSingle():
    pos = 0
    len = 20
    while(1):
        printHitmanBar(pos, len, '█')
        pos += 1

        if pos >= len:
            while(pos > 0):
                pos -= 1
                printHitmanBar(pos, len, '|')


