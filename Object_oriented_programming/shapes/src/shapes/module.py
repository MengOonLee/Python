# This code requires Python 3 and tkinter (which is usually installed by default)
# This code will NOT work on trinket.io as the tkinter module is not supported
# Raspberry Pi Foundation 2020
# CC-BY-SA 4.0

try:
    from tkinter import Tk, Canvas, BOTH   
except ImportError:
    raise Exception("tkinter did not import successfully - check you are running Python 3 and that tkinter is available.")

import random

class Paper():
    
    # the tk object which will be used by the shapes
    tk = None
    # author (str): Author of the display. Default to MengOonLee.
    author = "MengOonLee"
    # width (int): The width of the display. Default to 600.
    width = 600
    # height (int): The height of the display. Default to 600.
    height = 600
            
    @staticmethod
    def info():
        print("Made using the OOP creator (c) me")
     
    @classmethod
    def create(cls):
        """
        Create a Paper object which is required to draw shapes onto.
        It is only possible to create 1 Paper object.
        
        Returns:
            Paper: A Paper object
        """
        if cls.tk is not None:
            raise Exception("Error: Paper has already been created, there can be only one.")
        try:
            cls.tk = Tk()
            # Set some attributes
            cls.tk.title("Drawing shapes")
            cls.tk.geometry(str(cls.width) + "x" + str(cls.height))
            cls.tk.paper_width = cls.width
            cls.tk.paper_height = cls.height
            # Create a tkinter canvas object to draw on
            cls.tk.canvas = Canvas(cls.tk)
            cls.tk.canvas.pack(fill=BOTH, expand=1)
        except ValueError:
            raise Exception("Error: could not instantiate tkinter object")
            
    @classmethod
    def display(cls):
        """
        Displays the paper
        """
        cls.tk.mainloop()
        print("Thank you for drawing")
        print("Created by " + cls.author)

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

    # Getters and setters for Shape attributes
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        """
        Sets the width of the shape.

        Args:
            width (int): The width of the shape
        """
        self._width = width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        """
        Sets the height of the shape.
        
        Args:
            height (int): The height of the shape.
        """
        self._height = height

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        """
        Sets the x position of the shape
        
        Args:
            x (int): The x position for the shape.
        """
        self._x = x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        """
        Sets the y position of the shape
        
        Args:
            y (int): The y position for the shape.
        """
        self._y = y
        
    @property
    def color(self):
        """
        Returns the colour of the shape
        
        Returns:
            color (string): The color of the shape
        """
        return self._color
        
    @color.setter
    def color(self, color):
        """
        Sets the colour of the shape
        
        Args:
            color (string): The color of the shape.
        """
        self._color = color

# Rectangle class is a subclass of Shape
class Rectangle(Shape):

    # This is how to draw a rectangle
    def draw(self):
        """
        Draws a rectangle on the canvas. The properties of the rectangle
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2 = self._location()

        # Draw the rectangle
        Paper.tk.canvas.create_rectangle(x1, y1, x2, y2, fill=self._color)

class Oval(Shape):

    def draw(self):
        """
        Draws an oval on the canvas. The properties of the oval
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2 = self._location()

        # Draw the oval
        Paper.tk.canvas.create_oval(x1, y1, x2, y2, fill=self._color)

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
        super().__init__()
        self.__color=color

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
        Paper.tk.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self.__color)

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
        self.__color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Change the behaviour of set_width and set_height methods for a triangle
    # because triangles are not drawn in the same way
    
    @property
    def width(self):
       return self.__width
    
    @width.setter
    def width(self, width):
        """
        Overrides the setter method for width

        Args:
            width (int): The width of the shape
        """
        raise Exception("Width cannot be defined for Triangle objects")

    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, height):
        """
        Overrides the setter method for height

        Args:
            height (int): The height of the shape
        """
        raise Exception("Height cannot be defined for Triangle objects")

# This if statement means
# "if you run this file (rather than importing it), run this demo script"
if __name__ == "__main__":

    Paper.info()
    Paper.create()
    
    # Random size and location triangle
    tri = Triangle()
    tri.randomize()
    tri.draw()

    # Specific size and location rectangle
    rect = Rectangle(height=40, width=90, x=110, y=20, color="yellow")
    rect.draw()

    # Default oval
    oval = Oval()
    oval.draw()

    # Oval with setters
    oval2 = Oval()
    oval2.height = 200
    oval2.width = 100
    oval2.color = "fuchsia"
    oval2.x = 30
    oval2.y = 90
    oval2.draw()

    Paper.display()