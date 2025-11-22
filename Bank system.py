from tkinter import *
from tkinter import messagebox
import sqlite3

win = Tk()
win.geometry("1530x790+0+0")

username = StringVar()
password = StringVar()

t8 = StringVar()
empid=StringVar()
empname = StringVar()
empfather = StringVar()
empaddress = StringVar()
empmail = StringVar()
empdesg = StringVar()
empsal = StringVar()
empsalary=StringVar()

cusername = StringVar()
cmail = StringVar()
ccontact = StringVar()
ccomplaint = StringVar()
csuggestion = StringVar()

acno = StringVar()
acctype = StringVar()
username = StringVar()
address = StringVar()
crbalance = StringVar()
withdraw = StringVar()
balance = StringVar()
date = StringVar()
initialamt = StringVar()
currentamt=StringVar()
withdrawmoney=StringVar()
depositemoney=StringVar()

mail = StringVar()
contact = StringVar()
altcontact = StringVar()
suggestion = StringVar()

def signup():
    ins = sqlite3.connect("project3.db")
    usernames = username.get()
    passwords = password.get()

    if (usernames==""):
        messagebox.showinfo("Banking Management System", "Please enter username")
    elif (passwords==""):
        messagebox.showinfo("Banking Management System", "Please enter password")
    else:
        ins.execute("create table if not exists login(username char(20) not null, password cgar(20) not null);")
        ins.execute("insert into login(username, password) values (?,?)", (usernames, passwords,));
        messagebox.showinfo("SIGNUP COMPLETE", "You are registered user")
        ins.commit()

def login():
    usernames=username.get()
    passwords=password.get()
    ins = sqlite3.connect("project3.db")

    if (usernames==""):
        messagebox.showinfo("Banking Management", "Please enter the username")
    elif (passwords==""):
        messagebox.showinfo("Banking Management", "Please enetr the password")
    else:
        show = ins.execute("select * from login where USERNAME = ? AND PASSWORD = ?", (usernames, passwords,))
        if show.fetchone() is None:
            messagebox.showinfo("Signup Process", "Please enter the correct username and password")
        else:
            messagebox.showinfo("Signup Process", "You are administrator of the project") 
            flog.grid_forget()
            fmain.grid(row=0, padx=120, pady=100)
    
def complaint():
    fmain.grid_forget()
    fcomp.grid(row=0, padx=200, pady=200)
        
def suggestion():
    fmain.grid_forget()
    fsugg.grid(row=0, padx=200,pady=200)

def account():
    facmt.grid(row=0, padx=200, pady=200)
    fmain.grid_forget()

def previous():
    facmt.grid_forget()
    fmain.grid(row=0, padx=200, pady=200)

def save():
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    
    ins=sqlite3.connect('project3.db')


    if (acnos==""):
        messagebox.showinfo("Banking Management", "Please enter the account number")
    elif(empnames==""):
        messagebox.showinfo("Banking Management","Please enter the employee names")
    elif(empfathers==""):
        messagebox.showinfo("Banking Management","Please enter the father name")
    elif(acctypes==""):
        messagebox.showinfo("Banking Management","Please enter the account type")
    elif(empmails==""):
        messagebox.showinfo("Banking Management","Please enter the emails")
    elif(empaddresses==""):
        messagebox.showinfo("Banking Management","Please enter the address")
    elif(contacts==""):
        messagebox.showinfo("Banking Management","Please enter the contact")
    elif(altcontact==""):
        messagebox.showinfo("Banking Management","Please enter the alternative contact")
    elif(dates==""):
        messagebox.showinfo("Banking Management","Please enter the date")
    elif(initialamts==""):
        messagebox.showinfo("Banking Management","Please enter the initial amount")
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists employeedata(acno char(20) not null primary key,empname char(30) not null,empfather char(20) not null,acctype char(20) not null,empmail char(20) not null,empaddress char(20) not null,contact char(20) not null,gender,altcontact char(20) not null,date char(20) not null, initialamt char(20) not null);")
        ins.execute("insert into  employeedata(acno,empname,empfather,acctype,empmail,empaddress,contact,gender,altcontact,date,initialamt) values(?,?,?,?,?,?,?,?,?,?,?)",(acnos,empnames,empfathers,acctypes,empmails,empaddresses,contacts,gender,altcontacts,dates,initialamts,));
        messagebox.showinfo('Banking Project','Employee Data Saved')
        ins.commit()

