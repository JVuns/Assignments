eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [eren, mikasa, armin]
def comprint(students):
  for student in students:
        for a, b in student.items():
              print(a,": ",b)         
    # print("name", student["name"])
    # print("homework :", student["homework"])
    # print("quizzes :", student["quizzes"])
    # print("tests :", student["tests"])
    # print()
comprint(students)
def average(numbers):
  # print(numbers)
  total = sum(numbers)
  total = float((total))
  endtotal = total / len(numbers)
  return endtotal
# test = average(mikasa["homework"])
# print(test)
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  homework *= 0.1
  quizzes *= 0.3
  tests *= 0.6
  avgtotal = homework + quizzes + tests
  return avgtotal
def get_letter_grade(score):
  if score > 90:
      return "A"
  elif score >= 80 and score < 90:
      return "B"
  elif score >= 70 and score < 80:
      return "C"
  elif score >= 60 and score < 70:
      return "D"
  else:
      return "F"
# test = get_letter_grade(get_average(eren))
# print(test)

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student)) 
    return average(results)

print (get_class_average(students))
print (get_letter_grade(get_class_average(students)))
# print(get_average(eren))