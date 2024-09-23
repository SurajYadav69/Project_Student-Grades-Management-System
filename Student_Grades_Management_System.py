#Project Title: Student Grades Management System
# i just solved around 10 of array questions so now i want to test my skill in array with this small project

def input_student_data(num_students):
    names = []
    grades = []
    
    for i in range(num_students):
        name = input(f"Enter name of student {i + 1}: ")
        while True:
            try:
                grade = float(input(f"Enter grade of student {i + 1} (0-100): "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        names.append(name)
        grades.append(grade)
    
    return names, grades

def display_student_data(names, grades):
    print("\nStudent Grades:")
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]}: {grades[i]}")

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def find_highest_lowest(grades, names):
    highest_index = grades.index(max(grades))
    lowest_index = grades.index(min(grades))
    return (names[highest_index], grades[highest_index]), (names[lowest_index], grades[lowest_index])

def sort_students(names, grades):
    combined = list(zip(grades, names))
    combined.sort(reverse=True, key=lambda x: x[0])
    sorted_grades, sorted_names = zip(*combined)
    return sorted_names, sorted_grades

def main():
    num_students = int(input("Enter number of students (max 10): "))
    if num_students > 10:
        print("Maximum number of students is 10. Please try again.")
        return

    names, grades = input_student_data(num_students)
    
    display_student_data(names, grades)
    
    average_grade = calculate_average(grades)
    print(f"\nAverage Grade: {average_grade:.2f}")

    highest, lowest = find_highest_lowest(grades, names)
    print(f"Highest Grade: {highest[1]} ({highest[0]})")
    print(f"Lowest Grade: {lowest[1]} ({lowest[0]})")
    
    sorted_names, sorted_grades = sort_students(names, grades)
    print("\nStudents Sorted by Grades:")
    for i in range(len(sorted_names)):
        print(f"{i + 1}. {sorted_names[i]}: {sorted_grades[i]}")

if __name__ == "__main__":
    main()
