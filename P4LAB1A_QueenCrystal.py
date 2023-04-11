# CTI-110
# P4LAB1A - Shapes
# Crystal Queen
# 10 April 2023
#
# ****************** Pseudocode *********************
# Allow user to import turtle
# Create square, assign to squ
# Create triangle, assign to tri
# Executes the body with i = 0, then 1, then 2, then 3
# Make squ draw square
# Complete the square
# Turn squ right
# Executes the body with i = 0, then 1, then 2
# Make tri draw triangle
# Complete the triangle

import turtle
squ = turtle.Turtle()
tri = turtle.Turtle()

for i in [0,1,2,3]:
    squ.forward(50)
    squ.left(90)

squ.right(180)

for i in [0,1,2]:
    tri.forward(80)
    tri.left(120)
