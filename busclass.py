class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
         return self.seating_capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        final_fare = total_fare + (0.1 * total_fare)
        return final_fare
    
bus1 = Bus("School Volvo", 50)
print(f"Total Bus fare is: Rs {bus1.fare()}")