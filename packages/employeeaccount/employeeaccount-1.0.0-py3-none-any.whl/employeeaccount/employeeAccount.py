# Employee class Creation
class Employee:
    # Define a class attribute
    MIN_SALARY = 30000 #<--- no self.

    def __init__(self, name, salary):
        try:
            if(name==''):
                raise Exception('name must be not empty')
            else: 
               self.name = name
        except Exception as e:
            self.name = 'Anonymous'
            print(e)
        # Use   class name to access class attribute
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
    # reimplementing __repr__ for printing        
    def __repr__(self):
        return """Employee('{name}', {salary})""".format(name=self.name,salary=self.salary)
      
    # implementing __eq__()  
    def __eq__(self, other):
        # Diagnostic printout
        print("__eq__() is called")
        # Returns True if all attributes match
        return (self.name == other.name) and \
               (self.salary == other.salary) 

    def  increase_salary_rate(self, cur_salary, salary_increase):
        try:
             return 100*(salary_increase / cur_salary)
        except (ZeroDivisionError, TypeError, ValueError) as e:
             print(e)    

# BankAccount class Creation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
      
    def withdraw(self, amount):
        self.balance -= amount

# SavingAccount class inherited from BankAccount
class SavingsAccount(BankAccount):
  """ Constructor speficially for SavingsAccount 
      with an additional attribut"""
  def __init__(self, balance, interest_rate):
    # Call the parent constructor using ClassName.
    BankAccount.__init__(self, balance) 
    # Add more functionality
    self.interest_rate = interest_rate

  # New functionality
  def compute_interest(self, n_periods = 1):
    return self.balance * ( (1 + self.interest_rate) ** n_periods - 1)

# CheckingAccount class inherited from BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        super(BankAccount, balance).__init__(self, balance)
        # Add more functionality
        self.limit = limit
    # New method
    def deposit(self, amount):
        self.balance += amount
    # Modify method
    def withdraw(self, amount, fee=0):
        if fee <= self.limit:
            BankAccount.withdraw(self, amount - fee)
        else:
            BankAccount.withdraw(self,
                                 amount - self.limit)
