# Use Paper, Triangle, Oval and Rectangle classes for the shapes file.
from shapes import Paper, Triangle, Rectangle, Oval

Paper.info()
Paper.width = 500
Paper.height = 500
# Create an instance of a Paper object.
Paper.create()
# Create an instance of an object.
rect = Rectangle()
# Use setters methods to set values.
rect.x = 100
rect.y = 100
rect.width = 200
rect.height = 100
rect.color = "blue"
# Use draw method to draw.
rect.draw()

# Create an instance of an object.
oval = Oval()
# Call randomize method choose a value for each attributes.
oval.randomize()
# Use draw method to draw.
oval.draw()

# Create an instance of an object.
tri = Triangle(5, 5, 100, 5, 100, 200)
# Call randomize method choose a value for each attributes.
tri.randomize()
# Use draw method to draw.
tri.draw()

# Use display method of the Paper object.
Paper.display()