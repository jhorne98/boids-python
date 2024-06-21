from graphics import *
import math

g_leftMargin = 50
g_rightMargin = 750
g_topMargin = 50
g_bottomMargin = 550
g_turnFactor = 0.000002
g_maxSpeed = 0.01
g_minSpeed = 0.005
#g_margin = 50

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def main():
    boidList = [Boid(100,100,0.008,0.0001)]

    win = GraphWin(title="Boids", width=800, height=600, autoflush=False)
    curBoid = boidList[0]
    c = Circle(Point(curBoid.x, curBoid.y), 5)
    c.draw(win)
    while(True):
        if curBoid.x < g_leftMargin:
            curBoid.vx += g_turnFactor
        if curBoid.x > g_rightMargin:
            curBoid.vx -= g_turnFactor
        if curBoid.y > g_bottomMargin:
            curBoid.vy -= g_turnFactor
        if curBoid.y < g_topMargin:
            curBoid.vy += g_turnFactor

        curBoid.x += curBoid.vx
        curBoid.y += curBoid.vy

        speed = math.sqrt(curBoid.vx*curBoid.vx + curBoid.vy*curBoid.vy)
        if speed > g_maxSpeed:
            curBoid.vx = (curBoid.vx/speed)*g_maxSpeed
            curBoid.vy = (curBoid.vy/speed)*g_maxSpeed
        if speed < g_minSpeed:
            curBoid.vx = (curBoid.vx/speed)*g_minSpeed
            curBoid.vy = (curBoid.vy/speed)*g_minSpeed

        c.move(curBoid.vx, curBoid.vy)
        update()

if __name__ == "__main__":
    main()