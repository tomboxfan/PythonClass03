
is_bank_customer = input("如果您是本行客户，请按1；如果您不是本行客户，请按2: ")
service_type = input("信用卡服务，请按1；贷款服务，请按2；银行卡挂失，请按3: ")
print(is_bank_customer, service_type)

print("-------------------------------------------------")

account_type = input("1 - current account, 2 - saving account: ")
service_type = input("1 - show me the balance, 2 - withdraw money, 3 - deposit money: ")
withdraw_amount = int(input("Withdraw amount: "))

print(account_type, service_type, withdraw_amount)

print("-------------------------------------------------")

value = input()
print(value)


month = input("Month: ")
day = input("Day: ")
year = input("Year: ")
print(f"today's date is {month} {day}, {year}")

