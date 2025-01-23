def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero, None
print(function_with_uncommon_error(10, "a")) # Output: Error: Unsupported operand type(s) for /, None

#Uncommon error that might occur
print(function_with_uncommon_error(float('inf'), 2)) #Output: inf
print(function_with_uncommon_error(float('inf'), float('inf'))) # Output: nan
print(function_with_uncommon_error(float('nan'), 2)) #Output: nan