from .paper import Paper
import random

class Shape():

    # Constructor for Shape
    def __init__(self, width=50, height=50, x=None, y=None, color="black"):
        """
        Creates a generic 'shape' which contains properties common to all
        shapes such as height, width, x y coordinates and colour.

        Args:
            width (int): The width of the shape. Defaults to 50.
            height (int): The height of the shape. Defaults to 50.
            x (int): The x position of the shape. If None, the x position will be the middle of the screen. Defaults to None.
            y (int): The y position of the shape. If None, the y position will be the middle of the screen. Defaults to None.
            color (string): The color of the shape. Defaults to "black"
        """
        if Paper.tk is None:
            raise Exception("A Paper object has not been created. There is nothing to draw on.")

        # Set some attributes
        self._height = height
        self._width = width
        self._color = color

        # Put the shape in the centre if no xy coords were given
        if x is None:
            self._x = (Paper.tk.paper_width/2) - (self._width/2)
        else:
            self._x = x
        if y is None:
            self._y = (Paper.tk.paper_height/2) - (self._height/2)
        else:
            self._y = y

    # This is an internal method not meant to be called by users
    # (It has a _ before the method name to show this)
    def _location(self):
        """
        Internal method used by the class to get the location
        of the shape. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """
        x1 = self._x
        y1 = self._y
        x2 = self._x + self._width
        y2 = self._y + self._height
        return [x1, y1, x2, y2]

    # Randomly generate what the shape looks like
    def randomize(self, smallest=20, largest=200):
        """
        Randomly generates width, height, position and colour for a shape. You can specify
        the smallest and largest random size that will be generated. If not specified, the
        generated shape will default to a random size between 20 and 200.

        Args:
            smallest (int): The smallest the shape can be. Defaults to 20
            largest (int): The largest the the shape can be. Defaults to 200.

        """
        self._width = random.randint(smallest, largest)
        self._height = random.randint(smallest, largest)

        self._x = random.randint(0, Paper.tk.paper_width - self._width)
        self._y = random.randint(0, Paper.tk.paper_height - self._height)

        self._color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Setters for Shape attributes
    def width(self, width):
        """
        Sets the width of the shape.

        Args:
            width (int): The width of the shape
        """
        self._width = width

    def height(self, height):
        """
        Sets the height of the shape.
        
        Args:
            height (int): The height of the shape.
        """
        self._height = height

    def x(self, x):
        """
        Sets the x position of the shape
        
        Args:
            x (int): The x position for the shape.
        """
        self._x = x

    def y(self, y):
        """
        Sets the y position of the shape
        
        Args:
            y (int): The y position for the shape.
        """
        self._y = y
        
    def color(self, color):
        """
        Sets the colour of the shape
        
        Args:
            color (string): The color of the shape.
        """
        self._color = color