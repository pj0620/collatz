#!/usr/bin/python3

from matplotlib import pyplot as plt
import sys

def update_progress(progress,label=None):
    barLength = 40 # Modify this to change the length of the progress bar
    status = ""
    if label is None:
        label = "Percent"
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
#        status = "\r\nDone...\r\n"
        status = ""
    block = int(round(barLength*progress))
    text = "\r" + label + ": [{0}] {1:.1f}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def h(x):
    b_str = format(x, 'b')
    return len(b_str) - len(b_str.rstrip('0'))

L = 100
Hs = [0]*L
x = (2**100)-1
for i in range(L):
    update_progress(float(i)/float(L))
    h_x = h(3*x+1)
    if i == 0:
        Hs[0] = h_x
    else:
        Hs[i] = h_x + Hs[i-1]

    x = int((3*x+1)*(2**(-1*h_x)))
update_progress(1.0)
print(" ")
plt.plot(Hs)
plt.show()