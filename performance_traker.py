class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def cal_avg(self):
        return sum(self.marks)/len(self.marks)

def Avg_Cal(std):
    avg={}
    for name ,marks in std.items():
        student=Student(name,marks)
        avg[name]=round(student.cal_avg(),2)
    return avg



def Topper(avg):
    top_student = max(avg, key=avg.get)
    return top_student
    



students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
avg_marks=Avg_Cal(students)
topper=Topper(avg_marks)

print(f"Average Marks: {avg_marks}")
print(f"Top Performer: \"{topper}\"")