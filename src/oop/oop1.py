# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #This is the base class of all other classes
    def __init__(self):
        pass

class FlightVehicle(Vehicle): # Base class for starships and airplanes
    pass

class Starship(FlightVehicle):
    pass

class GroundVehicle(Vehicle): #base class for cars and motorcycles
    pass

class Airplane(FlightVehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
