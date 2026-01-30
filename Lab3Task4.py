sales = [2389, 1467, 5665, 1009, -12, 7809, 3689, 8729, -0.9, -99, 643, 5908]
corrected_sales = []

for sale in sales:
    if sale < 0:
        corrected_sales.append(0)
    else:
        corrected_sales.append(sale)
        
print(corrected_sales[0])
print(corrected_sales[4])
print(corrected_sales[11])