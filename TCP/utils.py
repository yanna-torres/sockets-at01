
CURRENCY_RATES = [('USD', 4.95), ('EUR', 5.37), ('GBP', 6.28), ('JPY', 0.033)]

def convert_currency(value, currency):
    for c in CURRENCY_RATES:
        if c[0] == currency:
            return value * c[1]
    return -1