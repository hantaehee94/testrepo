import matplotlib.pyplot as plt
class Vehicle:
    
    color = "White"
    # Constructor
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    # Method1
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    # Method2
    def display_properties(self):
        print("Properties of the vehicle:")
        print("Color:", self.color)
        print( "Max Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

Vehicle1 = Vehicle(200, 20)
Vehicle1.assign_seating_capacity(5)
Vehicle1.display_properties()

Vehicle2 = Vehicle(180, 25)
Vehicle2.assign_seating_capacity(4)
Vehicle2.display_properties()
