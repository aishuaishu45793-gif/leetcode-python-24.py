# 92 Count positive and negative numbers

numbers = [10, -5, 3, -8, 0, 7, -2]

positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)