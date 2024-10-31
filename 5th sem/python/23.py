class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.area = 0
def Set(self):
    self.length = int(input("Enter length of the rectangle: "))
    self.breadth = int(input("Enter breadth of the rectangle: "))

def Calculate(self):
    self.area = self.length * self.breadth
    print(f"Area of the rectangle: {self.area}")

class imain:

    def main():
        r = Rectangle()
        r.Set()
        r.Calculate()

if __name__ == "__main__":
    imain.main()