# class TemperatureSensor:
#     def __init__(self, temperature=0):
#         self.__temperature = 0
#         self.set_temperature(temperature)
#
#     def get_temperature(self):
#         return self.__temperature
#
#     def get_temperature_fahrenheit(self):
#         return self.__temperature * 9 / 5 + 32
#
#     def set_temperature(self, value):
#         if -100 <= value <= 100:
#             self.__temperature = value
#         else:
#             print("Температура должна быть от -100 до 100")
#
#
# sensor = TemperatureSensor(25)
# print(sensor.get_temperature())
# print(sensor.get_temperature_fahrenheit())

#2
# class PasswordManager:
#     def __init__(self, password):
#         self.__password = None
#         self.set_password(password)
#
#     def set_password(self, pwd):
#         if len(pwd) > 6:
#             self.__password = pwd
#         else:
#             print("Пароль должен быть длиннее 6 символов")
#
#     def _check_password(self, pwd):  # protected
#         return self.__password == pwd
#
#     def change_password(self, old, new):
#         if not self._check_password(old):
#             print("Старый пароль неверный")
#             return
#
#         if len(new) <= 6:
#             print("Новый пароль слишком короткий")
#             return
#
#         self.__password = new
#         print("Пароль успешно изменён")
#
#
# pm = PasswordManager("mypassword")
# pm.change_password("mypassword", "newsecurepass")
# pm.change_password("wrong", "12345678")

#3
# class User:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password
#
#     def check_password(self, pwd):
#         return self.__password == pwd
#
#     def get_username(self):
#         return self.__username
#
#     def change_password(self, old, new):
#         if self.check_password(old) and len(new) > 6:
#             self.__password = new
#             print("Пароль изменён")
#         else:
#             print("Ошибка смены пароля")
#
#
# class Admin(User):
#     def reset_password(self, user, new_password):
#         if len(new_password) > 6:
#             user.change_password(user._User__password, new_password)
#         else:
#             print("Пароль слишком короткий")
#
#
# user1 = User("Ivan", "password123")
# admin = Admin("Admin", "adminpass")
#
# admin.reset_password(user1, "newsecurepass")
# print(user1.check_password("newsecurepass"))

#4
class Client:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, car_type):
        self.car_type = car_type


class Order:
    def __init__(self, client, address, car, price):
        self.client = client
        self.address = address
        self.car = car
        self.__price = price  # инкапсуляция

    def change_address(self, new_address):
        self.address = new_address

    def change_car(self, new_car):
        self.car = new_car

    def get_price(self):
        return self.__price


class TaxiSystem:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)

    def show_orders(self):
        for order in self.orders:
            print(order.client.name, order.address, order.car.car_type, order.get_price())

client1 = Client("Alex")
car1 = Car("Premium")
order1 = Order(client1, "Main Street 10", car1, 250)

system = TaxiSystem()
system.add_order(order1)
system.show_orders()