import math

# This gives the variables their assigned number. These numbers will become apart of the formula
a = int(input("A: "))
b = int(input("B: "))
c = int(input("c: "))

# These are the parts of the equation. Python gets the order of operations wrong, so in order to actually do it correctly, we need to solve it step by step
discriminant = (b**2 - (4*a*c))
plus_minus = -(b)
div = 2 * a
"""
This gives the functions their value by doing + or - -b. 
The quadratic equation returns two numbers because a parabola goes through the X axis at two points.
If the discriminant is less than 0, the equation becomes an imaginary number, so we need to let python know that
or else it sends an error.
"""
def quadratic_equation_plus():
  return plus_minus + math.sqrt(discriminant)
def quadratic_equation_minus():
  return plus_minus - math.sqrt(discriminant)
if discriminant < 0:
  print("This is an imaginary number!")
else:
  print((quadratic_equation_plus() / div),"and", (quadratic_equation_minus() / div))
