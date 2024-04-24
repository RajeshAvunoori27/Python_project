rate = 10
hour_of_day = {
    (0,6):1.25,
    (6,12):1,
    (12,18):1.5,
    (18,24):1.75  
    
}
def calculate_hour_of_day_pricing(hour_value,price):
    for k,v in hour_of_day.items():
        if k[0] <= hour_value <= k[1]:
            price = price * v
            break
    return price
def calculate_dynamic_pricing(distance,time_of_day,partners):
    dynamic_price = rate * distance
    dynamic_price = calculate_hour_of_day_pricing(time_of_day,dynamic_price)
    return dynamic_price

if __name__ == '__main__':
    distance = 15
    dp = calculate_dynamic_pricing(distance,19,'')
    print(dp)
    
