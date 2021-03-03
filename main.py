"""
A module with classes for the Logistic system implementation.
"""
from random import randint


class Location:
    """
    A location class. Contains information about postoffice location
    """

    def __init__(self, city: str, postoffice: int):
        """
        Initialize new location with properties: city, location
        """
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Class for delivery item description
    """

    def __init__(self, name: str, price: float):
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

    def __init__(self, vehicleNo: int):
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:
    """
    Order class which contains all info about order and user
    """

    def __init__(self, user_name: str, city: str, postoffice: int, items: list, vehicle=None):
        self.orderId = randint(100000000, 999999999)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = vehicle
        print(f"Your order number is {self.orderId}.")

    def __str__(self):
        return f"Order: {[item.__str__() for item in self.items]}"

    def calculateAmount(self):
        """
        Calculates the total price of all items in the order.
        """
        return sum(item.price for item in self.items)

    def assignVehicle(self, vehicle: Vehicle):
        """
        Assigns a vehicle object to the order's property vehicle
        """
        self.vehicle = vehicle


class LogisticSystem:
    """
    A class for logistic system with the capabilities of placing and tracking the order.
    """

    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        Places the order and assigns a vehicle using assignVehicle function from the order class.
        Returns "There is no available vehicle to deliver an order." if there isn't any vehicle available.
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                vehicle.isAvailable = False
                order.assignVehicle(vehicle)
                self.orders.append(order)
                return
        return "There is no available vehicle to deliver an order."

    def trackOrder(self, orderId: int):
        """
        Returns info about the specific order, including location, total price and order id.
        Returns "No such order." if the given orderId is incorrect, does not exist.
        """
        for order in self.orders:
            if order.orderId == orderId:
                return f"Your order #{orderId} is sent to {order.location.city}." \
                       f" Total price: {order.calculateAmount()} UAH."
        return "No such order."
