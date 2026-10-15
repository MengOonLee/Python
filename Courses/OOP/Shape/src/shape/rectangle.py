from .paper import Paper
from .shape import Shape

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