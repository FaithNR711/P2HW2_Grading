# CTI-110
# P2HW2 - List
# Faith Rivera
# 04/7/2023

# Prompt the user to enter grades for each module
module1 = 65.5
module2 = 88
module3 = 78.5
module4 = 90
module5 = 61
module6 = 92

# Create a list of grades entered by the user
grades_list = [module1, module2, module3, module4, module5, module6]

# Determine the lowest and highest grades in the list
lowest_grade = min(grades_list)
highest_grade = max(grades_list)

# Calculate the sum and average of grades in the list
grades_sum = sum(grades_list)
grades_average = grades_sum / len(grades_list)

# Display the grades for each module
print("Grades for each module:")
print("Module 1:", module1)
print("Module 2:", module2)
print("Module 3:", module3)
print("Module 4:", module4)
print("Module 5:", module5)
print("Module 6:", module6)

# Display the results of the grades
print("\n----Results----")
print("Lowest grade:", format(lowest_grade, '.2f'))
print("Highest grade:", format(highest_grade, '.2f'))
print("Sum of grades:", format(grades_sum, '.2f'))
print("Average of grades:", format(grades_average, '.2f'))
