#class creation --
from itertools import cycle


class vehicle:
    color = "red",
    engine = "Petrol"

#object creation --
bike = vehicle()
bike.color = "blue"
bike.engine = "Petrol"


car = vehicle()
car.color = "green"
car.engine = "Petrol"

Cycle = vehicle()
Cycle.color = "yellow"
Cycle.engine = "None"

print(bike.color)
print(bike.engine)
print(car.color)

