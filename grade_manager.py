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

        if (total_subjects == 0):
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
