def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.") # copilot suggested this line and I accepted it to make the if case
    
    flightTime = 180 - (.1 * weight_grams)
    if flightTime < 0:
        return 0
    return flightTime


def flight_time_table(max_weight_grams, step_grams):
    if step_grams <= 0:
        raise ValueError("Step size must be a positive number.")

    table =[] # copilot suggested that i make an if statement to check and make sure the max weight grams is not 0 and that steps are not 0
              # I used it to make sure the steps were not 0 but I wanted the fact that the max weight CAN be 0 to stay
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time)) # copilot suggested that i make a list or some variable called appended = to (weight, setps) which is an unnecessary step so i didnt do it.
    return table

#  INPUT SECTION 
if __name__ == "__main__":
    
    max_weight = 0
    step = 0
    
    results = flight_time_table(max_weight, step)
    
    print("Weight (g) | Flight Time (min)")
    print("-" * 30)
    for weight, time in results:
        print(f"{weight:<10} | {time:.2f}")