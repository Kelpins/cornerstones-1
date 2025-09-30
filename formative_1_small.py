"""

This program will determine the maximum deflection values for a cantilevered beam with a load at one end,
given the user inputs of separate load weights, beam length, modulus of elasticity, beam base length, and beam height length.

First, the program will prompt the user for each of the above inputs, barring load weight.
Next, the program will initialize maximum dmax and corresponding w values to 0.
This is okay since every value must be positive, so the maximum value will always be greater than 0.
Once the constants are verified, the program will prompt the user for five load weights. This is our independent variable.
As the user inputs each load weight, the program calculates dmax for that weight.
We then check to see if that is the largest dmax found so far; if it is, we update our global variables accordingly.
Finally, we will print our concluding statement with the maximized deflection value and its associated load weight.

"""

# numpy arrays for faster calculations (unused)
import numpy as np

# ask for an input L
l = float(input("Please input a positive numeric value for L: "))

# ask for an input e
e = float(input("Please input a positive numeric value for E: "))

# ask for an input b
b = float(input("Please input a positive numeric value for b: "))

# ask for an input h
h = float(input("Please input a positive numeric value for h: "))


max_dmax_val = 0
corresponding_w_val = 0

# prompt the user 5 times
for i in range(5):
    # ask for an input w_i
    w = float(input("Please input a positive numeric value for W_" + str(i) + ": "))

    # calculate dmax
    dmax = (w * 4 * l**3) / (e * b * h**3)
    # check if its the largest so far
    if dmax > max_dmax_val:
        # if this is the largest dmax, update variables accordingly
        max_dmax_val = dmax
        corresponding_w_val = w

# print concluding statement with maximized dmax value and corresponding w
print(
    "For W = "
    + str(round(corresponding_w_val, 3))
    + ", we have the largest d_max value of "
    + str(round(max_dmax_val, 3))
    + "."
)
