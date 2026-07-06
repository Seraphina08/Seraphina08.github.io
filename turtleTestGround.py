import turtle
##This makes a star shape. The turtle will draw a star until it returns to the starting point.
turtle.shape('turtle') # there are various shapes available.
turtle.color('purple')
turtle.fillcolor('pink')
turtle.begin_fill()
while True: # the turtle will draw a star until it returns to the starting point
    turtle.forward(200)
    turtle.left(144) # 144 makes the perfect 5 point star. 180 makes a straight line, 90 makes a square, 60 makes a triangle, 120 makes a diamond.
    if abs(turtle.pos()) < 1: # a way to know when the turtle is back to the starting point
        break
    turtle.end_fill()
# ##for steps in range(100):
#     for c in ('red', 'blue', 'yellow', 'green', 'purple', 'pink'): 
#         turtle.color(c)
#         turtle.forward(steps)
#         turtle.left(90)

turtle.done() ## apparently if you dont add (), the turtle window will close immediately after the turtle is done drawing.