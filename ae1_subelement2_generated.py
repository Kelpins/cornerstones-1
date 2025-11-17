"""
Student Grades Analyzer
This program analyzes math and chemistry grades to find relationships between
students' performance in both subjects.
"""

def read_grades(filename):
    """
    Reads grades from a file and returns them as a list of integers.
    """
    # Create an empty list to store all the grades
    grades = []
    
    # Open the file for reading
    with open(filename, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Remove whitespace and convert the line to an integer
            grade = int(line.strip())
            # Add the grade to our list
            grades.append(grade)
    
    # Return the complete list of grades
    return grades


def find_min_and_max(grades):
    """
    Finds the minimum and maximum values in a list of grades.
    """
    # Find the smallest grade in the list
    minimum = min(grades)
    # Find the largest grade in the list
    maximum = max(grades)
    
    # Return both values as a tuple
    return minimum, maximum


def find_index(grades, value):
    """
    Finds the position (index) of a specific value in the list.
    """
    # Find and return the index where the value appears
    position = grades.index(value)
    # Return the position
    return position


def display_results(min_math, max_math, chem_for_min, chem_for_max):
    """
    Displays the results in the required format.
    """
    # Print the first line showing min math grade and corresponding chemistry grade
    print(f"The student who got {min_math} in math got {chem_for_min} in chemistry.")
    # Print the second line showing max math grade and corresponding chemistry grade
    print(f"The student who got {max_math} in math got {chem_for_max} in chemistry.")


def main():
    """
    Main function that runs the entire program.
    """
    # Print a message to show the program is starting
    print("Analyzing student grades...")
    print()
    
    # Read all math grades from the maths.txt file
    math_grades = read_grades('maths.txt')
    
    # Read all chemistry grades from the chemistry.txt file
    chemistry_grades = read_grades('chemistry.txt')
    
    # Find the minimum and maximum math grades
    min_math, max_math = find_min_and_max(math_grades)
    
    # Find the position of the student with the minimum math grade
    min_position = find_index(math_grades, min_math)
    
    # Find the position of the student with the maximum math grade
    max_position = find_index(math_grades, max_math)
    
    # Get the chemistry grade for the student at the minimum math position
    chemistry_at_min = chemistry_grades[min_position]
    
    # Get the chemistry grade for the student at the maximum math position
    chemistry_at_max = chemistry_grades[max_position]
    
    # Display all the results in the required format
    display_results(min_math, max_math, chemistry_at_min, chemistry_at_max)


# Check if this program is being run directly (not imported)
if __name__ == "__main__":
    # Run the main function
    main()