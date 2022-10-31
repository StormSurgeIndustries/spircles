import turtle
import random
import canvasvg
import tkinter

turningrate = 0
movement = 0
root = turtle.Screen()
drawing = 1
def save():
    canvas = root.getcanvas()
    canvasvg.saveall("spircles.svg", canvas)
print("turning angle:")
try:
    turningrate = float(input())
    if turningrate == None:
        turningrate = random.randint(1, 360)
except:
    pass
    print("random")
    turningrate = random.randint(0, 360)
    print(turningrate)
print("size:")
forward = float(input())
print("spiral:")
try:
    spiral = float(input())
    if spiral == None:
        spiral = random.random()
except:
    pass
    spiral = (random.random() + random.randint(1,180))
    print(spiral)
root.screensize(canvwidth=4000, canvheight=3000)
turtle = turtle.Turtle(visible=False)
turtle.speed(speed=0)
turtle.hideturtle()
turtle.ht()
print(" ")
root.tracer(0, 0)
try:
    while drawing == 1:
        movement += 1
        if movement % 200 == 0:
            root.update()
        print("drawing. spiral:", spiral, "drawing step:", movement, "                     ", end = "\r")
        root.listen()
        root.onkey(save, "s")
        turtle.left(turningrate)
        turtle.forward(forward)
        turningrate += spiral
        spiral += (spiral /  turningrate)
except Exception as e:
    drawing = 0
    pass
    print("done. press enter to exit. error:", e)
    input()
    exit()
turtle.mainloop()
