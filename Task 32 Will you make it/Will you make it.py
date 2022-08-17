# my task solution
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 25, 2))
print(zero_fuel(27, 20, 2))

# codewars task best solution
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
