def AddIncome (data):
      print ("AddIncome")
      amount = int(input("Please enter new Income amount: "))
      type = input("Please enter type of income: ")
      data["balance"] += amount
      data["transactions"].add(("income", amount, type))
      
      print(data)
      return data

def AddExpense(data):
      print ("AddExpense")
      amount = int(input("Please enter new expense amount: "))
      type = input("Please enter type of expense: ")
      data["balance"] -= amount
      data["transactions"].add(("expense", amount, type))
      
      print(data)
      return data

def ShowBalance (data):
      print ("ShowBalance")
      print(data["balance"])

def ShowTransactionHistory (data):
      print ("ShowTransactionHistory")
      for transaction in data["transactions"]:
            print(transaction) 

