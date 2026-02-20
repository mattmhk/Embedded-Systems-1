str_numbers = "210; 4; 8; 15; 16; 23; 42; 52; 101; 35"

words = str_numbers.split(";")
sum =0

for i in words:
    sum += int(i)
    
print(sum)
    