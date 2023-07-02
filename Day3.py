import time
from memory_profiler import profile

import string

path1 = "E:\RJC\Advent of code-Learning\Day 3\Day3testinput.txt"
path2 = "E:\RJC\Advent of code-Learning\Day 3\Day3.txt"


# @profile
def fun(path):
    input = open(path, "r")
    count = 0
    duplicate = []
    duplicate_upper = []
    duplicate_lower = []
    duplicate_upper_priority = []
    duplicate_lower_priority = []

    for line in input:
        count += 1
        stringlen = len(line)
        stringlen_half = stringlen // 2
        first = line[slice(0, stringlen_half)]
        second = line[slice(stringlen_half, stringlen)]

        for i in second:
            if first.count(i) + first.count(i) > 1:
                duplicate.append(i)
                if i.isupper():
                    duplicate_upper.append(i)
                    duplicate_upper_priority.append(
                        string.ascii_uppercase.index(i) + 27
                    )
                else:
                    duplicate_lower.append(i)
                    duplicate_lower_priority.append(string.ascii_lowercase.index(i) + 1)
                break

    #     print(
    #         "Line{}:, {} , {},{}".format(count, len(line.strip()) // 2, first, second)
    #     )
    # print(duplicate_upper_priority)
    # print(duplicate_lower_priority)

    return sum(duplicate_upper_priority) + sum(duplicate_lower_priority)


profile


def fun2(path):
    input = open(path, "r")
    count = 0
    threelines = 0
    strlist = []
    duplicate = []
    duplicate_upper = []
    duplicate_lower = []
    duplicate_upper_priority = []
    duplicate_lower_priority = []
    for line in input:
        count += 1
        threelines += 1
        strlist.append(line.strip("\n"))
        if threelines % 3 == 0:
            for i in strlist[0]:
                if strlist[1].count(i) >= 1 and strlist[2].count(i) >= 1:
                    duplicate.append(i)
                    if i.isupper():
                        duplicate_upper.append(i)
                        duplicate_upper_priority.append(
                            string.ascii_uppercase.index(i) + 27
                        )
                    else:
                        duplicate_lower.append(i)
                        duplicate_lower_priority.append(
                            string.ascii_lowercase.index(i) + 1
                        )
                    break

            # print(duplicate)
            threelines = 0
            strlist = []
    return sum(duplicate_upper_priority) + sum(duplicate_lower_priority)


def timecode():
    itnum = 5000
    Timefortimecode = 0
    for i in range(itnum):
        time_start = time.perf_counter()
        fun2(path2)
        time_elapsed = time.perf_counter() - time_start
        Timefortimecode += time_elapsed
    return "%5.5f ms " % (Timefortimecode / itnum * 1000)


print(timecode())


# print(fun(path2))  # 19.4MB 1.18ms
# print(fun2(path2))  # 19.7MB 0.63538ms
