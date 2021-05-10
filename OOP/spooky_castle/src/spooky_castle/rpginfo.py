class RPGInfo():
    
    author = "Anonymous"
    
    @staticmethod
    def info():
        print("The Spooky Castle")
        print("Made using the OOP RPG game creator (c) me")
        
    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
