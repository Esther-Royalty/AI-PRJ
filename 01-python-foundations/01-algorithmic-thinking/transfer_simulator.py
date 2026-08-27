sender_balance = float(input("Enter your current balance: "))
transfer_amount = float(input("Enter amount to transfer: "))

if transfer_amount <= sender_balance:
    sender_balance = sender_balance - transfer_amount
    print("Transfer successful!")
    print("New balance:", sender_balance)
else:
    print("Insufficient funds")