from random import randint


class Location:
    """
    A location class. Contains information about postoffice location
    """

    def __init__(self, city:str, postoffice:int):
        """
        Initialize new location
        """
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Class for delivery item description
    """
    def __init__(self, name:str, price:float):
        """
        Initialize a new item.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}. Price: {self.price}."


class Vehicle:
    """
    Class for delivery vehicles
    """
    def __init__(self, vehicleNo:int):
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:
    """
    Order class which contains all info about order and user
    """
    def __init__(self, user_name:str, city:str, postoffice:int, items:list, vehicle=None):
        self.orderId = randint(100000000, 999999999)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = vehicle
        print(f"Your order number is {self.orderId}.")

    def __str__(self):
        return f"Order: {[item.__str__() for item in self.items]}"

    def calculateAmount(self):
        return sum(item.price for item in self.items)

    def assignVehicle(self, vehicle:Vehicle):
        self.vehicle = vehicle


class LogisticSystem:

    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                vehicle.isAvailable = False
                order.assignVehicle(vehicle)
                self.orders.append(order)
                return
        return "There is no available vehicle to deliver an order."

    def trackOrder(self, orderId:int):
        for order in self.orders:
            if order.orderId == orderId:
                return f"Your order #{orderId} is sent to {order.location.city}." \
                       f" Total price: {order.calculateAmount()} UAH."
        return "No such order."