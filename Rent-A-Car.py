def initialize_cars():
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True},
        {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": True},
        {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price": 55, "available": True},
        {"id": 4, "brand": "Mercedes", "model": "C-Class", "rental_price": 50, "available": True},
        {"id": 5, 'brand': "BMW", "model": "X5", "rental_price": 55, "available": True},
        {"id": 6, 'brand': "Volkswagen", "model": "Golf", "rental_price": 30, "available": True}
    ]
    return cars

def rent_car(cars, car_id):
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"You have rented the {car['brand']} {car['model']}."
    return "Car is unavailable or invalid car ID."

def return_car(cars, car_id, days):
    for car in cars:
        if car["id"] == car_id and car["available"] == False:
            car["available"] == True
            price = days * car['rental_price']
            return f'Thank you for returning the {car["brand"]}!\nYou have used it for {days} and it will cost you {price}'
        return "Car hasn't been rented. Please check ID."