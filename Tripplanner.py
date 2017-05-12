def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475

def rental_car_cost(days):
    per_day = 40 * days
    if days >= 7:
        return per_day - 50
    elif days >= 3:
        return per_day - 20
    else:
        return per_day

def trip_cost(city, days, spending_money):
    return plane_ride_cost(city) + hotel_cost(days) + rental_car_cost(days) + spending_money

print trip_cost('Los Angeles', 5, 600)
