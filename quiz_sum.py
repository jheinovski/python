#!/usr/bin/env python3

_sum = 0

for i in range(10):
    try:
        if 10 / i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
        _sum += 1
    else:
        print(2)
        _sum += 2

print("\n{}".format(_sum))
