#imports
import turtle #turtle is a drawing library

"""
have a turtle draw squares on the screen
"""

# draw square loop to be used below
def draw_shape(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

# draw the image
def draw_art():
    window = turtle.Screen()
    window.bgcolor("darkblue")

    # create the turtle Mark using classes!!!
    mark = turtle.Turtle()
    mark.shape("turtle") #.shape exits within turtle.Turtle
    mark.color("yellow") #.color exits within turtle.Turtle
    mark.speed(15) #.speed exits within turtle.Turtle
    
    for i in range(1,37):
        draw_shape(mark)
        mark.right(10) #.right exits within turtle.Turtle
        
        
    # closes window on click
    window.exitonclick()
    
# run this at the end
draw_art()
