# Parent Class
class Vehicle:
    brand = "Honda"
    color = "White"

# Child Class
class Car(Vehicle):
    model = "City"

    def show(self):
        print("Brand :", self.brand)
        print("Color :", self.color)
        print("Model :", self.model)


# Create Object of Car Class
c1 = Car()
c1.show()