numbers = [210, 4, 8, 15, 16, 23, 42, 52, 101, 35]
odd = []
even = []
print("Original list of numbers:", numbers)

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("List of odd numbers:", odd)
print("List of even numbers:", even)