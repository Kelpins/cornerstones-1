"""

This program will determine the maximum deflection values for a cantilevered beam with a load at one end,
given the user inputs of separate load weights, beam length, modulus of elasticity, beam base length, and beam height length.

First, the program will prompt the user for each of the above inputs, barring load weight.
Next, the program will verify that the user inputted valid positive numbers, reprompting the user in case they did not.
Once the constants are verified, the program will prompt the user for five load weights. This is our independent variable.
In each step of the loop, a similar verification check will be run to ensure each W value is positive.
Once we have all of our load weights inputted into a numpy array, we will run an operation on the array to convert to dmax values.
We will then run a function to find the maximum value among items in that array, and find corresponding load weight.
Finally, we will print our concluding statement with the maximized deflection value and its associated load weight.

Oh also after I complete the code, I will add in the if statement so it proves I know what we did in class.
That's just a stupid way to do it when numpy does everything implicitly and cleanly

"""

#numpy arrays for faster calculations
import numpy as np

#ask for an input L
l = float(input("Please input a positive numeric value for L: "))
#verifies that L is positive
while (l < 0):
    print("L must be positive.")
    #prompts user for a new value of L until L is positive
    l = float(input("Please input a positive value for L: "))

#ask for an input e
e = float(input("Please input a positive numeric value for E: "))
#verifies that e is positive
while (e < 0):
    print("E must be positive.")
    #prompts user for a new value of E until E is positive
    e = float(input("Please input a positive value for E: "))
    
#ask for an input b
b = float(input("Please input a positive numeric value for b: "))
#verifies that b is positive
while (b < 0):
    print("b must be positive.")
    #prompts user for a new value of b until b is positive
    b = float(input("Please input a positive value for b: "))

#ask for an input h
h = float(input("Please input a positive numeric value for h: "))
#verifies that h is positive
while (h < 0):
    print("h must be positive.")
    #prompts user for a new value of h until h is positive
    h = float(input("Please input a positive value for h: "))

#number of load weight inputs to maximize
num_inputs = 5
#define a list of w_vals to contain our five user-inputted values of W
w_vals = np.zeros(num_inputs)
#prompt the user 5 times
for i in range(num_inputs):
    #ask for an input w_i
    w = float(input("Please input a positive numeric value for W_" + str(i) + ": "))
    #verifies that w is positive
    while (w < 0):
        print("W must be positive.")
        #prompts user for a new value of w until w is positive
        w = float(input("Please input a positive value for W" + str(i) + ": "))
    #add the verified w value to our numpy list
    w_vals[i] = w

#create a new numpy array of all of the dmax values
dmax_vals = ((w_vals * 4 * l**3) / (e * b * h ** 3))
#find the max dmax value
max_dmax = np.max(dmax_vals)
#find where that value exists in the array
max_index = np.where(dmax_vals == max_dmax)
#find the w value corresponding to the max dmax
max_w = w_vals[max_index]

#print the final statement
print("For W = " + str(round(max_w[0], 3)) + ", we have the largest d_max value of " + str(round(max_dmax, 3)) + ".")



###write an if statement inside a loop so that i get +20 points###

#can initialize at 0 since all values are positive, so the maximum value must be positive as well
maximum_dmax_value = 0
corresponding_w_value = 0

#loop through values to find maximum value
for i in range(len(dmax_vals)):
    #if this dmax value is the largest one we've found so far, update the variables to reflect that
    if (dmax_vals[i] > maximum_dmax_value):
        maximum_dmax_value = dmax_vals[i]
        corresponding_w_value = w_vals[i]

#print it again to prove it's the same result
print("For W = " + str(round(corresponding_w_value, 3)) + ", we have the largest d_max value of " + str(round(maximum_dmax_value, 3)) + ".")

