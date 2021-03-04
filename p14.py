balance = 5000
print("Note---> \nw for 'Withdraw' , \nc for 'Check balance', \nd for 'Deposit'")
print("\n")
key = input("Enter any key which are mention in above note : ")
if(key == 'w'):
    amt = int(input("Enter amount : "))
    if(amt<balance):
        if(amt<500):
            print("Amount must be greater than 500")
        else:
                  print("Transaction Successfull!")
                  total = balance -amt
                  print("\nAvailable balance : ",total)        
    else:
        print("Transaction can not be!")
elif(key=='d'):
    amt2 = int(input("Enter amout : "))
    balance = balance +amt2
    print("Successfull Deposit! Now your available balance : ",balance)
elif(key=='c'):
    print("Your balance : ", balance)
    
