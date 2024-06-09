job_grade=""
basic_salary=""
house_allowance=""
travel_allowance=""
gross_salary=basic_salary+house_allowance+travel_allowance
class employee:
def employee_details(self):
self.name=input("Employee name:\t")
self.gender=input("Employee gender:\t")
self.jobgrade=input("Employee jobgrade:\t)
def display(self):
print("Name", "Gender", "Job Grade")
print(self.name, self.gender, self.jobgrade)
if job_grade=="H":
basic_salary=18000
house_allowance=2000
travel_allowance=3000
elif job_grade=="M":
basic_salary=18000
elif job_grade=="S":
basic_salary=60000
house_allowance=40000
travel_allowance=12000
def gross_income(self):
gross_salary=basic_salary+house_allowance+travel_allowance
print("Gross salary is:\t", gross_salary)
k=employee()
k.employee_details()
k.display()
k.gross_income()
