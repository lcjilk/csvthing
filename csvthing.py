import csv


filename = input('Please enter a filename: ')

def get_carton_size(carton):
    pass

def get_unit_price(price, unit):
    price_usd = int(price)
    lot_size = None
    if unit == 'carton':
        lot_size = get_carton_size()
    else:
        lot_size = int(unit)
    return price_usd / lot_size

with open(filename) as csvf:
    # if col 2 is > 100:
    headers = list()
    for l in csv.reader(csvf):
        if not headers:
            headers = l
            continue
        print(get_unit_price(l[0], l[1]))


