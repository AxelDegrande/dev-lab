while True:
    try:
        print("What is your income:")
        income = int(input("> "))
        break
    except ValueError:
        print("That's not an int!")

if income <= 10000:
    print("Your income is not taxed!")
    print(f"Income: {income} euro, Tax: 0 euro, Remaining: {income}")
elif income > 10000:
    incomeAfterFirstTax = income - 10000
    taxOnFirstIncome = incomeAfterFirstTax * 0.1
    if incomeAfterFirstTax > 10000:
        incomeAfterSecondTax = incomeAfterFirstTax - 10000
        taxOnSecondIncome = incomeAfterSecondTax * 0.2
        print(f"For an income of {income}: the first 10k is free, the next 10k is taxed at 10% ({taxOnFirstIncome}), and the remaining {incomeAfterSecondTax} is taxed at 20% ({taxOnSecondIncome}).")
    else:
        print(f"For an income of {income}: the first 10k is free, the next 10k is taxed at 10% ({taxOnFirstIncome})")        