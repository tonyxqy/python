"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 90)
    koch(t, m)
    rt(t, 90)
    koch(t, m)
    rt(t, 90)
    koch(t, m)
    koch(t, m)
    lt(t, 90)
    koch(t, m)
    lt(t, 90)
    koch(t, m)
    rt(t, 90)
    koch(t, m)
def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(1):
        koch(t, n)
        lt(t, 90)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = 0
bob.y = -150
bob.redraw()

snowflake(bob, 300)

world.mainloop()