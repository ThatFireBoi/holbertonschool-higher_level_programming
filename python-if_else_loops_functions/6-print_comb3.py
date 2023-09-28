#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        if i / 10 < i % 10:
            print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
