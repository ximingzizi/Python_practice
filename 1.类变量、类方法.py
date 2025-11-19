class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
    @classmethod
    def change_str(cls,string):
        name,age = string.split(' ')
        return cls(name,age)
    @staticmethod # 静态方法,不能访问类变量
    def print_str(string):
        print(f"{string}")

s1 = Student('Bob', 12)
# s2 = Student.change_str('Alice 13')
print(f"{Student.count}")
print(f"{s1.count}")
Student.print_str(s1.name)

