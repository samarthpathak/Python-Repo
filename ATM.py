d1={11:"Mohan",12:"Ram",13:"Dhanush"}
d2={11:1234,12:5555,13:6789}
d3={11:25000,12:45600,13:55000}

a=int(input("What would you like to do today?\n1.Login\n2.Register\n"))
if a==2:
    name=str(input("Enter your name\n"))
    amount=int(input("Enter the amount youw want to deposit\n"))
    s=int(input("Enter the pin\n"))
    idl=list(d1.keys())
    id2=idl[-1]+1
    d1[id2]=name
    d3[id2]=amount
    d2[id2]=s
    print(d1[id2],d2[id2],d3[id2])

m=int(input("Enetr your User Id\n"))
n=int(input("Enter the pin\n"))
if d2[m]==n:
    k=0
    i="Y"
    while i!="N":
        k=int(input("Please choose one of the following options\n1.Check balance\n2.Withdraw amount\n3.Deposit amount\n4.Change Pin\n5.Exit\n"))
        if(k==1):
            print("Your current balance is ",d3[m])
        elif(k==2):
            s=int(input("Enter the amount to be withdrawn: "))
            if s<d3[m]:
                d3[m]=d3[m]-s
                print("Total Balance remaining : ",d3[m])
            else:
                print("Insufficient Balance")
        elif(k==3):
            s=int(input("Enter the amount to be depositted: "))
            d3[m]=d3[m]+s
            print("Total Balance: ",d3[m])
        elif(k==4):
            s,r=0,-1
            while(s!=r):
                s=int(input("Enter new pin :"))
                r=int(input("Enter confirm new pin :"))
                if s==r:
                    d2[m]=s
                    print("Pin changed successfully\n")
                else:
                    print("Pin and Confirm new pin didn't match\n")
        else:
            break
        i=str(input("Do you wish to continue? Y/N\n"))
else:
    print("Incorrect Pin")
