# import the python math library for sine and cosine
import math

# defining coefficient of static friction
mu_static = 0.15

# defining coefficient of kinetic friction
mu_kinetic = 0.10

# defining force of gravity
force_gravity = 9.81

# prompts the user for an initial angle value
angle = float(input("Enter a numeric value between 30 and 45 to represent the angle (degrees): "))

# if the angle provided is out of range, repeat the following until the user provides a valid angle:
while (angle < 30 or angle > 45):
    # output to the user that their angle value was out of range
    print("The range of acceptable angles is between 30 and 45 degrees. Please input an acceptable value.")
    # request that the user input a new value to represent the angle
    angle = float(input("Enter a numeric value between 30 and 45 to represent the angle (degrees): "))
    
# since math.sin() and math.cos() both take radian inputs, this new variable represents the angle in radians for calculations
angle_rad = math.radians(angle)

# prompt the user for a mass value for block 1 
mass_1 = float(input("Enter a numeric value for mass 1 (kilograms): "))

# calculate the minimum mass value for block two such that block 1 does not slide back down the ramp
threshold_mass_2 = mass_1 * (math.sin(angle_rad) + mu_static * math.cos(angle_rad))

# output this value to the user
print("The threshold for m2 for which the blocks remain stationary is '" + str(threshold_mass_2) + "'.")

# prompt the user for a new value for mass 2 to be used in an example case
mass_2 = float(input("Please input a new value for mass 2 larger than the minimum threshold value displayed above: "))

# if the mass provided is less than the minimum possible value, repeat the following until the user provides a valid mass:
while (mass_2 <= threshold_mass_2):
    # output to the user that their mass value was lower than the threshold value
    print("The new mass should have a value greater than the threshold value provided above. Please input an acceptable value.")
    # request that the user input a new value to represent the mass of block 2
    mass_2 = float(input("Please input a new value for mass 2 larger than the minimum threshold value displayed above: "))

# calculate instantaneous acceleration using the provided equation
acceleration = force_gravity * (math.sin(angle_rad) + mu_static * math.cos(angle_rad)) - force_gravity * (math.sin(angle_rad) + mu_kinetic * math.cos(angle_rad))

# provide output to the user in the provided formatting
print("For m1 = \'" + str(mass_1) + "' and m2='" + str(mass_2) + "' m1 moves up the slope with acceleration '" + str(acceleration) + "'.")