# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
heights = []
num_elements = int(input("Enter the number of students: "))
for n in range(num_elements):
  heights.append(int(input(f"Enter the weight of student {n+1}: ")))

sum = 0

for height in heights:
  sum += height

average_height = round(sum / num_elements) 

print(f"total height = {sum}")
print(f"number of students = {num_elements}")
print(f"average height = {average_height}")