"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 10) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.width(3)
    
    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    # bob.fd(radius)
    bob.goto(radius, 0)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    bob.circle(radius, extent=90)

    bob.pencolor('red')
    bob.fillcolor("blue")
    bob.begin_fill()

    square(bob, radius)
    bob.end_fill()
    bob.speed(10)
    polygon(bob, 8, radius)

    # wait for the user to close the window
    turtle.mainloop()


# turtle.forward(distance)：向前移动指定距离
# turtle.backward(distance)：向后移动指定距离
# turtle.left(angle)：向左转动指定角度
# turtle.right(angle)：向右转动指定角度
# turtle.penup()：抬起笔，移动不绘制
# turtle.pendown()：落下笔，移动时绘制
# turtle.pencolor(color)：设置笔的颜色
# turtle.fillcolor(color)：设置填充颜色
# turtle.pensize(width)：设置笔的宽度
# turtle.speed(speed)：设置绘制速度
# turtle.goto(x, y)：移动到指定的位置
# turtle.circle(radius, extent=None)：绘制指定半径和角度的圆
