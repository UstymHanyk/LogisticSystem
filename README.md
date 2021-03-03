# LogisticSystem
- The system can accept orders for delivery to a given destination;
- The order consists of a list of products. Each product has its own price, which is taken into account in the order;
- The user can track his order;
- Orders will be delivered by the transport available 
***
## UML diagram
![image](https://user-images.githubusercontent.com/25267338/109845059-68f6c800-7c55-11eb-8fb4-73ece2a8f0be.png)
1. Item - a class with which you can describe the product to be delivered;
2. Vehicle - displays the vehicle to which the delivery will be made, takes into account the availability of available transport;
3. Location - a simple class that simulates the address (city and branch of Ukrposhta);
4. Order - contains all the information about the order and the user;
5. LogisticsSystem - the main class that stores all information about users, orders and transportation. Has methods such as placeOrder (), trackOrder ().
***
## Examples
```commandline
>>> vehicles = [Vehicle(1), Vehicle(2)]

>>> logSystem = LogisticSystem(vehicles)

>>> my_items = [Item('book',110), Item('chupachups',44)]

>>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)

Your order number is 165488695.

>>> logSystem.placeOrder(my_order)

>>> logSystem.trackOrder(165488695)

Your order #165488695 is sent to Lviv. Total price: 154 UAH.


>>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]

>>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2)

Your order number is 234976475.

>>> logSystem.placeOrder(my_order2)

>>> logSystem.trackOrder(234976475)

Your order #234976475 is sent to Odessa. Total price: 164.33 UAH.


>>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]

>>> my_order3 = Order(Olesya, 'Kharkiv', 17, my_items3)

Your order number is 485932990.

>>> logSystem.placeOrder(my_order3)

There is no available vehicle to deliver an order.

>>> logSystem.trackOrder(485932990)

No such order.
```
