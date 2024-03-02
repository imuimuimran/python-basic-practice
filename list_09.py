def car_detail(cr):
    return cr['year']

cars = [
    {
        'car' : 'Ford',
        'year' : 2005
    },
    {
        'car' : 'Mitsubishi',
        'year' : 2002
    },
    {
        'car' : 'BMW',
        'year' : 2019
    },
    {
        'car' : 'VN',
        'year' : 2011
    }
    
]

cars.sort(key = car_detail)

print(cars)