"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zewei Xiang.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
#construct rose window
    window = rg.RoseWindow(400,400,'hello')
#crate first circle with color blue
    center1 = rg.Point(100,200)
    r=40
    circle1 = rg.Circle(center1,r)
    circle1.fill_color= 'green'
#draw the circle
    circle1.attach_to(window)
    window.render()
#stop the system 1 second
#    time.sleep(1)
# crate first circle with no color
    center2 = rg.Point(300, 200)
    r2 = 40
    circle2 = rg.Circle(center2, r2)
# draw the circle
    circle2.attach_to(window)
    window.render()
#disappear when click
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # construct rose window
    window = rg.RoseWindow(400, 400, 'hello')
    # crate a circle with color blue
    center1 = rg.Point(100, 200)
    r = 40
    circle1 = rg.Circle(center1, r)
    circle1.fill_color = 'blue'
    # draw the circle
    circle1.attach_to(window)
    window.render()
    #print everything
    print(circle1)
    #crate a rectangle
    point1 = rg.Point(300, 50)
    point2 = rg.Point(350, 150)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)
    window.render()
    #print everything
    print(rectangle)
    #close window when mousoe click
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    #open a window
    window=rg.RoseWindow()
    #define starting point and ending point
    sp1 =  rg.Point(100, 150)
    ep1 = rg.Point(200, 50)
    sp2 = rg.Point(150,100)
    ep2=rg.Point(0,0)
    #draw line
    line1=rg.Line(sp1,ep1)
    line2=rg.Line(sp2,ep2)
    line1.thickness = 5
    line1.attach_to(window)
    line2.attach_to(window)

    window.render()
    #print everything out
    mp1=rg.Line.get_midpoint(line1)
    print(mp1)
    print(mp1.x)
    print(mp1.y)

    window.close_on_mouse_click()


    # ------------------------------------------------------------------
    # done: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
