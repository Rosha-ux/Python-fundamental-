class student:
    def __init__(self,name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
        

stud1 = student("Ross", 9.0)
stud2 = student("Hello", 5.0)


print(f"{stud1.name} got the cgpa of {stud1.cgpa} in his last semester")