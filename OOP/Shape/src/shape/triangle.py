from .paper import Paper
from .shape import Shape
import random

# Triangle class is a subclass of Shape
class Triangle(Shape):
    
    # Every constructor parameter has a default setting
    # e.g. color defaults to "black" but you can override this
    def __init__(self, x1=0, y1=0, x2=20, y2=0, x3=20, y3=20, color="black"):
        """
        Overrides the Shape constructor because triangles require three
        coordinate points to be drawn, unlike rectangles and ovals.

        Args:
            x1 (int): The x position of the coordinate 1. Defaults to 0.
            y1 (int): The y position of the coordinate 1. Defaults to 0.
            x2 (int): The x position of the coordinate 2. Defaults to 20.
            y2 (int): The y position of the coordinate 2. Defaults to 0.
            x3 (int): The x position of the coordinate 3. Defaults to 20.
            y4 (int): The y position of the coordinate 3. Defaults to 20.
            color (string): The color of the shape. Defaults to "black"
        """
        # call the Shape constructor
        super().__init__(color=color)

        # Remove height and width attributes which make no sense for a triangle
        # (triangles are drawn via 3 xy coordinates)
        del self._height
        del self._width

        # Instead add three coordinate attributes
        self.__x = x1
        self.__y = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    def __location(self):
        """
        Internal method used by the class to get the location
        of the triangle. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """
        return [self.__x, self.__y, self.__x2, self.__y2, self.__x3, self.__y3]

    def draw(self):
        """
        Draws a triangle on the canvas. The properties of the triangle
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2, x3, y3 = self.__location()
        # Draw a triangle
        Paper.tk.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self.color)

    def randomize(self):
        """
        Randomly chooses the location of all 3 triangle points as well
        as the colour of the triangle
        """
        # Randomly choose all the points of the triangle
        self.__x = random.randint(0, Paper.tk.paper_width)
        self.__y = random.randint(0, Paper.tk.paper_height)
        self.__x2 = random.randint(0, Paper.tk.paper_width)
        self.__y2 = random.randint(0, Paper.tk.paper_height)
        self.__x3 = random.randint(0, Paper.tk.paper_width)
        self.__y3 = random.randint(0, Paper.tk.paper_height)

        # Randomly choose a colour of this triangle
        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Change the behaviour of set_width and set_height methods for a triangle
    # because triangles are not drawn in the same way
    
    def width(self, width):
        """
        Overrides the setter method for width

        Args:
            width (int): The width of the shape
        """
        raise Exception("Width cannot be defined for Triangle objects")

    def height(self, height):
        """
        Overrides the setter method for height

        Args:
            height (int): The height of the shape
        """
        raise Exception("Height cannot be defined for Triangle objects")