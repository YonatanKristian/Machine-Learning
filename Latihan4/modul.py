## override nilai sin dan pi
from math import sin, pi

print(sin(pi/2))

print("=====")

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))
print("\n")
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90

ar = radians(ad)
print(ar)
ad = degrees(ar)
print(ad)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)