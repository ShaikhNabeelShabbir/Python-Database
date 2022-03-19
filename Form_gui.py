import tkinter
import random
import mysql.connector
import os
from tkinter import ttk
from tkinter import *

os.system("cls")
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="0305"
)
cursor = mydb.cursor()
cursor.execute("USE login")


def submitact():
    x = ID1.get()
    y = NAME1.get()
    z = phone1.get()
    a = email1.get()
    sql = "INSERT INTO logininfo (id,name, phone,email) VALUES (%s,%s,%s,%s)"
    val = (x, y, z, a)
    cursor.execute(sql, val)
    mydb.commit()
    ID1.delete(0, END)
    NAME1.delete(0, END)
    phone1.delete(0, END)
    email1.delete(0, END)


def updateact_name():
    x = ID1.get()
    y = NAME1.get()
    sql = "update LOGININFO set name = %s where id = %s"
    val = (y, x)
    cursor.execute(sql, val)
    mydb.commit()
    ID1.delete(0, END)
    NAME1.delete(0, END)
    phone1.delete(0, END)
    email1.delete(0, END)


def updateact_phone():
    x = ID1.get()
    y = phone1.get()
    sql = "update LOGININFO set phone = %s where id = %s"
    val = (y, x)
    cursor.execute(sql, val)
    mydb.commit()
    ID1.delete(0, END)
    NAME1.delete(0, END)
    phone1.delete(0, END)
    email1.delete(0, END)


def updateact_email():
    x = ID1.get()
    y = email1.get()
    sql = "update LOGININFO set email = %s where id = %s"
    val = (y, x)
    cursor.execute(sql, val)
    mydb.commit()
    ID1.delete(0, END)
    NAME1.delete(0, END)
    phone1.delete(0, END)
    email1.delete(0, END)


def deleteact():
    f = []
    y = ID1.get()
    f.append(y)
    sql = "DELETE FROM LOGININFO WHERE id = %s"
    val = (f)
    cursor.execute(sql, val)
    mydb.commit()
    ID1.delete(0, END)
    NAME1.delete(0, END)
    phone1.delete(0, END)
    email1.delete(0, END)


def quitact():
    quit()


def viewact():
    # cursor.execute("SELECT * FROM LOGININFO")
    # records = cursor.fetchall()
    # print(records)
    # for i, (id, stname, course, fee) in enumerate(records, start=1):
    #     listBox.insert("", "end", values=(id, name, phone, email))
    cursor.execute("SELECT * FROM LOGININFO")
    for p in cursor:
        print(p)


    # creating window
window = Tk()
window.title("student information")
window.geometry('400x400')
window.configure(background='white')
# creating visible labels
Id = Label(window, text="id", fg='red',
           font=("Helvetica", 16)).grid(row=0, column=0)
name = Label(window, text=" Name", fg='red',
             font=("Helvetica", 16)).grid(row=2, column=0)
phone = Label(window, text="Number", fg='red', font=(
    "Helvetica", 16)).grid(row=4, column=0)
email = Label(window, text="Email", fg='red', font=(
    "Helvetica", 16)).grid(row=6, column=0)
# creating Entry block
ID1 = Entry(window)
ID1.grid(row=0, column=2)

NAME1 = Entry(window)
NAME1.grid(row=2, column=2)

phone1 = Entry(window)
phone1.grid(row=4, column=2)

email1 = Entry(window)
email1.grid(row=6, column=2)
# creating buttons
Submit_btn = Button(window, text="Submit", fg='blue',
                    command=submitact)
Submit_btn.grid(row=8, column=0)

update_name_btn = Button(window, text="update name",
                         fg='blue', command=updateact_name)
update_name_btn.grid(row=8, column=2)

update_phone_btn = Button(window, text="update phone",
                          fg='blue', command=updateact_phone)
update_phone_btn.grid(row=10, column=2)

update_email_btn = Button(window, text="update email",
                          fg='blue', command=updateact_email)
update_email_btn.grid(row=12, column=2)

delete_btn = Button(window, text="delete", fg='blue', command=deleteact)
delete_btn.grid(row=8, column=4)

delete_btn = Button(window, text="quit", fg='blue', command=quitact)
delete_btn.grid(row=10, column=4)

view_btn = Button(window, text="view", fg='blue', command=viewact)
view_btn.grid(row=10, column=0)

window.mainloop()
