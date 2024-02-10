numbers = [9, 5, 4, 1, 7, 94, 513, 574, -1, -200, 0]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]

print(numbers)
