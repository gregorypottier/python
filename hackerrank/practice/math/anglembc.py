# Math - find angle mbc
import math

AB, BC = float(input()), float(input())

AC = math.sqrt(AB**2 + BC**2)  # hypotenuse length
MC = AC / 2  # MC length

angle_MBC = round(math.degrees(math.atan(AB / BC))) 

print(f"{angle_MBC}\N{DEGREE SIGN}")
