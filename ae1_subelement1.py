import math


mu_static = 0.15
mu_kinetic = 0.10

force_gravity = 9.81


"""

Program Requirements
Part A: Input Validation for Angle
• Prompt the user to enter the mass m1 and angle θ
• Angle limits: 30° ≤ θ ≤ 45°
• If the angle θ entered is outside this range, display an error message such as:
  The minimum value for θ is 30 degrees and the maximum value of it is 45
  degrees. Please input a correct value.
• Important: The program can continue only if θ is in the accepted range.
  Otherwise, the error should be displayed repeatedly until the user inputs an
  acceptable value for θ.

"""

angle = float(input("Enter a numeric value between 30 and 45 to represent the angle (degrees): "))
while (angle < 30 or angle > 45):
    print("The range of acceptable angles is between 30 and 45 degrees. Please input an acceptable value.")
    angle = float(input("Enter a numeric value between 30 and 45 to represent the angle (degrees): "))

mass_1 = float(input("Enter a numeric value for mass 1 (kilograms): "))


"""

Part B: Calculate Threshold Mass
• Calculate and return m2 using the equation provided
• Display the result using this exact format: The threshold for m2 for which the
  blocks remain stationary is '(enter the value of m2 here)'.
  
"""

threshold_mass_2 = mass_1 * (math.sin(angle) + mu_static * math.cos(angle))

print("The threshold for m2 for which the blocks remain stationary is '" + str(threshold_mass_2) + "'.")

"""

Part C: Input Validation for Mass m2
• Ask the user to input a new value for m2 that is larger than the value
  calculated in Part B
• Check if the input m2 is larger than the calculated threshold
• If not, display an error message
• Important: Similar to Part A, the program can continue only if m2 is larger
  than the calculated threshold. Otherwise, repeat the error message until the
  user inputs an acceptable value for m2.

"""

mass_2 = float(input("Please input a new value for mass 2 larger than the minimum threshold value displayed above: "))

while (mass_2 <= threshold_mass_2):
    print("The new mass should have a value greater than the threshold value provided above. Please input an acceptable value.")
    mass_2 = float(input("Please input a new value for mass 2 larger than the minimum threshold value displayed above: "))

"""
  
Part D: Calculate Acceleration Calculate the acceleration of m1 up the slope using:
        a = g(sin(θ) + 𝜇𝑠 cos(θ)) - g(sin(θ) + 𝜇𝑘 cos(θ))

"""

acceleration = force_gravity * (math.sin(angle) + mu_static * math.cos(angle)) - force_gravity * (math.sin(angle) + mu_kinetic * math.cos(angle))

"""

Part E: Display Final Result Display the result using this exact format:
        For m1 = '(enter the value of m1 here)' and m2='(enter the value of m2 here)' m1
        moves up the slope with acceleration '(enter the value of a here)'.

"""

print("For m1 = \'" + mass_1 + "' and m2='" + new_mass_2 + "' m1 moves up the slope with acceleration '" + acceleration + "'.")