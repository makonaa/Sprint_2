class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name:str, hours:int, rest_days:int, email:str):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name:str, rest_days:int, email:str) -> 'EmployeeSalary':
        hours =  (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name:str, hours:int, rest_days:int) -> 'EmployeeSalary':
        email = f'{name}@email.com'
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_pay:int) -> None:
        cls.hourly_payment = new_hourly_pay
        return None

    def get_salary(self) -> int:
        salary = self.hours*self.hourly_payment
        return salary

#test employees to check class methods
employee1 = EmployeeSalary.get_hours('Jane', 3, 'janedoe@email.com')
employee2 = EmployeeSalary.get_email('John', 40, 2)
print(employee1.__dict__)
print(employee2.__dict__)
print(employee2.get_salary())
EmployeeSalary.set_hourly_payment(500)
print(employee2.get_salary())