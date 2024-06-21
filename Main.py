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
g_matchingFactor = 0.1
g_maxSpeed = 0.01
g_minSpeed = 0.007

g_protectedRange = 7
g_visibleRange = 20

g_numBoids = 5

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.c = Circle(Point(x, y), 5)

def main():
    # initialize the boidList with random positions/velocities
    boidList = []
    for _n in range(0, g_numBoids):
        x = random.randint(g_leftMargin, g_rightMargin)
        y = random.randint(g_topMargin, g_bottomMargin)
        vx = random.uniform(g_minSpeed, g_maxSpeed)
        vy = random.uniform(g_minSpeed, g_maxSpeed)
        boidList.append(Boid(x,y,vx,vy))

    # start the graphics window, draw the boids
    win = GraphWin(title="Boids", width=g_width, height=g_height, autoflush=False)
    for boid in boidList:
        boid.c.draw(win)

    while(True):
        for curBoid in boidList:
            closeDx = 0
            closeDy = 0

            xvelAvg = 0
            yvelAvg = 0
            neighboringBoids = 0

            for otherBoid in boidList:
                if otherBoid is not curBoid:
                    dist = math.dist([curBoid.x, curBoid.y], [otherBoid.x, otherBoid.y])
                    # separation check
                    if (dist < g_protectedRange):
                        closeDx += curBoid.x - otherBoid.x
                        closeDy += curBoid.y - otherBoid.y

                    # alignment and cohesion checks
                    if (dist < g_visibleRange):
                        xvelAvg += otherBoid.vx
                        yvelAvg += otherBoid.vy
                        neighboringBoids += 1

            # alignment and cohesion update
            if (neighboringBoids > 0):
                xvelAvg = xvelAvg / neighboringBoids
                yvelAvg = yvelAvg / neighboringBoids

                curBoid.vx += (xvelAvg - curBoid.vx)*g_matchingFactor
                curBoid.vy += (yvelAvg - curBoid.vy)*g_matchingFactor

            # separation update
            curBoid.vx += closeDx * g_avoidFactor
            curBoid.vy += closeDy * g_avoidFactor

            # boundary check
            if curBoid.x < g_leftMargin:
                curBoid.vx += g_turnFactor
            if curBoid.x > g_rightMargin:
                curBoid.vx -= g_turnFactor
            if curBoid.y > g_bottomMargin:
                curBoid.vy -= g_turnFactor
            if curBoid.y < g_topMargin:
                curBoid.vy += g_turnFactor

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
        update()

if __name__ == "__main__":
    main()