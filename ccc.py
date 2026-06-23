class Company:
    company_name = "TechSoft"
   
    def show(self,name="Hello"):
        self.company_name=name
        print(self.company_name)
emp1 = Company()
emp2 = Company()
emp1.show("PYTHON")
emp2.show()
# Output: TechSoft