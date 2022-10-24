from abc import ABC, abstractmethod


# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers


class FibonacciNumbers:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):

        if self.num > 0:
            self.num -= 1
            self.a, self.b = self.b, self.a + self.b
            return self.a
        else:
            raise StopIteration


fib = FibonacciNumbers(10)
print(type(fib))  # <class '__main__.FibonacciNumbers'>
for i in fib:
    print(i)


# 2.* Implement generator for Fibonacci numbers

def generator_fib(num):
    a = 0
    b = 1
    while num + 1 > 0:
        num -= 1
        yield a
        a, b = b, a + b


gen_fib = generator_fib(10)
print(type(gen_fib))  # <class 'generator'>
for fib in gen_fib:
    print(fib)

# 3. Write generator expression that returns square numbers of integers from 0 to 10

sqr_0_10 = (i * i for i in range(11))
print(type(sqr_0_10))  # <class 'generator'>
for x in sqr_0_10:
    print(x)


# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


# and create an HPLaptop class by using your interface.


class HPLaptop(Laptop):

    def screen(self):
        print("Screen")

    def keyboard(self):
        print("Keyboard")

    def touchpad(self):
        print("touchpad")

    def webcam(self):
        print("webcam")

    def ports(self):
        print("ports")

    # def dynamics(self):
    #     print("dynamics")


hp = HPLaptop()  # TypeError: Can't instantiate abstract class HPLaptop with abstract method dynamics


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.


class Car(ABC):

    def drive(self):
        print("the car is coming")

    def stop(self):
        print("the car stops")

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