def savewithdraw():
    acnos=acno.get()
    usernames=username.get()
    addresses=address.get()
    crbalances=crbalance.get()
    withdrawmoneys=withdrawmoney.get()
    balances=balance.get()
    dates=date.get()
    
    ins=sqlite3.connect('project3.db')
    
    if (acnos==""):
        messagebox.showinfo("Banking Management", "Please enter the account number")
    elif(usernames==""):
        messagebox.showinfo("Banking Management","Please enter the usernames")
    elif(addresses==""):
        messagebox.showinfo("Banking Management","Please enter the address")
    elif(crbalances==""):
        messagebox.showinfo("Banking Management","Please enter the current amount")
    elif(withdrawmoneys==""):
        messagebox.showinfo("Banking Management","Please enter the withdrawn money")
    elif(balances==""):
        messagebox.showinfo("Banking Management","Please enter the balance")
    elif(dates==""):
        messagebox.showinfo("Banking Management","Please enter the date")
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists withdrawal(acno char(20) not null primary key,username char(30) not null,address char(20) not null,crbalance char(20) not null,withdrawmoney char(20) not null,balance char(20) not null,date char(20) not null);")
        ins.execute("insert into  withdrawal(acno,username,address,crbalance,withdrawmoney,balance,date) values(?,?,?,?,?,?,?)",(acnos,usernames,addresses,crbalances,withdrawmoneys,balances,dates,));
        messagebox.showinfo('Banking Project','Withdrawal Data Saved')
        ins.commit()

def savedeposite():
    acnos=acno.get()
    usernames=username.get()
    addresses=address.get()
    crbalances=crbalance.get()
    depositemoneys=depositemoney.get()
    balances=balance.get()
    dates=date.get()
    
    ins=sqlite3.connect('project3.db')
    
    if (acnos==""):
        messagebox.showinfo("Banking Management", "Please enter the account number")
    elif(usernames==""):
        messagebox.showinfo("Banking Management","Please enter the usernames")
    elif(addresses==""):
        messagebox.showinfo("Banking Management","Please enter the address")
    elif(crbalances==""):
        messagebox.showinfo("Banking Management","Please enter the current amount")
    elif(depositemoneys==""):
        messagebox.showinfo("Banking Management","Please enter the deposite money")
    elif(balances==""):
        messagebox.showinfo("Banking Management","Please enter the balance")
    elif(dates==""):
        messagebox.showinfo("Banking Management","Please enter the date")
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists deposition(acno char(20) not null primary key,username char(30) not null,address char(20) not null,crbalance char(20) not null,depositemoney char(20) not null,balance char(20) not null,date char(20) not null);")
        ins.execute("insert into  deposition(acno,username,address,crbalance,depositemoney,balance,date) values(?,?,?,?,?,?,?)",(acnos,usernames,addresses,crbalances,depositemoneys,balances,dates,));
        messagebox.showinfo('Banking Project','Deposition Data Saved')
        ins.commit()
    

def update():
    ins=sqlite3.connect('project3.db')
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    ins.execute("update employeedata set empname=?,empfather=?, acctype=?, empmail=?, empaddress=?, contact=?, gender=?, altcontact=?, date=?, initialamt=? where acno=?",(empnames, empfathers, acctypes, empmails, empaddresses, contacts, gender, altcontacts, dates, initialamts,acnos,));
    messagebox.showinfo('Employee database','Employee Record Updated')
    ins.commit()                        

def search():
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    ins=sqlite3.connect('project3.db')
    show=ins.execute("select * from employeedata where acno=?", (acnos,))
    if show.fetchone() is None:
        messagebox.showinfo("Employee database", "Data doesnot exist")
    else:
        show=ins.execute("select * from employeedata where acno=?", (acnos,))
        for row in show:
            acno.set(row[0])
            empname.set(row[1])
            empfather.set(row[2])
            acctype.set(row[3])
            empmail.set(row[4])
            empaddress.set(row[5])
            contact.set(row[6])
            t8.set(row[7])
            altcontact.set(row[8])
            date.set(row[9])
            initialamt.set(row[10])
            print(row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7]," ",row[8]," ",row[9]," ",row[10]) 
            messagebox.showinfo("Employee database", "Employee Record Found")
    ins.commit()
    
def allaccount():
    ins=sqlite3.connect('project3.db')
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()

    show=ins.execute("select * from employeedata")
    
    for row in show:
        print(
            row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7]," ",row[8]," ",row[9]," ",row[10])
            
        print("welcome")
        messagebox.showinfo("Employee database", "All Employee Data")


def seeall():
    ins=sqlite3.connect('project3.db')
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    see=ins.execute("select * from employeedata")
    for row in see:
        acno.set(row[0])
        empname.set(row[1])
        empfather.set(row[2])
        acctype.set(row[3])
        empmail.set(row[4])
        empaddress.set(row[5])
        contact.set(row[6])
        t8.set(row[7])
        altcontact.set(row[8])
        date.set(row[9])
        initialamt.set(row[10])
        messagebox.showinfo("Employee database", "All Employee Data")


def allemployee():
    ins=sqlite3.connect('project3.db')
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsal.get()
    gender=t8.get()
    all=ins.execute("select * from employees")
    for row in all:
        empid.set(row[0])
        empname.set(row[1])
        empfather.set(row[2])
        empaddress.set(row[3])
        empmail.set(row[4])
        empdesg.set(row[5])
        empsalary.set(row[6])
        t8.set(row[7])
        messagebox.showinfo("Employee database", "All Employee Data")
    ins.commit()
    
