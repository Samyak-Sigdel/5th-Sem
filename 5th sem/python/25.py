class Rectangle: 
    def __init__(self, length, breadth): 
        self.length = length 
        self.breadth = breadth 
        self.area = 0 
    def computeArea(self): 
          self.area = self.length * self.breadth 
    def displayArea(self): 
        print(f"Area of the rectangle : {self.area}") 
def main(): 
    rect1 = Rectangle(5, 10) 
    rect2 = Rectangle(7, 8) 
    rect1.computeArea() 
    rect2.computeArea() 
    rect1.displayArea() 
    rect2.displayArea() 
    if rect1.area > rect2.area: 
        print(f"The rectangle 1 has a larger area: {rect1.area}") 
    elif rect2.area > rect1.area: 
        print(f"The rectangle 2 has a larger area") 
    else: 
        print("Both rectangles have the same area.")
if __name__ == "__main__": 
    main()
