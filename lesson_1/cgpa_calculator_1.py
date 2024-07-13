def calculate_grade(marks):
    if 0 <= marks <= 40:
        return 'F'
    elif 41 <= marks <= 60:
        return 'D'
    elif 61 <= marks <= 70:
        return 'C'
    elif 71 <= marks <= 80:
        return 'B'
    elif 81 <= marks <= 90:
        return 'A'
    elif 91 <= marks <= 100:
        return 'A+'
    else:
        return None


def main():
    subjects = ["Bangla", "English", "Math", "Science"]
    total_marks = 0
    num_subjects = len(subjects)

    print("Please enter your marks for the following subjects (1-100):")

    for subject in subjects:
        while True:
            try:
                marks = int(input(f"{subject}: "))
                if 1 <= marks <= 100:
                    total_marks += marks
                    grade = calculate_grade(marks)
                    print(f"Grade for {subject}: {grade}")
                    break
                else:
                    print("Invalid input. Marks must be between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    average_marks = total_marks / num_subjects
    overall_grade = calculate_grade(average_marks)

    print(f"\nYour average marks: {average_marks:.2f}")
    print(f"Your overall grade: {overall_grade}")


if __name__ == "__main__":
    main()
