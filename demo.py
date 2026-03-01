"""
Aqua Spiral - A mesmerizing turtle graphics pattern
Creates a spiral of aqua circles against a black background
"""

import turtle as t

# Setup
t.speed(0)           # Fastest speed
t.color("aqua")      # Beautiful aqua color
t.bgcolor("black")   # Dark background for contrast
t.hideturtle()       # Hide the turtle cursor

# Draw the spiral pattern
for i in range(170):          # 170 circles
    t.circle(i - 5)           # Gradually increasing radius
    t.left(5)                 # Rotate 5 degrees each time

# Keep window open
t.done()
