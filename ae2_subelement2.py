# Defines the "read_grades" function, which accepts a filename and returns every grade in that file as a list
def read_grades(filename):
    # Create an empty list to store all the grades in a given file
    grades = []
    
    # Open the file for reading
    with open(filename, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Remove whitespace and convert the line to an integer
            grade = int(line.strip())
            # Add the grade to our list
            grades.append(grade)
    
    # Return the complete list of grades from the inputted file
    return grades

# Defines the "find_min_and_index" function which accepts a list of grades and outputs the location and value of the lowest grade
def find_min_and_index(grades):
    # Find the smallest grade in the list
    minimum = min(grades)
    
    # Find the index at which the smallest grade value occurs
    index = grades.index(minimum)
    
    # Return both values as a tuple
    return minimum, index

# Defines the "find_max_and_index" function which accepts a list of grades and outputs the location and value of the highest grade
def find_max_and_index(grades):
    # Find the largest grade in the list
    maximum = max(grades)
    
    # Find the index at which the maximum grade value occurs
    index = grades.index(maximum)
    
    # Return both values as a tuple
    return maximum, index

# Defines the "display_results" function which accepts the four grades our program will report and prints them to the console
def display_results(min_math, max_math, chem_for_min, chem_for_max):
    # Print the first line showing min math grade and corresponding chemistry grade
    print(f"The student who got {min_math} in math got {chem_for_min} in chemistry.")
    # Print the second line showing max math grade and corresponding chemistry grade
    print(f"The student who got {max_math} in math got {chem_for_max} in chemistry.")

# Defines the "main" function which will call our other functions in order, effectively running our program
def main():
    # Interpret all math grades from the maths.txt file as a list of numbers
    math_grades = read_grades('maths.txt')
    
    # Interpret all chemistry grades from the chemistry.txt file as a list of numbers
    chemistry_grades = read_grades('chemistry.txt')
    
    # Find the minimum math grade and its index
    min_math, min_math_index = find_min_and_index(math_grades)
    
    # Find the maximum math grade and its index
    max_math, max_math_index = find_max_and_index(math_grades)
    
    # Get the chemistry grade for the student at the minimum math position
    chemistry_at_min = chemistry_grades[min_math_index]
    
    # Get the chemistry grade for the student at the maximum math position
    chemistry_at_max = chemistry_grades[max_math_index]
    
    # Display all the results in the required format
    display_results(min_math, max_math, chemistry_at_min, chemistry_at_max)

#Runs the main function to begin the program
main()