"""
Animated version - Colors change as circles grow!
"""

import turtle as t
import random

t.speed(0)
t.bgcolor("black")
t.hideturtle()

colors = ["aqua", "cyan", "blue", "purple", "pink", "white"]

for i in range(200):
    # Change color every 20 circles
    color_index = (i // 20) % len(colors)
    t.color(colors[color_index])
    
    t.circle(i - 10)
    t.left(7)

t.done()
