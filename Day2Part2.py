import time
import pandas as pd
from memory_profiler import profile


# @profile
def Day2Part2():
    excel_data_df = pd.read_excel(
        "E:\RJC\Advent of code-Learning\Day 2\Day2input.xlsx", names=["opponent", "me"]
    )

    # print whole sheet data
    # print(excel_data_df)
    me_choose = 0
    me_choose_list = []
    Score_list = []
    score = 0

    GAME_opponent = (
        excel_data_df["opponent"]
        .replace(["A", "B", "C"], ["1", "2", "3"])
        .apply(pd.to_numeric)
        .tolist()
    )

    GAME_me = (
        excel_data_df["me"]
        .replace(["X", "Y", "Z"], ["0", "3", "6"])
        .apply(pd.to_numeric)
        .tolist()
    )

    for i in range(len(GAME_me)):
        if GAME_me[i] == 3:
            me_choose = GAME_opponent[i] + 0
        elif GAME_me[i] == 6:
            if 1 <= GAME_opponent[i] + -2 <= 3:
                me_choose = GAME_opponent[i] + -2
            else:
                me_choose = GAME_opponent[i] + 1
        elif GAME_me[i] == 0:
            if 1 <= GAME_opponent[i] + -1 <= 3:
                me_choose = GAME_opponent[i] + -1
            else:
                me_choose = GAME_opponent[i] + 2

        score = GAME_me[i] + me_choose
        # print(me_choose, GAME_opponent[i], GAME_me[i], score)
        Score_list.append(score)

    return sum(Score_list)


def timecode():
    itnum = 100
    Timefortimecode = 0
    for i in range(itnum):
        time_start = time.perf_counter()
        Day2Part2()
        time_elapsed = time.perf_counter() - time_start
        Timefortimecode += time_elapsed
    return "%5.5f secs " % (Timefortimecode / itnum)


print(timecode())


print(Day2Part2())
