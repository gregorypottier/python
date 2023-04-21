# Math - Polar Coordinates
from cmath import polar

z = complex(input())
phase = polar(z)
for num in phase:
    print(num)
