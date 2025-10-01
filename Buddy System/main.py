# buddy_system.py
# Buddy System skeleton for high school hackathon
# This program provides basic team management and buddy pairing.

class Student:
    def __init__(self, name, grade):
        """
        Initialize a student with a name and grade.
        Each student can be assigned a buddy later.
        """
        self.name = name
        self.grade = grade
        self.buddy = None

    def assign_buddy(self, buddy):
        """
        Assign the given student as a buddy to this student.
        """
        self.buddy = buddy

class BuddySystem:
    def __init__(self):
        """
        Create an empty buddy system to hold all students.
        """
        self.students = []

    def add_student(self, name, grade):
        """
        Add a new student to the system.
        Args:
            name (str): Student's name.
            grade (int): Student's grade.
        """
        student = Student(name, grade)
        self.students.append(student)
    
    def list_students(self):
        """
        Print the list of all students currently in the system.
        """
        for idx, student in enumerate(self.students):
            print(f"{idx}: {student.name} (Grade {student.grade})")
    
    def pair_buddies(self):
        """
        Form buddy pairs by assigning consecutive students to each other.
        If odd number of students, the last one remains unpaired.
        """
        for i in range(0, len(self.students)-1, 2):
            self.students[i].assign_buddy(self.students[i+1])
            self.students[i+1].assign_buddy(self.students[i])

    def show_pairs(self):
        """
        Show all buddy pairs without duplication.
        """
        paired = set()
        for student in self.students:
            # Avoid showing the same pair twice
            if student.buddy and student.name not in paired:
                print(f"{student.name} ↔ {student.buddy.name}")
                paired.add(student.name)
                paired.add(student.buddy.name)

def main():
    # Initialize the buddy system
    system = BuddySystem()
    # Add students for demonstration purposes. This could be replaced by user input or file reading.
    system.add_student("Alice", 10)
    system.add_student("Bob", 10)
    system.add_student("Charlie", 11)
    system.add_student("Diana", 11)
    # Display current students
    system.list_students()
    print("Pairing buddies...")
    # Create buddy pairs
    system.pair_buddies()
    print("Buddy pairs:")
    # Display the pairs
    system.show_pairs()

if __name__ == "__main__":
    main()
