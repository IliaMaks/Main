import functions

budget_data = {
 "balance": 300,
 "transactions": {("income", 1000, "Salary"), ("expense", 500, "Rent"), ("expense", 200,
"Groceries")}
}

print("Budget Manager")
print("1.Add Income")
print("2.Add Expense")
print("3.Show Balance")
print("4.Show Transaction History")
print("5.Exit")


pick=""


while pick!=5 :
        pick=int(input(f"Please choose the option : " )) 
        def ch_option (pick) :
                match pick :
                   case 1 :
                     functions.AddIncome(budget_data)
                   case 2 :
                      functions.AddExpense(budget_data)
                   case 3 :
                      functions.ShowBalance(budget_data)
                   case 4 :
                      functions.ShowTransactionHistory(budget_data)
                   case 5 :
                       print("Exiting the program")
        ch_option(pick)            