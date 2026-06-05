#customer trasaction store 
transaction= [5000, -2000, 3000, -1000, -500, 7000]
balance = 0
Deposit=[]
Withdrawal=[]
for i in transaction:
    balance += i  #balance is updated with each transaction
print("Current Balance:", balance)         #total balance is displayed

for i in transaction:
    if i > 0:  #deposits are displayed
        Deposit.append(i)   
    else:  #
        Withdrawal.append(-i)

print("Deposits:", Deposit)
print("Withdrawals:", Withdrawal)   
print("largest Deposit:", max(Deposit))  #largest deposit is displayed
print("largest Withdrawal:", max(Withdrawal))  #largest withdrawal is displayed