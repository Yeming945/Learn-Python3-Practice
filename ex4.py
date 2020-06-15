""" 练习 4 变量和名字 """

cars = 100
space_in_car = 4.0  # 每辆汽车载客量
drivers = 30  # 司机数量
passengers = 90  # 乘客数量
cars_not_drivers = cars - drivers  # 没有司机的车的数量
cars_drivers = drivers
carpool_capacity = cars_drivers * space_in_car  # 总的载客量
average_passengers_per_car = passengers / cars_drivers  # 平均每辆车的乘客数量


print("There are", cars, "cars available.")
print("There ara only", drivers, "drivers available.")
print("There will be", cars_not_drivers, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
