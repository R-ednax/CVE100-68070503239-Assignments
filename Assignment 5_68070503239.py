# %%
class Car:
    def __init__(self, model, rent_per_day, available = True):
        self.model = model
        self.rent_per_day = rent_per_day
        self.available = available

    def rent(self, days):
        if self.available:
            self.available = False
            total_cost = (self.rent_per_day * days)
            print ("Car rented. Total cost = ", total_cost)
        else:
            print("Car not available")

    def return_car(self):
        self.available = True
        print("Car returned")

    def display(self):
        print("Model: ", self.model)
        print("Rent per day: " , self.rent_per_day)
        print("Availability: ", self.available)

Car_1 = Car("Model S", 250,)
Car_2 = Car("Model X", 300,)

Car_1.rent(5)
Car_1.display()
Car_1.return_car()
Car_1.display()


print (" ")

Car_2.rent(5)
Car_2.display()
Car_2.return_car()
Car_2.display()





    
    

        

# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Student(Person):
    def __init__(self, name, age, mark):
        super().__init__(name, age)
        self.mark = {}

    def add_mark(self, subject, score):
        if subject not in self.mark:
            self.mark[subject] = score
            print("Added a new subject")
        else:
            old_score = self.mark[subject]
            self.mark[subject] = score
            print("Updated the score of the subject")
            print("Old_score=", old_score)
            print("New_score=", score)

    def display_marks(self):
        print(self.mark)

    def average(self):
        if len(self.mark) == 0:
            return 0 
        else:
            self.mark
            average = sum(self.mark.values()) / len(self.mark)
            return average

Student_1 = Student("John", 16, {})

Student_1.display_info()

Student_1.add_mark("Math", 86)
Student_1.add_mark("Science", 89)

Student_1.display_marks()

Student_average = Student_1.average()

print(("Average score :"), Student_average)

print(" ")

Student_2 = Student("Leonard", 17, {})

Student_2.display_info()

Student_2.add_mark("Math", 91)
Student_1.add_mark("Science", 90)

Student_2.display_marks()

Student_average = Student_2.average()

print(("Average score :"), Student_average)


# %%



