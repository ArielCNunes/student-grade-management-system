# Student Grade Management System

# Store multiple students with their information
# Each student is a dictionary inside a list
# Each student has nested data - grades is another dictionary
students = [
    {
        "name": "Alice Johnson",
        "id": 12345,
        "grades": {"Math": [85, 92, 78], "English": [88, 91, 85], "Physics": [90, 87, 94]}
    },
    {
        "name": "Bob Smith", 
        "id": 12346,
        "grades": {"Math": [76, 84, 90], "English": [82, 79, 87], "Physics": [85, 88, 91]}
    },
    {
        "name": "Jack Shepard", 
        "id": 12347,
        "grades": {"Math": [45, 84, 90], "English": [82, 55, 87], "Physics": [85, 88, 78]}
    }
]

# Loop through students and print grades
for student in students:
    print(f"Student {student['name']}, (ID: {student['id']})")
    for subject, grades in student['grades'].items():
        print(f"{subject}: {grades}")
    print()

# Avarages with functions
def calculate_average(grades):
    """Calculate the average of a list of grades"""
    if len(grades) == 0: # avoid division by 0
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(average):
    """Convert numeric average to letter grade"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
# Overall DPA
def calculate_overall_gpa(student):
    """Calculate the overall GPA for a student across all subjects"""
    total_points = 0
    total_subjects = 0

    for subject, grades in student['grades'].items():
        avg = calculate_average(grades)
        total_points += avg
        total_subjects += 1

    if total_subjects == 0:
        return 0
        
    return total_points / total_subjects

# Call functions
for student in students:
    print(f"Student {student['name']}, (ID: {student['id']})")

    total_gpa = 0
    subject_count = 0

    for subject, grades in student['grades'].items(): # .items() returns the key value pairing -> "("Math", [85, 92, 78])"
        avg = calculate_average(grades)
        letter = get_letter_grade(avg)
        print(f"    {subject}: {grades} -> Average: {avg:.1f} ({letter})")
        total_gpa += avg
        subject_count += 1
    
    overall_gpa = calculate_overall_gpa(student)
    overall_letter = get_letter_grade(overall_gpa)
    print(f"  OVERALL GPA: {overall_gpa:.2f} ({overall_letter})")
    print("-" * 50)
    print()

# Adding nre students
def add_new_student():
    """Add a new student to the system"""
    print("\n=== Adding New Student ===")
    name = input("Enter student name: ")

    # Generate a simple ID
    student_id = len(students) + 12345

    # Create new object
    new_student = {
        "name": name,
        "id": student_id,
        "grades": {}
    }

    # Append to existing list and return it
    students.append(new_student)
    print(f"Added {name} with ID {student_id}")
    return new_student

# Add grades
def add_grade_to_student():
    """Add a grade to an existing student"""
    print("\n=== Add Grade ===")

    # Show all students
    for i, student in enumerate(students): # enumerate gives index and value (e.g.: "0: Jack Shepard")
        print(f"{i}: {student['name']} (ID: {student['id']})")
    
    try:
        choice = int(input("Choose student number: "))
        student = students[choice]
        
        subject = input("Enter subject: ")
        grade = float(input("Enter grade: "))
        
        # Add subject if it doesn't exist
        if subject not in student['grades']:
            student['grades'][subject] = []
        
        student['grades'][subject].append(grade)
        print(f"Added grade {grade} in {subject} for {student['name']}")
        
    except (ValueError, IndexError):
        print("Invalid input!")

# Menu system
def main_menu():
    """Main program menu"""
    while True:
        print("\n=== Grade Management System ===")
        print("1. View all students")
        print("2. Add new student") 
        print("3. Add grade to student")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            for student in students:
                print(f"Student: {student['name']} (ID: {student['id']})")
                
                for subject, grades in student['grades'].items():
                    avg = calculate_average(grades)
                    letter = get_letter_grade(avg)
                    print(f"  {subject}: {grades} -> Average: {avg:.1f} ({letter})")
                
                if student['grades']:  # Only show GPA if student has grades
                    overall_gpa = calculate_overall_gpa(student)
                    overall_letter = get_letter_grade(overall_gpa)
                    print(f"  OVERALL GPA: {overall_gpa:.2f} ({overall_letter})")
                print("-" * 50)
                
        elif choice == "2":
            add_new_student()
            
        elif choice == "3":
            add_grade_to_student()
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    main_menu()