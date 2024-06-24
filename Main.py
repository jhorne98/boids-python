from graphics import *
import math, random

g_width = 800.0
g_height = 600.0

g_margin = 75.0
g_leftMargin = g_margin
g_rightMargin = g_width - g_margin
g_topMargin = g_margin
g_bottomMargin = g_height - g_margin

g_turnFactor = 0.0005
g_avoidFactor = 0.00005
g_matchingFactor = 0.00005
g_centeringFactor = 0.0000007
g_maxSpeed = 0.2
g_minSpeed = 0.05

g_protectedRange = 5
g_visibleRange = 100

g_numBoids = 40

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.c = Circle(Point(x, y), 3)
        self.vec = Line(Point(x, y), Point(vx, vy))

    def distance(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))


def main():
    # initialize the boidList with random positions/velocities
    boidList = []
    for _n in range(0, g_numBoids):
        x = random.uniform(g_leftMargin, g_rightMargin)
        y = random.uniform(g_topMargin, g_bottomMargin)
        vx = random.uniform(-g_minSpeed, g_maxSpeed)
        vy = random.uniform(-g_minSpeed, g_maxSpeed)
        boidList.append(Boid(x,y,vx,vy))

    # start the graphics window, draw the boids
    win = GraphWin(title="Boids", width=g_width, height=g_height, autoflush=False)
    for boid in boidList:
        boid.c.draw(win)

    while(True):
        for curBoid in boidList:
            curBoid.vec.undraw()

            closeDx = closeDy = 0.0

            xvelAvg = yvelAvg = xposAvg = yposAvg = 0.0
            neighboringBoids = 0

            for otherBoid in boidList:
                if otherBoid is not curBoid:
                    dx = abs(curBoid.x - otherBoid.x)
                    dy = abs(curBoid.y - otherBoid.y)
                    if (dx<g_visibleRange and dy<g_visibleRange):
                        dist = curBoid.distance(otherBoid)
                        # separation check
                        if (dist < g_protectedRange):
                            closeDx += curBoid.x - otherBoid.x
                            closeDy += curBoid.y - otherBoid.y

                        # alignment and cohesion checks
                        elif (dist < g_visibleRange):
                            xvelAvg += otherBoid.vx
                            yvelAvg += otherBoid.vy
                            xposAvg += otherBoid.x
                            yposAvg += otherBoid.y
                            neighboringBoids += 1

            # alignment and cohesion update
            if (neighboringBoids > 0):
                xvelAvg = xvelAvg / neighboringBoids
                yvelAvg = yvelAvg / neighboringBoids
                xposAvg = xposAvg / neighboringBoids
                yposAvg = yposAvg / neighboringBoids

                curBoid.vx += (xposAvg - curBoid.x)*g_centeringFactor + (xvelAvg - curBoid.vx)*g_matchingFactor
                curBoid.vy += (yposAvg - curBoid.y)*g_centeringFactor + (yvelAvg - curBoid.vy)*g_matchingFactor

            # separation update
            curBoid.vx += (closeDx * g_avoidFactor)
            curBoid.vy += (closeDy * g_avoidFactor)

            # boundary check
            if curBoid.y < g_topMargin:
                curBoid.vy += g_turnFactor
            if curBoid.y > g_bottomMargin:
                curBoid.vy -= g_turnFactor
            if curBoid.x < g_leftMargin:
                curBoid.vx += g_turnFactor
            if curBoid.x > g_rightMargin:
                curBoid.vx -= g_turnFactor

            # speed tamping
            speed = math.sqrt(curBoid.vx*curBoid.vx + curBoid.vy*curBoid.vy)
            if speed > g_maxSpeed:
                curBoid.vx = (curBoid.vx/speed)*g_maxSpeed
                curBoid.vy = (curBoid.vy/speed)*g_maxSpeed
            if speed < g_minSpeed:
                curBoid.vx = (curBoid.vx/speed)*g_minSpeed
                curBoid.vy = (curBoid.vy/speed)*g_minSpeed

            # update position
            curBoid.x += curBoid.vx
            curBoid.y += curBoid.vy
            curBoid.c.move(curBoid.vx, curBoid.vy)
            curBoid.vec = Line(Point(curBoid.x, curBoid.y), Point(curBoid.x + (curBoid.vx * 100), curBoid.y + (curBoid.vy * 100)))
            curBoid.vec.draw(win)
        update()
        if(win.checkKey() or win.checkMouse()):
            break
    win.close()

if __name__ == "__main__":
    main()