def objective_function(x):
    # CHANGED: Replaced ^ with ** for correct algebraic squaring
    return -4 * (x - 5)**2 + 100

def HILL_CLIMBING(start, step_size, max_iterations):
    current_position = start
    current_value = objective_function(current_position)
    
    for i in range(max_iterations):
        left_position = current_position - step_size
        right_position = current_position + step_size
        
        left_value = objective_function(left_position)
        right_value = objective_function(right_position)
        
        # CHANGED: Compare left and right together to choose the absolute best neighbor
        if left_value > current_value and left_value >= right_value:
            current_position = left_position
            current_value = left_value
        elif right_value > current_value and right_value > left_value:
            current_position = right_position
            current_value = right_value
        else:
            # Peak reached: neither neighbor is higher than the current value
            break
            
    return current_position, current_value

# User input section matching your exact format
start = float(input("enter the starting value: "))
step_size = float(input("enter the step size: "))
max_iterations = int(input("enter maximum iterations: "))

best_position, best_value = HILL_CLIMBING(start, step_size, max_iterations)

print("\nBEST POSITION=", best_position)
print("MAXIMUM VALUE=", best_value)
