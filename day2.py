"""
Problem 1:  Write a program to compute the area A of an ellipse with semiaxes a and b and then
test your program with the values a = 2.5 m and b = 4 m.
Remember to include comments and have the user input the values for a and b.


import math

# input values for semi-major axis a and semi-minor axis b
semi_a = float(input("Enter the length of semi-major axis a (in meters): "))
semi_b = float(input("Enter the length of semi-minor axis b (in meters): "))

print(
    "The area of your ellipse is ",
    round(math.pi * semi_a * semi_b, 3),
    " square meters.",
)

*************************

Problem 2:

according to coulomb's law, the force F between two charged particles is given by the formula: F = Q1 * Q2 / 4*epsilon*pi*r^2'

epsilon = 8.8854 * 10^-12 farads/meter

write a program that calculates the force on a pair of charged particles based on the user input of Q1 coulombs, Q2 coulombs and r meters.

If the two balloons have the following charge and distance, compute the force:

Balloon 1:  3.25µC
Balloon 2:  6.35µC
Distance:  14.6 cm


import math

q1 = float(input("Enter the charge of particle 1 (in microcoulombs): "))
q2 = float(input("Enter the charge of particle 2 (in microcoulombs): "))
r = float(input("Enter the distance between the two particles (in centimeters): "))

print(
    "The force between the two charged particles is ",
    round(
        (q1 * q2 * 10 ** (-12.0)) / (4.0 * 8.8854e-12 * math.pi * (r / 100.0) ** 2), 3
    ),
    " newtons.",
)


Problem 1: Maximizer
Write a program that asks a user for two numbers and prints the larger number.
Can you improve your program to compare four numbers and then displays the largest number?
Don't forget to start by generating your pseudocode.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("The largest number is: " + str(max(num1, num2)))

num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

print("The largest number is: " + str(max(num1, num2, num3, num4)))



Problem 2:
 A mass m = 2 kilograms is attached to the end of a rope of length r = 3 meters.
 The mass is whirled around at high speed. The rope can withstand a maximum tension of T = 60 Newtons.
 Write a program that accepts a rotation speed v and determines if such a speed will cause the rope to break.

 The formula is: T=mv2/r
Have the user enter various speeds and let them know if the rope will break.


q = False
while not q:
    v = float(input("Enter the rotation speed in meters per second: "))
    m = 2.0  # mass in kilograms
    r = 3.0  # length of rope in meters
    T = 60.0  # maximum tension in Newtons

    tension = (m * v**2) / r

    if tension > T:
        print("The rope will break at this speed.")
    else:
        print("The rope will not break at this speed.")

    q = input("Do you want to quit? (yes/no): ").lower() == "yes"


Problem 3:
Write a program to calculate wind chill and report on frostbite times. Use the following formula:
Twc = 35.74 + 0.6215Ta - 35.75V0.16 + 0.4275TaV0.16

where Twc is the wind chill index, based on the Fahrenheit scale, Ta is the air temperature, measured in F, and V is the wind speed, in mph.
Prompt the user for required input and print Twc. If the value of Twc is below -19 report a frostbite time of 30 minutes or less.
If the value is below -48, report a frostbite time of 5 minutes or less.
State if Twc = -19 or greater “Frostbite not a concern for 30 minutes or less exposure”.

Test your program with the different air temperatures (Ta) and wind velocities (V).
Make sure when you test that is goes to all branches of the program.


air_temp = float(input("Enter the air temperature in Fahrenheit: "))
wind_speed = float(input("Enter the wind speed in miles per hour: "))

wind_chill = (
    35.74
    + 0.6215 * air_temp
    - 35.75 * wind_speed**0.16
    + 0.4275 * air_temp * wind_speed**0.16
)

print("The wind chill index is: " + str(round(wind_chill, 3)))
if wind_chill < -48:
    print("Frostbite time is 5 minutes or less.")
elif wind_chill < -19:
    print("Frostbite time is 30 minutes or less.")
else:
    print("Frostbite not a concern for 30 minutes or less exposure.")

"""
