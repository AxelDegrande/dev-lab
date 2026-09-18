class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "off"

        def start(self):
            self.status = "running"
            print("Engine started")

        def stop(self):
            self.status = "off"
            print("Engine stopped")


    def drive(self):
        if self.engine.status == "running":
            print(f"Driving the {self.brand} {self.model}!")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Landcruiser")
car.drive()
car.engine.start()
car.drive()      
                        