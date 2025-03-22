# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
average_height = 0
students = 0

for student_height in student_heights:
    students += 1
    average_height += student_height

average_height = average_height / students
average_height = round(average_height)

print(average_height)
