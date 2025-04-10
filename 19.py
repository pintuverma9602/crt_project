# Encapsulation Example (Simple Way)

class Student:
    def _init_(self):
        # Private Attribute
        self.__marks = 0  

    # Method to set marks
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Please enter valid marks (0 to 100)")

    # Method to get marks
    def show_marks(self):
        print("Marks of Student:", self.__marks)


# Object of Student Class
s1 = Student()

# Setting Marks
s1.set_marks(90)

# Showing Marks
s1.show_marks()