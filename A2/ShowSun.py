# ShowSun.py
# Cindy Zhang
# 15th November 2018

"""
A module to draw colored sun.
"""

from simpleGraphics import*

def DrawSun(x,y,r,c1,c2,c3):
    """
    Draws a sun in the current window with center (x,y), and radius r.
   
    c1, c2, and c3 are rgb arrays that specify the three ray colors
    c1 specifies the color of Rays 1, 4, 7, 10, and 13
    c2 specifies the color of Rays 2, 5, 8, 11, and 14
    c3 specifies the color of Rays 3, 6, 9, 12, and 15

    Preconditions: x,y, and r are float or int, r is positive. color
    is an rgb array and stroke is a nonnegative float or int.
    
    """
    # Function Body
    DrawStar(x,y,r,c1,stroke=0)
    DrawStar(x,y,r,c3,stroke=0,rotate=120)
    DrawStar(x,y,r,c2,stroke=0,rotate=240)
    DrawDisk(x,y,r*alpha,color=YELLOW,stroke=0)
    
    
#Application Script 
if __name__ == '__main__':
    """
    docstring in the required style
    """
    r = 5.
    x = 0.
    y = 0.
    alpha = .62
    # My chosen Ray colors
    c1 = MAGENTA
    c2 = CYAN
    c3 = ORANGE
    # Figure 1: A Single sun
    MakeWindow(6,bgcolor=BLACK)
    DrawSun(x,y,r,c1,c3,c2)
    # Figure 2: A nesting
    MakeWindow(6,bgcolor=BLACK)
    DrawSun(x,y,r,c1,c3,c2) #Sun 1
    r=alpha *r
    DrawSun(x,y,r,c2,c1,c3) #Sun 2
    r=alpha*r
    DrawSun(x,y,r,c3,c2,c1) #Sun3
    r=alpha*r
    DrawSun(x,y,r,c1,c3,c2) #Sun4
    r=alpha*r
    DrawSun(x,y,r,c2,c1,c3) #Sun5
    r=alpha*r
    DrawSun(x,y,r,c3,c2,c1) #Sun6
    
    ShowWindow()
