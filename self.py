class Family: # class

    def familyDetails(self): # method
        self.name = "Natty"
        print("Name = ", self.name)
        age = 30
        print("Age = ", age)

    def printfamilyDetails(self): # another method
        # self.name = "Natty"
        age = 37
        print("Print in another method")
        print("Name : ", self.name)
        print("Age : ", age)

family = Family() # create object to class
family.familyDetails() # call the method
family.printfamilyDetails() # call another method
