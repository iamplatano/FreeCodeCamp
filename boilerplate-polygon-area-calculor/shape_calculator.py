# Class for a Reactangle object
class Rectangle:
    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Set width and height methods
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Returns area
    def get_area(self):
        return self.width * self.height

    # Returns perimeter
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    # Returns diagonal distance
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    # Draws a picture made out of *
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = '{0:s}\n'.format("*" * self.width) * self.height
            return picture

    # Returns how many of the passed Rectangle objects could fit in
    def get_amount_inside(self, Rectangle):
        if self.height < Rectangle.height or self.width < Rectangle.width:
            return 0
        else:
            return self.height // Rectangle.height * self.width // Rectangle.width  # The number is the product of the ratios of width and height

    # String method
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


# Class of a Square, inherits Rectangle
class Square(Rectangle):
    # Constructor
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)
# Sets its side length

    def set_side(self, side):
        self.width = side
        self.height = side


# String method

    def __str__(self):
        return f'Square(side={self.width})'
