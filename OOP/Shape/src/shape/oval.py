from .paper import Paper
from .shape import Shape

# Oval class is a subclass of Shape
class Oval(Shape):

    def draw(self):
        """
        Draws an oval on the canvas. The properties of the oval
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2 = self._location()

        # Draw the oval
        Paper.tk.canvas.create_oval(x1, y1, x2, y2, fill=self._color)