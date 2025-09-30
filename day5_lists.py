import numpy as np

l = float(input("Please input a positive numeric value for L: "))
e = float(input("Please input a positive numeric value for E: "))
b = float(input("Please input a positive numeric value for b: "))
h = float(input("Please input a positive numeric value for h: "))

w_vals = np.zeros(5)
for i in range(5):
    w = float(input("Please input a positive numeric value for W_" + str(i) + ": "))
    while (w < 0):
        print("W must be positive.")
        w = float(input("Please input a positive value for W" + str(i) + ": "))
    w_vals[i] = w

dmax_vals = ((w_vals * 4 * l**3) / (e * b * h ** 3))
max_dmax = np.max(dmax_vals)
max_index = np.where(dmax_vals == max_dmax)
max_w = w_vals[max_index]

print("For W = " + str(round(max_w[0], 3)) + ", we have the largest d_max value of " + str(round(max_dmax, 3)) + ".")