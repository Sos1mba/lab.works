import sys 

while True:
    try:
        n_of_grades = int(input("Number of subjects: "))

        Grades = []

        for i in range(n_of_grades):
            grade = int(float(input("Grades: ")))
            Grades.append(grade)

        avarage_score = sum(Grades) / n_of_grades

        print(f"Your avarage score: {avarage_score:.2f}")
        break
    except ValueError:
        print("wrong value")
        