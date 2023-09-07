import time 

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute function {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

class Engine:
    def __init__(self, cylinders:int, gears:list):
        """
        This is the constructor for the Engine class.

        :param cylinders: The number of cylinders in the engine.
        :type cylinders: int
        :param gears: The list of gears in the engine.
        :type gears: list
        """
        if not isinstance(cylinders, int):
            raise ValueError(f"Cylinders must be an {type(int())} not  {type(cylinders)}")
        if not isinstance(gears, list):
            raise ValueError(f"Cylinders must be an {type(list())} not  {type(gears)}")
        self.cylinders = cylinders
        self.gears = gears
    
    def start(self):
        """
        This method starts the engine.
        """
        print(f"Engine with {self.cylinders} cylinders is starting")

    def stop(self):
        """
        This method stops the engine.
        """
        print(f"Engine with {self.cylinders} cylinders is stopping")

class Car:
    def __init__(self, make:str, model:str, year:int, engine:Engine):
        if not isinstance(make, str):
            raise ValueError(f"Make must be an {type(str())} not a {type(make)}")
        if not isinstance(model, str):
            raise ValueError(f"Model must be an {type(str())} not a {type(model)}")
        if not isinstance(year, int):
            raise ValueError(f"Year must be an {type(int())} not a {type(year)}")
        if not isinstance(engine, Engine):
            raise ValueError(
                    f"Engine must be an instance of <class 'engine.Engine'> not {type(engine)}")
        self.make = make
        self.model = model 
        self.year = year 
        self.engine = engine
        self.current_gear = 0
    @time_it
    def start(self):
        print(f"Starting {self.make} of a year: {self.year} with {self.engine.cylinders} cylinder engine")
        self.engine.start()
    
    def stop(self):
        print(f"Stopping {self.make} of a year: {self.year} with {self.engine.cylinders} cylinder engine")
        self.engine.stop()

@time_it
def shift_gear(car:Car, gear:int):
    gears = car.engine.gears
    if gear in gears:
        car.current_gear = gear
    else:
        raise ValueError(f"Gear number: {gear} is not in {gears}")

@time_it  
def create_car(make, model, year, cylinders, gears):
    engine = Engine(cylinders, gears)
    car = Car(make, model, year, engine)
    return engine, car

cylinder_4 = Engine(4, [0,1,2,3,4,5])
car1 = Car("Toyota", "Supra", 1992, cylinder_4)
car1.start()
car1.stop()

cylinder_8 = Engine(8, [0,1,2,3,4,5,6])
car2 = Car("Ford", "F-150", 2022, cylinder_8)
car2.start()
shift_gear(car2, 1)
car2.stop()

engine1, car3 = create_car("Nissan", "Focus", 2003, 6, [0,1,2,3,4])

car3.start()
car3.stop()