def exit():
    fwithdraw.grid_forget()
    facmt.grid_forget()
    fcomp.grid_forget()
    fadcomp.grid_forget()
    fsugg.grid_forget()
    fdeposite.grid_forget()
    fmain.grid_forget()
    fthank.grid(row=0, padx=200, pady=200)

def deposite():
    fdeposite.grid(row=0, padx=120, pady=100)
    facmt.grid_forget()

def delete():
    acnos=acno.get()
    ins=sqlite3.connect('project3.db')
    ins.execute("delete from employeedata where acno=?", (acnos,))
    ins.commit()
    messagebox.showinfo("Employee database", "Employee Record Deleted")

def deleteemployee():
    empids=empid.get()
    ins=sqlite3.connect('project3.db')
    ins.execute("delete from employees where empid=?", (empids,))
    ins.commit()
    messagebox.showinfo('Banking Management','Permanently deleted the employee data')
    
def searchemployee():
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsal.get()
    gender=t8.get()
    
    if(empids==""):
        messagebox.showinfo("Banking Management","Please enter the employee id")
    else:
        ins=sqlite3.connect('project3.db')
        empids=empid.get()
        show=ins.execute("select * from employees where empid=?",(empids,))
        if show.fetchone() is None:
            messagebox.showinfo("Banking Management", "Data doesnot exist")
        else:
            ins=sqlite3.connect('project3.db')
            show=ins.execute("select * from employees where empid=?",(empids,))
            for row in show:
                empid.set(row[0])
                empname.set(row[1])
                empfather.set(row[2])
                empaddress.set(row[3])
                empmail.set(row[4])
                empdesg.set(row[5])
                empsalary.set(row[6])
                t8.set(row[7])
                
            messagebox.showinfo('Banking Management','Employee Data Found')
        ins.commit()
    
def savesuggestion():
    cusernames=cusername.get()
    cmails=cmail.get()
    ccontacts=ccontact.get()
    csuggestions=csuggestion.get()
    
    if(cusernames==""):
        messagebox.showinfo('banking management','please enter the username')
    elif(cmails==""):
        messagebox.showinfo('banking management','please enter the emailid')
    elif(ccontacts==""):
        messagebox.showinfo('banking management','please enter the contacts')
    elif(csuggestions==""):
        messagebox.showinfo('banking management','please enter the Suggestion')
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists suggestions(usernames char(20) not null,mails char(30) not null,contact char(20) not null,suggestion char(30) not null);")
        ins.execute("insert into suggestions(usernames,mails,contact,suggestion) values(?,?,?,?)",(cusernames,cmails,ccontacts,csuggestions,));
        messagebox.showinfo('banking management',cusernames+'  '+cmails+'  '+ccontacts+' '+csuggestions)
        messagebox.showinfo('Banking Project','Suggestion Save')
        ins.commit()

def suggestionclear():
    cusername.set("")
    cmail.set("")
    ccontact.set("")
    csuggestion.set("")
    
def clearemployees():
    messagebox.showinfo('Banking Management','Employee Data Cleared')
    empid.set("")
    empname.set("")
    empfather.set("")
    empaddress.set("")
    empmail.set("")
    empsalary.set("")

def depositeclear():
    acno.set("")
    username.set("")
    address.set("")
    crbalance.set("")
    depositemoney.set("")
    balance.set("")
    date.set("")

def previous1():
    facc.grid_forget()
    facmt.grid(row=0, padx=200, pady=200)
    
def previous2():
    femp.grid_forget()
    fmain.grid(row=0, padx=200, pady=200)


import sqlite3
from tkinter import messagebox

