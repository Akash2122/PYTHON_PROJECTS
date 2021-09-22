from turtle import Turtle, left

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self) -> None:
        self.segments = []
        self.Create_Snake()
        self.head = self.segments[0]

    def Create_Snake(self):     
        
        for position in STARTING_POSITIONS:
            self.one_segment(position)
            

    def one_segment(self,position):
            segment = Turtle(shape="circle")
            segment.color("white")
            segment.pu()
            segment.goto(position)
            self.segments.append(segment)

    def extend_segment(self):
            self.one_segment(self.segments[-1].position())

    def move_snake(self):
        for i in range ((len(self.segments)-1),0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)