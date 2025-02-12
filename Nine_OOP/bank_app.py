from accounts.account import Account

#We have created an account object
# object instantiation
lisa_account = Account(100, 'Lisa', 'Simpson')
print(lisa_account)

bart_account = Account(20, 'Bart', 'Simpson')
print(bart_account)
print(bart_account.first_name)

bart_account.first_name = "Bartholomew"
print(bart_account.first_name)
print(bart_account.get_lastname())
lisa_account.set_lastname("simpson-flanders")
print(lisa_account.first_name + " " + lisa_account.get_lastname())
print("Mangled name of private field:", lisa_account._Account__last_name)

lisa_account.account_holder_name = "Lisa Van-Houten"
print(lisa_account.first_name)
print(lisa_account.get_lastname())
print(lisa_account.account_holder_name)
print(lisa_account.get_balance())
print(bart_account.get_balance())