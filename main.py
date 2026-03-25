customer={}
customer_name=[]
permanent_id=0
def acc_creater():
    global permanent_id
    permanent_id=permanent_id+1
    try:
        name=input("Enter name : ")
        i_amount=int(input("Enter initial amount to create account : "))
        if i_amount<0 :
            raise ValueError("Number is Negative !")
    except ValueError as msg :
        print(msg)
    customer[permanent_id]=i_amount
    customer_name.append(name)
def acc_detail():
    k=0
    for i,j in customer.items():
        print(f"{i} : {customer_name[k]},{j}")
        k=k+1
def transfer_money():
    try:
        u_id=int(input("Enter your id : "))
        s_id=int(input("Enter sender id to tansfer money : "))
        money=int(input("Enter amount to transfer : "))
    except ValueError:
        print("Enter correct id or money")
    for s_id in customer.keys():
        customer[u_id]=customer[u_id]-money
        customer[s_id]=customer[s_id]+money
    print("Transfered Success :) ")
def withdraw_money():
    id=int(input("Enter your id : "))
    money=int(input("Enter amount to withdraw : "))
    customer[id]=customer[id]-money
    print("Withdraw Success :) ")
while True:
    try:
        choice=int(input('''
1.Create Account
2.View Account Details
3.Transfer money
4.Withdraw money
4.Exit
Enter your choice : '''))
    except ValueError:
        print("Enter correct value !")
    if choice==1:
        acc_creater()
    elif choice==2:
        acc_detail()
    elif choice==3:
        transfer_money()
    elif choice==4:
        withdraw_money()
    elif choice==5:
        break
    else:
        pass