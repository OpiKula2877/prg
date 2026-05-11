from vehicle import Vehicle

class Bugatti(Vehicle):
    
    def whoami(self):
        return "I am a Bugatti – the fastest production car in the world!"
    
    def max_speed(self, speed):
        return f"My maximum speed is {speed} km/h."
    
    def fuel(self, f):  
        return f"My fuel type is {f}."
    
my_car = Bugatti()

print(my_car.whoami())
print(my_car.max_speed(500))
print(my_car.fuel("Diesel"))