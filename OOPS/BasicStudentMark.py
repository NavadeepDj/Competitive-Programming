class Student:
    def __init__(self, rollNo, name, id1):
        self.__rollNo = rollNo
        self.name = name
        self.id1 = id1
    def printing(self):
        print(f"Roll No: {self.__rollNo}")

    def get_name(self):
        return self.name
    def fet_rollNo(self):
        # print(self.__rollNo)
        return self.__rollNo


class TotalMarks:
    def __init__(self, student, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.student = student  # store the Student object
        # print(f"Me: {self.student._Student__rollNo}, Mark1: {self.mark1}")
        print(f"Me: {self.student.fet_rollNo()}, Mark1: {self.mark1}")



s = Student(6, "NK", 0)
t = TotalMarks(s, 1, 2, 3)
