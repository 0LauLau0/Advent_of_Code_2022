import copy

Inputpath = "E:\RJC\Advent of code-Learning\Day 1\Day1FirstInput.text"
elfNum = 1
Calories = []
curentColories = 0
maxCalories1 = 0
maxCalories2 = 0
maxCalories3 = 0
elfMax = 1

with open(Inputpath) as f:
    while True:
        line = f.readline()
        # print(line)
        if not line:
            break
        if line != "\n":
            curentColories += int(line)
        else:
            # print("elf")
            if curentColories > maxCalories3:
                maxCalories3 = copy.deepcopy(curentColories)
            elif curentColories > maxCalories2:
                maxCalories2 = copy.deepcopy(curentColories)
            elif curentColories > maxCalories1:
                maxCalories1 = copy.deepcopy(curentColories)
                elfMax = copy.deepcopy(elfNum)
            Calories.append(curentColories)
            curentColories = 0
            elfNum += 1

print("Elf number: ", elfNum)
print("No.", elfMax, " has the max Calories: ", maxCalories1)
# print(Calories)

print(sum([maxCalories1, maxCalories2, maxCalories3]))
