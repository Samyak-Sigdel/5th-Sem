import math 
class Quadratic: 
    def __init__(self): 
        self.a = 0  
        self.b = 0 
        self.c = 0 
        self.x1 = 0 
        self.x2 = 0

def Input(self): 
    self.a = float(input("Enter for a: ")) 
    self.b = float(input("Enter for b: ")) 
    self.c = float(input("Enter for c: ")) 

def Calculate(self): 
    discriminant = self.b**2 - 4 * self.a * self.c 

    if discriminant > 0: 
        self.x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
        self.x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a) 
        
    elif discriminant == 0: 
        self.x1 = self.x2 = -self.b / (2 * self.a) 
    else: 
        real_part = -self.b / (2 * self.a) 
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * self.a) 
        self.x1 = complex(real_part, imaginary_part) 
        self.x2 = complex(real_part, -imaginary_part) 


def Display(self): 
    print(f"Root 1: {self.round_to_two_decimals(self.x1)}")
    print(f"Root 2: {self.round_to_two_decimals(self.x2)}") 
def round_to_two_decimals(self, num): 
    if isinstance(num, complex): 
        return complex(round(num.real, 2), round(num.imag, 2)) 
    else: 
         return round(num, 2) 
class Imain: 
    @staticmethod 
    def main(): 
        q = Quadratic() 
        q.Input() 
        q.Calculate() 
        q.Display() 

if __name__ == "__main__": 

    Imain.main()
