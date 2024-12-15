class Vehicle:

    def move(self):
   
        raise NotImplementedError("Expected to be overridden by subclasses")

class Boat(Vehicle):
 
    def move(self):
        return "Sailing"


class Car(Vehicle):
   
    def move(self):
        return "Driving"


class Plane(Vehicle):

    def move(self):
        return "Flying"
    

class Bicycle(Vehicle):

    def move(self):
        return "Pedaling"



def show_movement(vehicle):

    print(f"{vehicle.__class__.__name__}: {vehicle.move()}")


if __name__ == "__main__":
    boat = Boat()
    car = Car()
    plane = Plane()    
    bicycle = Bicycle()
  
    vehicles = [boat, car, plane, bicycle]
    for vehicle in vehicles:
        show_movement(vehicle)
