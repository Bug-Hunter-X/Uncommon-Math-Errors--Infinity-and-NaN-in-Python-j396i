import sys

def function_with_improved_error_handling(x, y):
    if y == 0:
        print("Error: Division by zero")
        return None
    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
      if math.isinf(x) or math.isinf(y) or math.isnan(x) or math.isnan(y):
        print("Error: Infinity or NaN encountered in calculation")
        return None 
      else:
        try:
            result = x / y
            return result
        except TypeError:
            print("Error: Unsupported operand type(s) for / ")
            return None
    else:
        print("Error: Invalid input type")
        return None
import math
# Example usage
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero, None
print(function_with_improved_error_handling(10, "a")) # Output: Error: Invalid input type, None

#Improved handling of uncommon errors
print(function_with_improved_error_handling(float('inf'), 2)) #Output: Error: Infinity or NaN encountered in calculation, None
print(function_with_improved_error_handling(float('inf'), float('inf'))) # Output: Error: Infinity or NaN encountered in calculation, None
print(function_with_improved_error_handling(float('nan'), 2)) #Output: Error: Infinity or NaN encountered in calculation, None