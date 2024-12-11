def function_with_uncommon_error_solution(a, b):
    if b == 0:
        return float('inf')  # Return positive infinity if dividing by zero
    else:
        return a / b

result = function_with_uncommon_error_solution(5, 0) # Returns inf
print(result)

result2 = function_with_uncommon_error_solution(5,2) # Returns 2.5
print(result2)

result3 = function_with_uncommon_error_solution(0,5) # Returns 0
print(result3)