# 91 Find the smallest number

numbers = [15, 8, 23, 4, 19]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)