
class Father:
    father_name = "Raj"
    father_hobby = "Playing Chess"


class Mother:
    mother_name = "Sita"
    mother_hobby = "Reading Books"


class Child(Father, Mother):
    child_name = "Aman"

    def show_details(self):
        print("Father Name  :", self.father_name)
        print("Father Hobby :", self.father_hobby)
        print("Mother Name  :", self.mother_name)
        print("Mother Hobby :", self.mother_hobby)
        print("Child Name   :", self.child_name)


obj = Child()
obj.show_details()