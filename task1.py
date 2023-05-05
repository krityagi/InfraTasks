import random

numbers = list(range(1, 11))

for i in range(len(numbers)):
    index1 = random.randint(0, len(numbers)-1)
    index2 = random.randint(0, len(numbers)-1)
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

print(numbers)
