per_cent = {'BBVA': 5.6, 'ING': 5.9, 'BDE': 4.28, 'CAIXA': 4.0}
money = int(input("Enter the amount you plan to deposit at interest: "))
deposit = [int(money * rate / 100) for rate in per_cent.values()]
max_deposit = max(deposit)
print("Deposits in banks:", deposit)
print("The maximum amount you can earn is:", max_deposit)
