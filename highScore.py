# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# student_scores = []
# num_elements = int(input("Enter the number of scores: "))
# for n in range(num_elements):
#   student_scores.append(int(input(f"Enter score {n+1}: ")))

# Write your code below this row 👇
high_score = 0

for n in student_scores:
  if n > high_score:
    high_score = n

print(f"The highest score in the class is: {high_score}")