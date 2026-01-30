numbers = []
count=0

while count<100:
    numbers.append(count**3)
    count+=1
print(numbers)

for num in numbers:
    if (num) % 10 == 0:
        print(num)