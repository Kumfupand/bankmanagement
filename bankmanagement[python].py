import mysql.connector
mydb=mysql.connector.connecct(host='local host',user='root',password='sathish@45',database='bms')
def open_account():
  name=input("enter your name:")
  acc=input("enter your account:")
  dob=input("enter your dob:")
  add=input("enter your address:")
  con=input("enter your contact:")
  op_bal=int("enetr your opening balance:")
  data1=(name,acc,dob,add,con,op_bal)
  data2=(name,acc,op_bal)
  sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
  sql2=('insert into ammount values(%s,%s,%s)')
  x=mydb.corsor()
  x=execute(sql1,data1)
  x.execute(sql2,data2)
  mydb.commit()
print("data entered succesfully")
main()
def deposite():
  amount=input("enter the amount to be deposited:")
  acc=input("enter your acc no:")
  a="select balance from ammount where acc_no=%s"
  data1=(acc)
  x=mydb.corsor()
  x.execute(a,data1)
  result=x.fetchone()
  t=result[0]+amount
  sql=('update ammount sey balance where acc_no=%s')
  d=(t,acc)
  x.execute(sql,d)
  mydb.commit()

print("_____________________________________________")
main()
def withdraw():
  amount=input("enter the amount to withdraw:")
  acc=input("enter your acc no")
  a="select balance from ammount where acc_no=%s"
  data1+(acc1)
  x=mydb.corsor()
  x.execute(a,data1)
  result=x.fetchone()
  t=result[0]-amount
  sql=('update amount set balance where acc_no=%s')
  d=(t,acc)
  x.execute(sql,d)
  mydb.commit()

print("___________________________________________")
main()
def balance():
  acc:input("enter the account number:")
  a="select"*"from ammount whre acc_no=%s"
  data=(ac1)
  x=mydb.corsor()
  x.execute(a,data)
  mydb.commit             
                    

       
