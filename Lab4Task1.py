
lst_numbers = [210, 4, 8, 15, 16, 23, 42, 52, 101, 35]
sum=0
max = lst_numbers[0]
min = lst_numbers[0]

for i in lst_numbers:
    sum = sum + i
    if i > max:
        max = i
    if i < min:
        min = i

print("The sum of all the numbers in the list:", sum)
print("The average of all the numbers in the list:", sum/len(lst_numbers))
print("The maximum number in the list:", max)
print("The minimum number in the list:", min)