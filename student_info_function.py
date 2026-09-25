"""
Student Information Module
A separate file for student information function.
"""

def get_student_info():
    """Get student information from user input."""
    print("Enter Student Information")
    print("-" * 30)
    
    name = input("Name: ").strip()
    batch = input("Batch: ").strip()
    course = input("Course: ").strip()
    learning_goal = input("Learning Goal: ").strip()
    
    return {
        "name": name,
        "batch": batch,
        "course": course,
        "learning_goal": learning_goal
    }


def display_student_info(student):
    """Display student information."""
    print("\nStudent Details")
    print("-" * 30)
    print(f"Name          : {student['name']}")
    print(f"Batch         : {student['batch']}")
    print(f"Course        : {student['course']}")
    print(f"Learning Goal : {student['learning_goal']}")


if __name__ == "__main__":
    student = get_student_info()
    display_student_info(student)