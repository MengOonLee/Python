# This code requires Python 3 and tkinter (which is usually installed by default)
# This code will NOT work on trinket.io as the tkinter module is not supported
# Raspberry Pi Foundation 2020
# CC-BY-SA 4.0

try:
    from tkinter import Tk, Canvas, BOTH   
except ImportError:
    raise Exception("tkinter did not import successfully - check you are running Python 3 and that tkinter is available.")

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