class Rectrangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return(self.length*self.width)

    def calculate_perimeter(self):
        return (2*(self.length+self.width))

rectrangle1=Rectrangle(10,20)
rectrangle2=Rectrangle(5,10)

print(f"Area of rectrangle with length: {rectrangle1.length} and width: {rectrangle1.width} is {rectrangle1.calculate_area()}")
print(f"Perimeter of rectrangle with length: {rectrangle1.length} and width: {rectrangle1.width} is {rectrangle1.calculate_perimeter()}")

print(f"Area of rectrangle with length: {rectrangle2.length} and width: {rectrangle2.width} is {rectrangle2.calculate_area()}")
print(f"Perimeter of rectrangle with length: {rectrangle2.length} and width: {rectrangle2.width} is {rectrangle2.calculate_perimeter()}")