rate = 10

def calculate_dynamic_pricing(distance,time_of_day,partners):
    dynamic_price = rate * distance
    return dynamic_price

if __name__ == '__main__':
    distance = 15
    dp = calculate_dynamic_pricing(distance,'','')
    print(dp)
    
