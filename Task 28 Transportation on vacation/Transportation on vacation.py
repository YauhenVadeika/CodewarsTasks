# my task solution
def rental_car_cost(d):
    cost = d * 40
    if d < 3:
        total = cost
    elif d >= 3 and d < 7:
        total = cost - 20
    else:
        total = cost - 50
    return total


print(rental_car_cost(1))
print(rental_car_cost(4))
print(rental_car_cost(7))
print(rental_car_cost(8))


# codewars task best solution
def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result


# codewars task best solution
def rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30
