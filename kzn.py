class BMW():
    def engine(self):
        print("BMW engine started.")

    def speed(self):
        print("BMW accelerates smoothly.")

    def model(self):
        print("BMW is a luxury car.")


class Ferrari():
    def engine(self):
        print("Ferrari engine roars to life.") 

    def speed(self):
        print("Ferrari accelerates rapidly.")

    def model(self):
        print("Ferrari is a high-performance sports car.")


bmw_car = BMW()
ferrari_car = Ferrari()


for car in (bmw_car, ferrari_car):
    car.engine()
    car.speed()
    car.model()
    