def saveemployee():
    # Get input from user
    empids = empid.get()
    empnames = empname.get()
    empfathers = empfather.get()
    empaddresses = empaddress.get()
    empmails = empmail.get()
    empdesgs = empdesg.get()
    empsals = empsalary.get()
    gender = t8.get()

    # Validate inputs
    if not empids:
        messagebox.showinfo("Banking Management", "Please enter the employee ID")
        return
    elif not empnames:
        messagebox.showinfo("Banking Management", "Please enter the employee name")
        return
    elif not empfathers:
        messagebox.showinfo("Banking Management", "Please enter the father's name")
        return
    elif not empaddresses:
        messagebox.showinfo("Banking Management", "Please enter the employee address")
        return
    elif not empmails:
        messagebox.showinfo("Banking Management", "Please enter the email")
        return
    elif not empdesgs:
        messagebox.showinfo("Banking Management", "Please enter the designation")
        return
    elif not empsals:
        messagebox.showinfo("Banking Management", "Please enter the salary")
        return
    elif not gender:
        messagebox.showinfo("Banking Management", "Please select the gender")
        return

    # Connect to database
    try:
        conn = sqlite3.connect('project3.db')
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute("""CREATE TABLE IF NOT EXISTS employees(empid CHAR(20) NOT NULL PRIMARY KEY,empname CHAR(30) NOT NULL,empfather CHAR(20) NOT NULL,empaddress CHAR(30) NOT NULL,empmail CHAR(30) NOT NULL,empdesg CHAR(200) NOT NULL,empsalary CHAR(30) NOT NULL,gender CHAR(10))""")

        # Check if empid already exists
        cursor.execute("SELECT * FROM employees WHERE empid = ?", (empids,))
        if cursor.fetchone():
            messagebox.showinfo("Banking Management", "Employee ID already exists. Please use a unique ID.")
            return

        # Insert new employee record
        cursor.execute("""
            INSERT INTO employees(empid, empname, empfather, empaddress, empmail, empdesg, empsalary, gender)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (empids, empnames, empfathers, empaddresses, empmails, empdesgs, empsals, gender))
        
        # Commit changes and show success message
        conn.commit()
        messagebox.showinfo('Banking Project', 'Employee data saved successfully!')

    except sqlite3.IntegrityError as e:
        messagebox.showerror("Banking Management", f"Integrity Error: {e}")
    except sqlite3.OperationalError as e:
        messagebox.showerror("Banking Management", f"Operational Error: {e}")
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


def updateemployee():
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsalary.get()
    gender=t8.get()

    if (empids==""):
        messagebox.showinfo("Banking Management", "Please enter the employee id")
    elif(empnames==""):
        messagebox.showinfo("Banking Management","Please enter the employee names")
    elif(empfathers==""):
        messagebox.showinfo("Banking Management","Please enter the father name")
    elif(empaddresses==""):
        messagebox.showinfo("Banking Management","Please enter the employee address")
    elif(empmails==""):
        messagebox.showinfo("Banking Management","Please enter the emails")
    elif(empsals==""):
        messagebox.showinfo("Banking Management","Please enter the employee salary")
    else:
        ins=sqlite3.connect('project3.db')                                                                                                                                                                               
        ins.execute("update employees set empname=?,empfather=?,empaddress=?,empmail=?,empsalary=?,gender=? where empid=?",(empnames,empfathers,empaddresses,empmails,empsals,gender,empids));
        messagebox.showinfo('Banking Project','Employee Data Updated')
        ins.commit()

def previous3():
    fcomp.grid_forget()
    fmain.grid(row=0, padx=200, pady=200)

def addcomplaint():
    fadcomplaint.grid(row=0, padx=200, pady=200)
    fcomp.grid_forget()

def showcomplaints():
    ins=sqlite3.connect('project3.db')
    show=ins.execute("select * from complaints")
 
    for row in show:
        print(row[0]+'   '+row[1]+'   '+row[2]+'  '+row[3])

    ins.commit()

def savecomplaint():
    cusernames=cusername.get()
    cmails=cmail.get()
    ccontacts=ccontact.get()
    complaints=ccomplaint.get()

    if (cusernames==""):
        messagebox.showinfo('Banking Management', 'Please enter the username')
    elif (cmails==""):
        messagebox.showinfo('Banking Management', 'Please enter the email')
    elif(ccontacts==""):
        messagebox.showinfo('Banking Management','Please enter the contacts')
    elif(complaints==""):
        messagebox.showinfo('Banking Management','Please enter the complaint')
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists complaints(usernames char(20) not null,mails char(30) not null,contact char(20) not null,ccomplaint char(30) not null);")
        ins.execute("insert into complaints(usernames,mails,contact,ccomplaint) values(?,?,?,?)",(cusernames,cmails,ccontacts,complaints,));
        messagebox.showinfo('Banking Management',cusernames+'  '+cmails+'  '+ccontacts+' '+complaints)
        messagebox.showinfo('Banking Project','Complaint Saved')
        ins.commit()   

def complaintclear():
    cusername.set("")
    cmail.set("")
    ccontact.set("")
    ccomplaint.set("")

def withdrawclear():
    acno.set("")
    username.set("")
    address.set("")
    crbalance.set("")
    withdrawmoney.set("")
    balance.set("")
    date.set("")

def reset():
    username.set("")
    password.set("")

def createaccount():
    facc.grid(row=0)
    facmt.grid_forget()

def withdraw():
    fwithdraw.grid(row=0,padx=120,pady=70)
    facmt.grid_forget()

def clears():
    username.set("")
    password.set("")

def addcomplaint():
    fadcomp.grid(row=0,padx=130,pady=100)
    fcomp.grid_forget()

def employee():
    femp.grid(row=0)
    fmain.grid_forget()

def deleteemployee():
     empids=empid.get()
     if(empids==""):
         messagebox.showinfo("Banking Management","Please enter the employee id")
     else:
         empids=empid.get()
         ins=sqlite3.connect('project3.db')
         ins.execute("delete from employees where empid=?",(empids,))
         messagebox.showinfo('Banking Management','Permanently deleted the employee data')

def showsuggestion():
    ins=sqlite3.connect('project3.db')
    show=ins.execute("select * from suggestions")
    
    for row in show:
        print(row[0]+'   '+row[1]+'   '+row[2]+'  '+row[3])
        
  
    
flog=Frame(win,width=2000,height=2500,bg='gray87',border='100')


label0= Label(flog, text="BANKING MANAGEMENT SYSTEM", bg="black", fg="white", font=("mangal", 40, "bold")).grid(row=0, column=2, columnspan=4)
label1= Label(flog, text='Admin Login', font=('arial', 20, 'bold'), bg='steelblue').grid(row=3, column=3)
label2= Label(flog,text="Username",font=('arial',20,'bold'),height=2,bg='gray87').grid(row=7, column=2)
label3= Label(flog,text="Password",font=('arial',20,'bold'),height=2,bg='gray87').grid(row=8, column=2)

e1=Entry(flog,textvariable=username,bd=5,font=('arial',25,'bold'),border='3',bg="cadetblue1",fg='black').grid(row=7, column=3)
e2=Entry(flog,textvariable=password,bd=5,font=('arial',25,'bold'),border='3',bg="cadetblue1",fg='black',show='*').grid(row=8, column=3)
  
b1=Button(flog,text="Login",font=('arial',22,'bold'),padx=35,pady=2,bd=20,bg="navyblue",fg='white',border='4',width='10',command=login).grid(row=11,column=2)
b2=Button(flog,text="Sign Up",font=('arial',22,'bold'),padx=35,pady=2,bd=20,bg="navyblue",fg='white',border='4',width='10',command=signup).grid(row=11, column=3)
b3=Button(flog,text="Reset",font=('arial',22,'bold'),padx=35,pady=2,bd=20,bg="navyblue",fg='white',border='4',width='10',command=clears).grid(row=11,column=4)


fmain= Frame(win,width=1800,height=2000,bg='gray87',border='50')

label4=Label(fmain, text='WELCOME TO BANKING MANAGEMENT SYSTEM', bg='black', fg='white', font=('arial', 40, 'bold')).grid(row=0, column=2, columnspan=4)

btmain1=Button(fmain,text="Account Management",font=('arial',20,'bold'),padx=7,pady=2,bd=7,bg="gray20",fg='white',command=account).grid(row=7, column=2, columnspan=5)
btmain2=Button(fmain,text="Employee",font=('arial',20,'bold'),padx=84,pady=2,bd=7,bg="gray",fg='white',command=employee).grid(row=9, column=2, columnspan=5)
btmain3=Button(fmain,text="Complaint",font=('arial',20,'bold'),padx=82,pady=2,bd=7,bg="gray20",fg='white',command=complaint).grid(row=11, column=2, columnspan=5)
btmain4=Button(fmain,text="Suggestion",font=('arial',20,'bold'),padx=75,pady=2,bd=7,bg="gray",fg='white',command=suggestion).grid(row=13, column=2, columnspan=5)
btmain5=Button(fmain,text="Exit",font=('arial',20,'bold'),padx=124,pady=2,bd=7,bg="gray20",fg='white',command=exit).grid(row=15, column=2, columnspan=5)



facmt= Frame(win,width=1800,height=2000,bg='gray87',border='50')

label4=Label(facmt,text=" ACCOUNT MANAGEMENT ",bg='black',fg='white',width='30',font=('arial',40,'bold')).grid(row=0, column=2,columnspan=4)

btmain1=Button(facmt,text="Create Account",font=('arial',20,'bold'),width='15',padx=100,pady=2,bd=7,bg="gray20",fg='white',command=createaccount).grid(row=6, column=2, columnspan=4)
btmain2=Button(facmt,text="Withdraw Money",font=('arial',20,'bold'),width='15',padx=100,pady=2,bd=7,bg="gray",fg='white',command=withdraw).grid(row=8, column=2, columnspan=4)
btmain3=Button(facmt,text="Deposite Money",font=('arial',20,'bold'),width='15',padx=100,pady=2,bd=7,bg="gray20",fg='white', command=deposite).grid(row=10, column=2, columnspan=4)
btmain4=Button(facmt,text="All Accounts",font=('arial',20,'bold'),width='15',padx=100,pady=2,bd=7,bg="gray",fg='white', command=allaccount).grid(row=12, column=2, columnspan=4)
btmain5=Button(facmt,text="Previous",font=('arial',20,'bold'),width='15',padx=100,pady=2,bd=7,bg="gray20",fg='white',command=previous).grid(row=14, column=2, columnspan=4)


facc= Frame(win,width=1800,height=2000,bg='gray87',border='50')

label0=Label(facc,text="  CUSTOMER ACCOUNT  ",bg='black',fg='white',font=('arial',40,'bold'),width='35').grid(row=4,column=2,columnspan=5)

label1=Label(facc,text="Account No. ",font=('arial',20,'bold'),bg='gray87').grid(row=6,column=2)
eacc1=Entry(facc,textvariable=acno, justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=6, column=4)

label2=Label(facc,text="User Name ",bg='gray87',font=('arial',20,'bold')).grid(row=7,column=2)
eacc1=Entry(facc,textvariable=empname, justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=7, column=4)

label3=Label(facc,text="Father's Name ",bg='gray87',font=('arial',20,'bold')).grid(row=8,column=2)
eacc1=Entry(facc,textvariable=empfather, justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=8, column=4)

label4=Label(facc,text="Account Type ",bg='gray87',font=('arial',20,'bold')).grid(row=9,column=2)
eacc1=Entry(facc,textvariable=acctype,justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=9, column=4)

label5=Label(facc,text="Email Id ",bg='gray87',font=('arial',20,'bold')).grid(row=10,column=2)
eacc1=Entry(facc,textvariable=empmail,justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=10, column=4)

label6=Label(facc,text="Address ",bg='gray87',font=('arial',20,'bold')).grid(row=11,column=2)
eacc1=Entry(facc,textvariable=empaddress,justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=11, column=4)

label7=Label(facc,text="Contact No. ",bg='gray87',font=('arial',20,'bold')).grid(row=12,column=2)
eacc1=Entry(facc,textvariable=contact,justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=12, column=4)

label8=Label(facc,text="Gender ",bg='gray87',font=('arial',20,'bold')).grid(row=13,column=2)
radiobutton=Radiobutton(facc,text="Male",variable=t8,bg='gray87', font=('arial',20,'bold'),value=1).grid(row=13,column=4,sticky='w')
radiobutton=Radiobutton(facc,text="Female",variable=t8,bg='gray87', font=('arial',20,'bold'),value=0).grid(row=13,column=5,sticky='w')

label9=Label(facc,text="Alternative Contact No. ",bg='gray87',font=('arial',20,'bold')).grid(row=14,column=2)
eacc1=Entry(facc,textvariable=altcontact, justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=14, column=4)

label10=Label(facc,text="Date ",bg='gray87',font=('arial',20,'bold')).grid(row=15,column=2)
eacc1=Entry(facc, textvariable=date, justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=15, column=4)

label11=Label(facc,text="Initial Amount ",bg='gray87',font=('arial',20,'bold')).grid(row=16,column=2)
eacc1=Entry(facc, textvariable=initialamt, justify="right",bg="cadetblue1",fg='black',bd=3,font=('arial',20,'bold')).grid(row=16, column=4)

bfacc1=Button(facc,text="Save",font=('arial',20,'bold'),padx=84,pady=2,bd=4,bg="grey",command=save).grid(row=18, column=2)
bfacc2=Button(facc,text="Update",font=('arial',20,'bold'),padx=69,pady=2,bd=4,bg="grey20",command=update).grid(row=19, column=2)
bfacc3=Button(facc,text="Delete",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey20",command=delete).grid(row=18, column=3)
bfacc4=Button(facc,text="Search",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey",command=search).grid(row=19, column=3)
bfacc5=Button(facc,text="See All Accounts",font=('arial',20,'bold'),padx=3,pady=2,bd=4,bg="grey", command=seeall).grid(row=18, column=4)
bfacc6=Button(facc,text="Previous Page",font=('arial',20,'bold'),padx=20,pady=2,bd=4,bg="grey20",command=previous1).grid(row=19, column=4)


fwithdraw = Frame(win,width=1800,height=2000,bg='gray87',border='80')

label0= Label(fwithdraw, text="WITHDRAW MONEY", bg='black', fg='white', font=('arial', 40, 'bold'),width='35').grid(row=3, column=2, columnspan=5, sticky='e')

label1= Label(fwithdraw, text="Account No. ",bg='gray87', font=('arial', 20, 'bold'), justify='left').grid(row=6, column=2)
e1=Entry(fwithdraw,textvariable=acno,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

label2=Label(fwithdraw,text="Username ",bg='gray87',justify='left',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(fwithdraw,textvariable=username,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

labe3=Label(fwithdraw,text="Address ",bg='gray87',font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(fwithdraw,textvariable=address,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

label4=Label(fwithdraw,text="Current Amount ",bg='gray87',font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(fwithdraw,textvariable=crbalance,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

label5=Label(fwithdraw,text="Withdraw Money ",bg='gray87',font=('arial',20,'bold')).grid(row=10,column=2)
e5=Entry(fwithdraw,textvariable=withdrawmoney,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=10,column=3)

label6=Label(fwithdraw,text="Balance ",bg='gray87',font=('arial',20,'bold')).grid(row=11,column=2)
e6=Entry(fwithdraw,textvariable=balance,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=11,column=3)

label7=Label(fwithdraw,text="Date ",bg='gray87',font=('arial',20,'bold')).grid(row=12,column=2)
e7=Entry(fwithdraw,textvariable=date,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=12,column=3)


bc1=Button(fwithdraw,text="Save",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey20",width='10',command=savewithdraw).grid(row=19, column=2)
bc2=Button(fwithdraw,text="Reset",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey",width='10', command=withdrawclear).grid(row=19, column=3)
bc3=Button(fwithdraw,text="Exit",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey20",width='10',command=exit).grid(row=19, column=4)



fdeposite = Frame(win,width=1800,height=2000,bg='gray87',border='80')

label0=Label(fdeposite,text="DEPOSITE MONEY",bg='black',fg='white',font=('arial',40,'bold'),width='35').grid(row=1,column=2,columnspan=3,sticky='e')

l1=Label(fdeposite,text="Account No. ",bg='gray87',font=('arial',20,'bold'),justify='left').grid(row=3,column=2)
e1=Entry(fdeposite,textvariable=acno,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=3,column=3)

l2=Label(fdeposite,text="Username ",bg='gray87',justify='left',font=('arial',20,'bold')).grid(row=4,column=2)
e2=Entry(fdeposite,textvariable=username,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=4,column=3)

l3=Label(fdeposite,text="Address ",bg='gray87',font=('arial',20,'bold')).grid(row=5,column=2)
e3=Entry(fdeposite,textvariable=address,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=5,column=3)

l4=Label(fdeposite,text="Current Amount ",bg='gray87',font=('arial',20,'bold')).grid(row=6,column=2)
e4=Entry(fdeposite,textvariable=crbalance,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l5=Label(fdeposite,text="Deposite Money ",bg='gray87',font=('arial',20,'bold')).grid(row=7,column=2)
e5=Entry(fdeposite,textvariable=depositemoney,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l6=Label(fdeposite,text="Balance ",bg='gray87',font=('arial',20,'bold')).grid(row=8,column=2)
e6=Entry(fdeposite,textvariable=balance,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l7=Label(fdeposite,text="Date ",bg='gray87',font=('arial',20,'bold')).grid(row=9,column=2)
e7=Entry(fdeposite,textvariable=date,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

bc1=Button(fdeposite,text="Deposite",font=('arial',20,'bold'),padx=65,pady=2,bd=4,bg="grey",width='12', command=savedeposite).grid(row=14, column=2)
bc2=Button(fdeposite,text="Reset",font=('arial',20,'bold'),padx=65,pady=2,bd=4,bg="grey20",width='12', command=depositeclear).grid(row=14, column=3)
bc3=Button(fdeposite,text="Exit",font=('arial',20,'bold'),padx=65,pady=2,bd=4,bg="grey",width='12',command=exit).grid(row=14, column=4)

                                                                        

femp=Frame(win,width=1800,height=2000,bg='gray87',border='50')
                                                                                                          
label0=Label(femp,text="EMPLOYEE DETAILS",bg='black',fg='white',font=('arial',40,'bold'),width='35').grid(row=4,column=2,columnspan=5,sticky='e')

l1=Label(femp,text="Employee Id ",bg='gray87',font=('arial',20,'bold'),justify='left').grid(row=6,column=2)
e1=Entry(femp,textvariable=empid,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l2=Label(femp,text="Employee Name ",bg='gray87',justify='left',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(femp,textvariable=empname,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l3=Label(femp,text="Father's Name ",bg='gray87',font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(femp,textvariable=empfather,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l4=Label(femp,text="Employee Address ",bg='gray87',font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(femp,textvariable=empaddress,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

l5=Label(femp,text="Email Id ",bg='gray87',font=('arial',20,'bold')).grid(row=10,column=2)
e5=Entry(femp,textvariable=empmail,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=10,column=3)

l6=Label(femp,text="Designation ",bg='gray87',font=('arial',20,'bold')).grid(row=11,column=2)
e6=Entry(femp,textvariable=empdesg,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=11,column=3)

l7=Label(femp,text="Salary ",bg='gray87',font=('arial',20,'bold')).grid(row=12,column=2)
e7=Entry(femp,textvariable=empsalary, justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=12,column=3)

l8=Label(femp,text="Gender ",bg='gray87',font=('arial',20,'bold')).grid(row=13,column=2)
radiobutton=Radiobutton(femp,text="Male",bg='gray87',variable=t8,font=('arial',20,'bold'),value=1).grid(row=13,column=3,sticky='w')
radiobutton=Radiobutton(femp,text="Female",bg='gray87',variable=t8,font=('arial',20,'bold'),value=0).grid(row=13,column=3,sticky='e')

bfacc1=Button(femp,text="Save",font=('arial',20,'bold'),padx=25,pady=2,bd=4,bg="grey",width='12',command=saveemployee).grid(row=15, column=2)
bfacc2=Button(femp,text="Update",font=('arial',20,'bold'),padx=25,pady=2,bd=4,bg="grey20",width='12',command=updateemployee).grid(row=17, column=2)
bfacc3=Button(femp,text="Delete",font=('arial',20,'bold'),padx=25,pady=2,bd=4,bg="grey20",width='12',command=deleteemployee).grid(row=15, column=3)
bfacc4=Button(femp,text="Search",font=('arial',20,'bold'),padx=25,pady=2,bd=4,bg="grey",width='12',command=searchemployee).grid(row=17, column=3)
bfacc5=Button(femp,text="All Employees ",font=('arial',20,'bold'),padx=25,pady=2,bd=4,bg="grey",width='12', command= allemployee).grid(row=15, column=4)
bfacc6=Button(femp,text="Previous Page",font=('arial',20,'bold'),padx=25,pady=2,bd=4,bg="grey20",width='12',command=previous2).grid(row=17, column=4)



fcomp=Frame(win,width=1800,height=2000,bg='gray87',border='80')

label1=Label(fcomp, text="COMPLAINT BOX", bg='black', fg='white', font=('arial', 40, 'bold'),width='35').grid(row=6, column=3, columnspan=3)

btmain1=Button(fcomp,text="Add Complaint",font=('arial',20,'bold'),padx=40,pady=2,bd=7,bg="grey",command=addcomplaint).grid(row=8, column=3,columnspan=5)
btmain2=Button(fcomp,text="See All Complaints",font=('arial',20,'bold'),padx=13,pady=2,bd=7,bg="grey20", command=showcomplaints).grid(row=10, column=3,columnspan=5)
btmain2=Button(fcomp,text="Previous Page",font=('arial',20,'bold'),padx=44,pady=2,bd=7,bg="grey",command=previous3).grid(row=12, column=3,columnspan=5)



fadcomp=Frame(win,width=1800,height=2000,bg='gray87',border='80')

label0=Label(fadcomp,text=" ADD COMPLAINT",bg='black',fg='white',font=('arial',40,'bold'),width='35').grid(row=3,column=2,columnspan=5)

l1=Label(fadcomp,text="Username :",font=('arial',20,'bold'),bg='gray87',justify='left').grid(row=6,column=2)
e1=Entry(fadcomp,textvariable=cusername,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l2=Label(fadcomp,text="Email Id :",justify='left',bg='gray87',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(fadcomp,textvariable=cmail,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l3=Label(fadcomp,text="Contact No :",font=('arial',20,'bold'),bg='gray87').grid(row=8,column=2)
e3=Entry(fadcomp,textvariable=ccontact,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l4=Label(fadcomp,text="Complaint :",font=('arial',20,'bold'),bg='gray87').grid(row=9,column=2)
e4=Entry(fadcomp,textvariable=ccomplaint,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

bc1=Button(fadcomp,text="Save",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=savecomplaint).grid(row=19, column=2)
bc2=Button(fadcomp,text="Reset",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey20",command=complaintclear).grid(row=21, column=2)
bc3=Button(fadcomp,text="All Complaints",font=('arial',20,'bold'),padx=3,pady=2,bd=4,bg="grey",command=showcomplaints).grid(row=19, column=3)
bc4=Button(fadcomp,text="Exit",font=('arial',20,'bold'),padx=75,pady=2,bd=4,bg="grey20",command=exit).grid(row=21, column=3)



fsugg=Frame(win,width=1800,height=2000,bg='gray87',border='50')

label0=Label(fsugg,text="SUGGESTION BOX",bg='black',fg='white',font=('arial',40,'bold'),width='35').grid(row=3,column=2,columnspan=5,sticky='e')

l1=Label(fsugg,text="Username :",font=('arial',20,'bold'),bg='gray87',justify='left').grid(row=6,column=2)
e1=Entry(fsugg,textvariable=cusername,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l2=Label(fsugg,text="Email Id :",justify='left',bg='gray87',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(fsugg,textvariable=cmail,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l3=Label(fsugg,text="Contact No :",bg='gray87',font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(fsugg,textvariable=ccontact,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l4=Label(fsugg,text="Suggestions :",bg='gray87',font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(fsugg,textvariable=csuggestion,justify="right",bg="cadetblue1",fg='black',bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

bc1=Button(fsugg,text="Save",font=('arial',20,'bold'),padx=74,pady=2,bd=7,bg="grey",command=savesuggestion).grid(row=18, column=2,columnspan=3)
bc2=Button(fsugg,text="Reset",font=('arial',20,'bold'),padx=65,pady=2,bd=7,bg="grey",command=suggestionclear).grid(row=18, column=3,columnspan=3)
bc3=Button(fsugg,text="All Suggestions",font=('arial',20,'bold'),padx=2,pady=2,bd=7,bg="grey20",command=showsuggestion).grid(row=20, column=2,columnspan=3)
bc4=Button(fsugg,text="Exit",font=('arial',20,'bold'),padx=75,pady=2,bd=7,bg="grey20",command=exit).grid(row=20, column=3,columnspan=3)



fthank=Frame(win,width=1800,height=2000,bg='gray87',border='100')
l=Label(fthank, text="THANKS FOR USING",bg='gray87', font=("Playfair Display", 30, 'bold')).grid(row=5, column=4)
l1=Label(fthank, text="BANKING MANAGEMENT SYSTEM SOFTWARE",bg='gray87', font=('Playfair Display', 30, 'bold'), height=1).grid(row=7, column=4)
                                                                                                      

flog.grid(row=0, padx=200,pady=200)
win.mainloop()
