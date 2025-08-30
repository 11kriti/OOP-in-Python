class Student:
    def __init__(self, name, roll, std, sec): .. CONST
        self.name = name
        self.roll = roll
        self.std = std
        self.sec = sec
        
    def show_info(self): //METHOD
        print(f"student name : {self.name} , roll no. : {self.roll} , std : {self.std} , sec : {self.sec}")
        
student1 = Student("Aman" , 3, "||", "E") // ACTUAL OBJECT
student2 = Student("Kriti" , 12, "||", "E")

student1.show_info() //CALL
student2.show_info()
