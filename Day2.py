import pandas as pd

excel_data_df = pd.read_excel(
    "E:\RJC\Advent of code-Learning\Day 2\Day2input.xlsx", names=["opponent", "me"]
)

# print whole sheet data
print(excel_data_df)
result = 0
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
    .replace(["X", "Y", "Z"], ["1", "2", "3"])
    .apply(pd.to_numeric)
    .tolist()
)

for i in range(len(GAME_me)):
    result = GAME_me[i] - GAME_opponent[i]

    if result == 0:
        score = GAME_me[i] + 3
    elif result == -1:
        score = GAME_me[i] + 0
    elif result == 2:
        score = GAME_me[i] + 0
    elif result == 1:
        score = GAME_me[i] + 6
    elif result == -2:
        score = GAME_me[i] + 6
    Score_list.append(score)

print(len(Score_list))
print(sum(Score_list))
