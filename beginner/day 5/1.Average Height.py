student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum_of_heights=0
num_of_student=0
for item in student_heights:
    sum_of_heights += item
    num_of_student+=1
average_heights=round(sum_of_heights/num_of_student)
print(f"the average height is {average_heights}")