ADJ_FACTOR = 0.7

def is_capital_negative(capital):
    return capital < 0
def is_rate_and_duration_positive(rate, duration):
    return rate > 0 and duration > 0
def get_adjusted_capital(capital, rate, duration, income):
    result = 0
    if is_capital_negative(capital):
        return
    if is_rate_and_duration_positive(rate, duration):
        return (income / duration) * ADJ_FACTOR
    

adjusted_capital = get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital)