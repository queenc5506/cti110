# CTI-110
# P4LAB1B - Initials
# Crystal Queen
# 10 April 2023
#
# ****************** Pseudocode *********************
# Allow user to import turtle
# Create letter C, assign to int_c
# Make int_c draw the letter C
# Complete the letter C
# Pen up
# Set position
# Make int_q draw the letter Q
# Complete the letter Q

import turtle
wn = turtle.Screen()
wn.title("CQ")

int_c = turtle.Turtle()
int_q = turtle.Turtle()
int_c.pensize(30)
int_c.color("red")

int_c.circle(95,-180)

int_q.penup()
int_q.setpos(60,-60)
int_q.pendown()
int_q.pensize(30)
int_q.color("black")

int_q.circle(100)
int_q.forward(40)
int_q.left(125)
int_q.forward(90)
int_q.backward(120)
