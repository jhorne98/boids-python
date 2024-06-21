from graphics import *

g_leftMargin = g_rightMargin = 50

class Boid:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

def main():
    boidList = [Boid(10,10,0.005,0)]

    win = GraphWin(title="Boids", width=200, height=200, autoflush=False)
    curBoid = boidList[0]
    c = Circle(Point(curBoid.x, curBoid.y), 5)
    c.draw(win)
    while(True):
        c.move(curBoid.dx, curBoid.dy)
        update()

if __name__ == "__main__":
    main()