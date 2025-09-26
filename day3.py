"""
Write a program with for loop that converts mph to km/h and ft/h for 10<mph<100 with a decrement of 10 mph.
*****************************************************************
Write a program using a for loop to print a degree to radian conversion table
(Remember: To convert from degrees to radians, you need to multiply the number of degrees by π/180).
Use 45 as the increment for degree values. Write the output like this:
0 degree in radians is 0pi
45 degree in radians is 0.25pi
90 degree in radians is 0.5pi

"""

for i in range(100, 0, -10):
    kmh = i * 1.60934
    fth = i * 5280
    print(f"{i} mph is {kmh:.2f} km/h and {fth} ft/h")

# ---------------------------------------------------------------#

for i in range(0, 361, 45):
    deg_to_rad = i / 180
    print(f"{i} degree in radians is {deg_to_rad}pi")


"""
1- Radioactive decay of radioactive materials can be modeled by the equation

          A=A0e-t(log(2)/h)

where A is the amount of material at time t and A0 is the amount at time 0, and h is the half-life.

Technetium-99 is a radioisotope that is used in imaging of the brain.
It has a half-life of 6 hours.
Write a program that displays the relative amount A/A0 in a patient body every hour for 24 hours after receiving a dose.
Create a neat table, and use a while loop.

"""

import math

i = 0
while i <= 24:
    A_A0 = math.exp(-i * (math.log(2) / 6))
    print(f"After {i} hours, the relative amount A/A0 is {A_A0:.4f}")
    i += 1


"""
******************************************************************************************

2- Transformer circuit power: Write a python program that will solve the following problem:

    image.png

image.png

This is a device called a transformer.  These are often constructed by wrapping coils of wire around a ferrite core.
The figure above illustrates a situation that occurs in various audio devices such as cell phones and music players.
In this circuit, a transformer is used to connect a speaker to the output of an audio amplifier.

The symbol used to represent the transformer is intended to suggest two coils of wire.
The parameter n of the transformer is called the “turns ratio” of transformer.
(The number of times that a wire is wrapped around the core to form a coil is called the number of turns in the coil.
The turns ratio is literally the ratio of the number of turns in two coils of wire.)

When designing the circuit, we are concerned primarily with the value of the power delivered to the speakers
that power causes the speakers to produce the sounds we want to hear.
Suppose we were to connect the speakers directly to the amplifier without using the transformer.
Some fraction of the power available from the amplifier would get to the speakers.
The rest of the available power would be lost in the amplifier itself.
The transformer is added to the circuit to increase the fraction of the amplifier power that is delivered to the speakers.

The power Ps delivered to the speakers is calculated using the formula:

Ps = Rs ( n Vs / ( n2 R0 + Rs))2  

Write a python program that models the circuit shown and varies the turns ratio from 0.01 to 2 in .01 increments,
and also finds the value of the turns ratio that maximizes the power delivered to the speakers. Use these values for solving the problem:

R0 =10

Rs= 5

Vs = 7


"""

R0 = 10
Rs = 5
Vs = 7
max_power = 0
optimal_n = 0
n = 0.01
while n <= 2.0:
    Ps = Rs * (n * Vs / (n**2 * R0 + Rs)) ** 2
    # print(f"{n:.2f}\t{Ps:.4f}")
    if Ps > max_power:
        max_power = Ps
        optimal_n = n
    n += 0.01
print(
    f"The optimal turns ratio is {optimal_n:.2f} with a maximum power of {max_power:.4f} W."
)
