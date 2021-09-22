from turtle import Turtle, width
import random
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("red")
        self.create_food()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)

    def create_food(self):
        self.random_x = random.randint(-280,280)
        self.random_y = random.randint(-280,280)
        self.goto(self.random_x,self.random_y)