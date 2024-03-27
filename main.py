from pygame import *
import cmath
import math

screen = display.set_mode((500, 500))

pos = [(250, 250), (125, 250), (375, 250)]
radii = [-250, 125, 125]

queue = [0, 1, 2]

def tangent(z1, z2, k1, k2):
    pos1 = (z1.real, z1.imag)
    pos2 = (z2.real, z2.imag)
    if type(k1) is complex: k1 = k1.real
    if type(k2) is complex: k2 = k2.real
    k1, k2 = sorted([k1, k2])
    if(k1 < 0.0):
        return abs(-1.0/k1-1.0/k2-math.hypot(*[x1-x2 for x1,x2 in zip(pos1, pos2)]))<0.0001
    else:
        return abs(1.0/k1+1.0/k2-math.hypot(*[x1-x2 for x1,x2 in zip(pos1, pos2)]))<0.0001

def descartes():
    c1,c2,c3 = queue[0:3]
    del queue[0:3]
    k1 = 1/radii[c1]
    k2 = 1/radii[c2]
    k3 = 1/radii[c3]
    k4 = (k1+k2+k3) - (2*cmath.sqrt(k1*k2 + k2*k3 + k3*k1))
    k5 = (k1+k2+k3) + (2*cmath.sqrt(k1*k2 + k2*k3 + k3*k1))

    z1 = complex(*pos[c1])
    z2 = complex(*pos[c2])
    z3 = complex(*pos[c3])
    z4 = ((z1*k1 + z2*k2 + z3*k3) - (2*cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k3*k1*z3*z1)))/k4
    z5 = ((z1*k1 + z2*k2 + z3*k3) + (2*cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k3*k1*z3*z1)))/k4
    z6 = ((z1*k1 + z2*k2 + z3*k3) - (2*cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k3*k1*z3*z1)))/k5
    z7 = ((z1*k1 + z2*k2 + z3*k3) + (2*cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k3*k1*z3*z1)))/k5

    for z, k in list(set(list(zip([z4, z5, z6, z7], [k4, k4, k5, k5])))):
        if tangent(z, z1, k, k1) and tangent(z, z2, k , k2) and tangent(z, z3, k , k3):
            radii.append(1/k)
            pos.append((z.real, z.imag))

            queue.append(len(pos)-1)
            queue.append(c1)
            queue.append(c2)

            queue.append(len(pos)-1)
            queue.append(c1)
            queue.append(c3)

for i in range(20000):
    descartes()
    # pos = list(set(pos))


while QUIT not in [e.type for e in event.get()]:
    screen.fill((255, 255, 255))
    for p, r in zip(pos, radii):
        draw.circle(screen, (0, 0, 0), p, abs(r), 1)
    display.flip()

quit()
exit()