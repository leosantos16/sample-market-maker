from subprocess import Popen
import sys

filename = 'run.py'
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
