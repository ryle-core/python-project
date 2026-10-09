class student:

   def __init__(self,name,age, gender):
       self.name= name
       self.age= age
       self.gender=gender



   def study(self):
        print("student is studying")

   def sing (self):
      print("student is singing")

student1 = student("jade" ,14 , "female")
print(student1.name, student1.age, student1.gender)
student2 = student("john" ,14 ,  "male")
print(student2.name, student2.age, student2.gender)
student3 = student("jada" ,19 , "female")
print(student3.name, student3.age, student3.gender)
student4 = student("mary" ,16 , "female")
print(student4.name, student4.age, student4.gender)

