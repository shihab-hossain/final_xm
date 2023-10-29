
class Account:
    accounts=[]
    total_bank_tk=0
    total_bank_loan=0
    number=1000
    def __init__(self,name, email,address,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=0
        self.trans_history=[]
        self.account_num=Account.generate_account_number()
        Account.accounts.append(self)
        self.loan_lim=2
        self.loan_cnt=0
    @staticmethod
    def generate_account_number():
        Account.number+=1
        return Account.number 
    
    def deposit(self, amount):
        if amount>0:
            self.balance +=amount
            Account.total_bank_tk +=amount
            print(f'\nsuccessfuly deposit the amount:-> {amount}')
            self.trans_history.append(f'deosit:-> {amount}')
        else:
            print('Invalid deposit amount')
        
    def withdraw (self, amount):
        if amount>0 and amount<self.balance:
            self.balance -=amount
            Account.total_bank_tk -=amount
            print(f'\nsuccessfuly withdraw the amount:-> {amount}')
            self.trans_history.append(f'withdraw:-> {amount}')
        else:
            print('Withdrawal amount exceeded')
    
    def check_available_balance(self):
        print(f'\ncurrent balance:-> {self.balance}')

    def Transaction_history(self):
        print(f'-----transaction history-----')
        for histo in self.trans_history:
            print(histo)
    
    def take_loan(self,amount):
        if self.loan_cnt < self.loan_lim:
            if amount>0:
                self.balance +=amount
                self.loan_cnt +=1
                Account.total_bank_loan +=amount
                Account.total_bank_tk -=amount
                print(f'\ntake {amount} tk loan from bank successfully ')
                self.trans_history.append(f'take loan:-> {amount}')
            else:
                print('\nInvalid loan amount')
        else:
            print(f'\nloan limit exceeded')
    
    def transfer_money(self,send_id,amount):
        ac=False
        for id in self.accounts:
            
            if send_id==  id.account_num:
                # print('dhbhb')
                if amount >0 and amount<self.balance:
                    self.balance -=amount
                    id.balance +=amount
                    ac=True
                    print(f'\ntransfer the amount successfully {amount} ')
                    self.trans_history.append(f'transferred:-> {amount}')
                else:
                    ac=True
                    print('\ninvalid transfer amount')
        if ac==False:
            print('\nAccount does not exist')

    def __repr__(self) -> str:
        print('')
        print(f'name:-> {self.name} ,account type:-> {self.account_type}')
        print(f'balance:-> {self.balance} and email is:-> {self.email}')
        print(f'he live in:-> {self.address}')
        print(f'account number is:-> {self.account_num}')
        # print(Account.accounts[0].account_num)
        return ''
 
# ob1=Account('shihab','shihab@.com','kabil','saving')
# ob2=Account('hossain','hossain@.com','gonj','saving')
# ob1.deposit(1000)
# ob1.transfer_money(1003,200)
# print(ob2)

class Admin(Account):
    bank_admin=[]
    def __init__(self,name,id,pas) -> None:
        self.name=name
        self.id=id
        self.pas=pas
        self.accountss=[]
        Admin.bank_admin.append(self)
    # def admins(self,id):
    #     Admin.bank_admin.append(id)
    def delete_users(self,inp):
        ss=False    
        for ids in admin.accountss:
            # print(ids)
            if ids.account_num==inp:
                Account.total_bank_tk -=ids.balance
                admin.accountss.remove(ids)
                Account.accounts.remove(ids)
                # Account.number -=1
                ss=True
            # else:
            #     print(f' this account does ont in your list')
            # if inp in ids.account_num:
            #     # admin.accountss.remove(inp)
            #     print(inp)
            #     break
        if ss==True:
            print('\naccount delete successful')
        else:
            print('\nthis account does not in our list')


admin=None
user=None
while True:
    print('1. ADMIN')
    print('2. USER')
    print('3. EXIT')
    print('\nHOW ARE YOU!!!')
    op=int(input('chose your option:'))
    if op==1:
        while True:
            if admin==None:
                print('\n-----hi admin-----')
                ch=input('Register/Login (R/L) : ')
                if ch=='R':
                    print('ADMIN INFO-> NAME:Sha , ID:Admin , PASS:admin123')
                    name=input('admin name:')
                    ide=input('admin id:')
                    pas=input('admin pass:')
                    admin=Admin(name,ide,pas)
                elif ch=='L':
                    print('ADMIN INFO-> NAME:Sha , ID:Admin , PASS:admin123')
                    na=input('admin name:')
                    sa=input('admin id:')
                    de=input('admin pas:')
                    for adm in Admin.bank_admin:
                        if adm.name==na and adm.id==sa and adm.pas:
                            admin=adm

            else:
                print('\n----welcome admin----')
                print('1. create an account for user')
                print('2. delete any user account')
                print('3. all user account list')
                print('4. total available balance of the bank')
                print('5. total loan amount')
                print('6. no or off loan feature of the bank')
                print('7. exit\n')
                ope=int(input('chose option:'))
                if ope==1:
                    ne=input('name:')
                    em=input('email:')
                    ad=input('address:')
                    ac=input('account type:')
                    acco=Account(ne,em,ad,ac)
                    admin.accountss.append(acco)
                    print('\naccount create successfulu!!!!')
                    print(acco)
                elif ope==2:
                    inp=int(input('give account number:'))
                    admin.delete_users(inp)
                    
                elif ope==3:
                    print('=====ALL ACCOUNT IN OUR BANK LIST=====')
                    for person in admin.accountss:
                        print(person)
                elif ope==4:
                    print(f'\nbank has total money:-> {admin.total_bank_tk}')   
                elif ope==5:
                    print(f'\nbank give total loan:-> {admin.total_bank_loan}')
                elif ope==7:
                    admin=None
                    break
    elif op==2:
        while True:
            if user==None:
                print('\n---------give your information for login---------')
                ne=input('user name:')
                em=input('user email:')
                ad=input('user address:')
                ac=input('user account type:')   
                u=False         
                for use in Account.accounts:
                    if use.name==ne and use.email==em and use.address==ad and use.account_type==ac:
                        user=use
                        u=True
                if u==False:
                    print('for your given information we can not find any account?????')
            else:
                print('\n-------HI USER-------')
                print('1. deposit tk in your account')
                print('2. withdrawl tk from your account')
                print('3. your available balance')
                print('4. your all transaction')
                print('5. take loan from bank')
                print('6. transfer tk another account')
                print('7. exit\n')
                a=int(input('option:'))
                if a==1:
                    b=int(input('give your deposit amount: '))
                    user.deposit(b)
                elif a==2:
                    c=int(input('give the amount you can withdraw: '))
                    user.withdraw(c)
                    
                elif a==3:
                    user.check_available_balance()
                elif a==4:
                    user.Transaction_history()
                elif a==5:
                    tk=int(input('how mutch tk do you need: '))
                    if tk < Account.total_bank_tk:
                        user.take_loan(tk)
                    else:
                        print('bank does not enough money sorry!!')
                elif a==6:
                    d=int(input('give transfer account number: '))
                    e=int(input('give the amount you can transfer: '))
                    user.transfer_money(d,e)
                elif a==7:
                    user=None
                    break
    elif op==3:
        print('\n----------BYE COME AGAIN----------')
        break 

    
         



