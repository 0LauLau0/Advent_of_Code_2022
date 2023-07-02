import time
from memory_profiler import profile

import re

path1 = "E:\RJC\Advent of code-Learning\Day 4\Day4testinput.txt"
path2 = "E:\RJC\Advent of code-Learning\Day 4\Day4input.txt"


# @profile
def fun(path):
    input = open(path, "r")
    count = 0
    full_contain = 0
    for line in input:
        count += 1
        pair = [int(i) for i in re.split("[- , ]", line.strip("\n"))]
        if pair[0] <= pair[2] and pair[1] >= pair[3]:
            full_contain += 1
        elif pair[2] <= pair[0] and pair[3] >= pair[1]:
            full_contain += 1
    return full_contain


# @profile
def fun2(path):
    input = open(path, "r")
    count = 0
    not_contain = 0
    for line in input:
        count += 1
        pair = [int(i) for i in re.split("[- , ]", line.strip("\n"))]
        if pair[1] < pair[2]:
            not_contain += 1
        elif pair[3] < pair[0]:
            not_contain += 1
    return count - not_contain


def timecode():
    itnum = 1000
    Timefortimecode = 0
    for i in range(itnum):
        time_start = time.perf_counter()
        fun2(path2)
        time_elapsed = time.perf_counter() - time_start
        Timefortimecode += time_elapsed
    return "%5.5f ms " % (Timefortimecode / itnum * 1000)


print(timecode())


# print(fun(path1))
# print(fun(path2)) #19.5 MiB 2.33494 ms
# print(fun2(path2)) #19.5 MiB 2.36795 ms
