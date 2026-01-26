class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,newWidth):
        self.width = newWidth
    
    def set_height(self,newHeight):
        self.height = newHeight

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2 *self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width **2 + self.height ** 2) **.5

    def get_picture(self):
        # lines of *
        #end with \n 
        # IF >50 THEN 'Too big for picture'
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        shape = ''
        for i in range(self.height):
            shape += '*'*self.width + '\n'
        return shape
            

    def get_amount_inside(self,other):
        #self.width,self.height,other.width,other.height
        #self should be larger than other shape
        
        answer1 = 0
        answer2 = 0

        #check horizontal
        if self.height >= other.height: #can fit vertically
            answer1 = self.width // other.width
            #multiply by number of times it can fit vertically
            answer1 = answer1* (self.height//other.height)

        #check vertical
        if self.width >= other.width: #can fit horizontally
            answer2 = self.height // other.height
        #multiply by number of times it can fit horizontally
            answer2 = answer2 * (self.width//other.width)
        #print(answer1,answer2)
        if answer1 > answer2:
            return answer1
        else:
            return answer2

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

    def set_side(self,newSide):
        self.height = newSide
        self.width = newSide
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_width(self,newWidth):
        self.set_side(newWidth)
    
    def set_height(self,newHeight):
        self.set_side(newHeight)


        
#tests
print(Square(5))
print(Rectangle(3, 6).get_diagonal())
print(Rectangle(3, 51).get_picture())
print(Rectangle(15,10).get_amount_inside(Square(5)))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))
