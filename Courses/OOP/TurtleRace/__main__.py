# Import Turtle class.
from turtle import Turtle
# randint function from the random module generates random integers.
from random import randint

if __name__ == '__main__':
    # Create an instance of a Turtle object.
    laura = Turtle()
    # Use color and shape methods to customise attributes.
    laura.color('red')
    laura.shape('turtle')
    # Stop drawing.
    laura.penup()
    # Move to a location.
    laura.goto(-160, 100)
    # Draw a line.
    laura.pendown()

    # Create 3 more instances of a Turtle object.
    rik = Turtle()
    rik.color('green')
    rik.shape('turtle')
    rik.penup()
    rik.goto(-160, 70)
    rik.pendown()

    lauren = Turtle()
    lauren.color('blue')
    lauren.shape('turtle')
    lauren.penup()
    lauren.goto(-160, 40)
    lauren.pendown()

    carrieanne = Turtle()
    carrieanne.color('brown')
    carrieanne.shape('turtle')
    carrieanne.penup()
    carrieanne.goto(-160, 10)
    carrieanne.pendown()

    # Each turtle will move forward by a random number of pixels.
    for movement in range(100):
        laura.forward(randint(1, 5))
        rik.forward(randint(1, 5))
        lauren.forward(randint(1, 5))
        carrieanne.forward(randint(1, 5))

    # See the output.
    input("Press Enter to close")