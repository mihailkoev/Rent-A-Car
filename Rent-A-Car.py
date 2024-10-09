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


def display_cars(cars):
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")


def main_menu():
    print("Welcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")

    while True:
        choice = input("Please choose an option (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid input. Please enter a number between 1 and 4.")


def run_program():
    cars = initialize_cars()

    while True:
        choice = main_menu()

        if choice == "1":
            display_cars(cars)
        elif choice == "2":
            car_id = int(input("Enter the car ID you want to rent: "))
            print(rent_car(cars, car_id))
        elif choice == "3":
            car_id = int(input("Enter the car ID you want to return: "))
            days = int(input("How many days did you rent the car? "))
            print(return_car(cars, car_id, days))
        elif choice == "4":
            print("Exiting program.")
            break

if __name__ == "__main__":
    run_program()
