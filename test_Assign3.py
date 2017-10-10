'''Test animation and depth.
'''

from graphics import *
from math import *
import time
import frange

# def yUp(self):
#     """Set coordinates of window to run from (0,0) in the
#     lower-left corner and the window widthand height
#     in the upper left corner, so y increases upward."""
#     self.setCoords(0, 0, self.width, self.height)


def promptMouse(window_object, x, y, prompt):
    '''Temporarily place the prompt text at (x,y),
    and wait for and then return a mouse click.
    '''
    message = Text(Point(x, y), prompt)
    message.draw(window_object)
    pt = window_object.getMouse()
    message.undraw()
    return pt


def promptClose(window_object, x, y=None):
    '''Place a prompt to close the window at (x,y)
    or if y is None, in existing Text object x,
    and close after a mouse click.
    '''
    prompt = 'Click anywhere to quit.'
    if isinstance(x, Text):
        x.setText(prompt)
        window_object.getMouse()
    else:
        promptMouse(window_object, x, y, prompt)
    window_object.close()


def main():
    win = GraphWin('Sinusoid', 300, 300)
    win.setCoords(0, 0, win.width, win.height)

    # rect = Rectangle(Point(200, 90), Point(220, 100))
    # rect.setFill("blue")
    # rect.draw(win)
    #
    # cir1 = Circle(Point(40, 100), 25)
    # cir1.setFill("yellow")
    # cir1.draw(win)
    #
    # cir2 = Circle(Point(150, 125), 25)
    # cir2.setFill("red")
    # cir2.draw(win)

    pt1 = Point(0, 150)
    pt1.draw(win)

    ln2 = Line(pt1, Point(300, 150))
    ln2.draw(win)

    # x=[1,2,3,4,5,6,7,8,9,10]


    t = 0.05
    amplitude = 10


    for x in frange.frange(0,10,t/2):

        y = amplitude * math.sin((2*math.pi)*x)

        pt1.move(x, y)
        time.sleep(t/2)

        if pt1.getX() >= win.width:
            promptClose(win, win.getWidth() / 2, 20)
            break

    # for x in range(46):
    #     cir1.move(5, 0)
    #     time.sleep(.05)

    # for x in range(46):
    #     cir1.move(-5, 0)
    #     time.sleep(.05)

    # promptClose(win, win.getWidth() / 2, 20)


# main()

for x in range(1,11):

    sqrt((x**2)) * sin(sqrt((x**2)))
    sin(x**2) * cos(x**2)
    round(sin(x**20), 1)
    sqrt(x)
    10 * x**2 / 5
    abs(x - 2) * cos(x**2)
    tan(x**2)
