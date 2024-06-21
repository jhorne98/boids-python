from graphics import *
import math, random

g_width = 800
g_height = 600

g_leftMargin = 50
g_rightMargin = g_width - 50
g_topMargin = 50
g_bottomMargin = g_height - 50

g_turnFactor = 0.000002
g_avoidFactor = 0.1
g_maxSpeed = 0.01
g_minSpeed = 0.005

g_numBoids = 5

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.c = Circle(Point(x, y), 5)

def main():
    boidList = []
    for _n in range(0, g_numBoids):
        x = random.randint(g_leftMargin, g_rightMargin)
        y = random.randint(g_topMargin, g_bottomMargin)
        vx = random.uniform(g_minSpeed, g_maxSpeed)
        vy = random.uniform(g_minSpeed, g_maxSpeed)
        boidList.append(Boid(x,y,vx,vy))

    #boidList = [Boid(100,100,0.008,0.0001), Boid(150,150,0.008,0.001)]

    win = GraphWin(title="Boids", width=g_width, height=g_height, autoflush=False)
    for boid in boidList:
        boid.c.draw(win)

    while(True):
        for curBoid in boidList:
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

            curBoid.c.move(curBoid.vx, curBoid.vy)
        update()

if __name__ == "__main__":
    main()