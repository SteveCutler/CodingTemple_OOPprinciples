class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget

    def get_name(self):
        return self.__name
    
    def get_budget(self):
        return self.__budget
    
    def set_name(self, name):
        if len(name)>=1:
            self.__name = name
        else:
            print("Please enter a valid name")

    def set_budget(self, amount):
        if amount >=0 and int(amount):
            self.__budget = amount
        else:
            print("Please enter a valid budget amount")

    def deductExpense(self, expense):
        if self.get_budget() >= expense:
            self.set_budget(self.get_budget() - expense)
            print(f"Expense {expense} registered. Your new budget is {self.get_budget()}!")
        else:
            print(f"Please enter an expense that is less than your total budget of {self.get_budget()}")

    def budgetSummary(self):
        print(f"Your remaining budget for category '{self.get_name()}' is: {self.get_budget()}")


