import math


class Category:
    def __init__(self, name):
        self.category = name
        self.ledger = []
        self.balance = 0.00

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, "Transfer to %s" % category.category)
            category.deposit(amount, "Transfer from %s" % self.category)
            return True

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        category_name = f'{self.category:*^30}'
        finalstr = f'{category_name}\n'
        for transaction in self.ledger:
            finalstr += f'{transaction["description"][:23]:<23}{transaction["amount"]:>7.2f}\n'
        finalstr += f'Total: {self.get_balance():.2f}'

        return finalstr


def create_spend_chart(categories):
    total_spent = 0
    chart = "Percentage spent by category\n"
    categories_array = []
    total_in_category = 0

    for category in categories:
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                total_spent += abs(transaction["amount"])
                total_in_category += abs(transaction["amount"])
        categories_array.append(total_in_category)
        total_in_category = 0

    for percentage in range(10, -1, -1):
        marks_for_category = ["", "", "", ""]
        for total in range(len(categories_array)):
            if math.floor(categories_array[total] / total_spent *100) >= percentage * 10:
              marks_for_category[total] = "o"
        
        chart += f'{percentage *10:>3}|{marks_for_category[0]:>2}{marks_for_category[1]:>3}{marks_for_category[2]:>3}{marks_for_category[3]:>2}\n'

    chart += '    {0:->{length}s}'.format("",length = len(categories)*3 +1)
    
    print(chart)

    return chart
