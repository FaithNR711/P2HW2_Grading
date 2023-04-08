# This program takes a number grade, determines average, and displays letter grade for average.
# 04/20/2023
#CTI-P3HW1
# Enter grades for six modules
#Faith Rivera

mod_1 = 86.5
mod_2 = 80
mod_3 = 76.9
mod_4 = 90
mod_5 = 79
mod_6 = 88

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest, sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# determine letter grade for average

if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
elif average_grade >= 70:
    letter_grade = 'C'
elif average_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# print grades for each module

print(f'Module 1: {mod_1}')
print(f'Module 2: {mod_2}')
print(f'Module 3: {mod_3}')
print(f'Module 4: {mod_4}')
print(f'Module 5: {mod_5}')
print(f'Module 6: {mod_6}')

# print results

print('---------Results----------')
print(f'Lowest Grade: {lowest_grade}')
print(f'Highest Grade: {highest_grade}')
print(f'Sum of Grades: {sum_of_grades}')
print(f'Average: {average_grade}')
print('----------------------------')
print(f'Your grade is: {letter_grade}')
