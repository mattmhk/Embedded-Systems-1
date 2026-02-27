def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both numerator and denominator must be numbers."
    else:
        print("Division successful.")
    print("Execution completed.")
    
print(safe_divide(10, 2))  
print(safe_divide(10, 0))  
print(safe_divide(10, 'a'))
print(safe_divide(15, 3))