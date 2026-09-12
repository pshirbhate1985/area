class area:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        return self.length*self.width
new_rectangle=area(100,50)
print("dimensions of rectangle : length = %d and width = %d"%(new_rectangle.length,new_rectangle.width))
print(" total area of rectangle = ",new_rectangle.rectangle_area())