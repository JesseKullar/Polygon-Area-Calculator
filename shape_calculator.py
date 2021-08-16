class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_picture(self):
        error = 'Too big for picture.'
        if (self.height > 50) or (self.width > 50):
            return error
        pic = ''
        for i in range(self.height):
            pic += '*' * self.width + '\n'
        return pic

    def __str__(self):
        name = str(self.__class__.__name__).title() + '(width=' + str(self.width) +\
              ', height=' + str(self.height) + ')'
        return name

    def get_amount_inside(self, shape):
        count = int()
        remain_area = self.get_area()
        while remain_area >= shape.get_area():
            count += 1
            remain_area -= shape.get_area()
        return count



class Square(Rectangle):

    def __init__(self, side):
        super()
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        name = str(self.__class__.__name__).title() + '(side=' + \
               str(self.width) +')'
        return name
