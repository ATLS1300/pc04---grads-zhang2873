"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Amy Zhang

********* HEY, READ THIS FIRST **********

This is a description of the code that is written out below. This script is start code for PC04 + beyond. 
It imports random and math libraries along with the turtle libraries.
You should add your name(s), to line 4, and replace this description with one that describes what your code does!
(Hint: what patterns does it make? should it evoke any emotions?
 
 This pattern makes one spirograph of circles
 that has random colors every time the code runs, 
 a wheel of arrow stamps that are blue, and a
 parametric equation that has two iterations/random scaling.

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 
panel.bgcolor("black")



# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

para = turtle.Turtle()
arrow = turtle.Turtle()
circle = turtle.Turtle()
para.speed(15)
arrow.speed(10)
circle.speed(15)


para.color((57,255,20))

para.up()

#copy code from [https://canvas.colorado.edu/courses/75648/pages/parametric-patterns] for funky spiral

a = random.randint(25, 40) #random constant for equation, this is a multiplier

b = random.randint(20, 35) #random constant for equation, this is a multiplier

scale = random.randint(30, 100) #gets bigger or smaller in scale
iterate = 2

ANGLES = range(0,180) 
ANGLES2 = range(180,360)

for i in range(iterate):
   
   for angle in ANGLES:   
        angle = math.radians(angle)
    
        X = angle - 1.6*math.cos(a*angle)

        Y = angle - 1.6*math.cos(b*angle)

        X*=scale 
        Y*=scale
        para.down() 
        para.goto(X,Y)
        
   for angle in ANGLES2:
        angle = math.radians(angle)
    
        X = angle - 3.2*math.cos(a*angle)

        Y = angle - 3.2*math.cos(b*angle)

        X*=scale
   
        Y*=scale
        para.down() 
        para.goto(X,Y)
        
   a = -a * iterate
   b = -b * iterate
   para.color((225,255,20)) 
para.up()

arrow.goto(-100,-100)
arrows = 19
arrow.down()
arrow.shape("arrow")
arrow.color('blue')

for i in range(arrows):
    
    arrow.forward(50)
    arrow.stamp()
    arrow.backward(50)
    arrow.right(20)
    
#code below built from Taylor Dupuy's pseudocode
r= random.randint(0, 255)
g= random.randint(0, 255)
b= random.randint(0, 255)
rgb= [r, g, b]

angleNew= 10
numint= int(360/angleNew)
circleAngle= 30
circleRadius= 25
innerRadius= 2

for i in range(numint):
    circle.goto(-150,150)
    circle.color(rgb)
    circle.forward(innerRadius)
    circle.right(circleAngle)
    circle.circle(circleRadius)
    

#panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
