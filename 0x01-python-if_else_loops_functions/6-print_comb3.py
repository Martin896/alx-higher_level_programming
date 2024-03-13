#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        print("{}{}, ".format(i, j) if i != 8 or j != 9
              else "{}{}".format(i, j), end="\n" if i == 8 and j == 9 else "")
