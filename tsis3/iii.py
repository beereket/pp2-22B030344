class InputOutputString:
    def __init__(self):
        self.s=""
    
    def get_string(self):
        self.s=input("Enter a string: ")
    
    def print_string(self):
        print(self.s.upper())

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width= width
        
    def area(self):
        return (self.length * self.width)

class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f'{Point(self.x,self.y)}')
    def move(self, delta_x, delta_y):
        self.x+=delta_x
        self.y+=delta_y
    def dist(self, end_point):
        dist_x=self.x-end_point.x
        dist_y=self.y-end_point.y
        return (dist_x**2+dist_y**2)**0.5
    
class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to the account of {self.owner}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account of {self.owner}.")




is_prime = lambda x: all(x % i != 0 for i in range(2, x**0.5))
prime_numbers = list(filter(is_prime, numbers))
