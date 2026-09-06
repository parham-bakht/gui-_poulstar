from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient

root = Tk()
root.title("Login Form")

Label(root,text="Username: ",font=("arial",15)).grid(row=0,column=0,padx=10,pady=10)
username_entry = Entry(root,font=("arial",15))
username_entry.grid(row=0,column=1,padx=10,pady=10)

Label(root,text="Password: ",font=("arial",15)).grid(row=1,column=0,padx=10,pady=10)
password_entry = Entry(root,font=("arial",15))
password_entry.grid(row=1,column=1,padx=10,pady=10)

Button(root,text="Login",font=("arial",15),bg="light green").grid(row=2,column=0,padx=10,pady=10)
Button(root,text="Register",font=("arial",15),bg="blue").grid(row=2,column=1,padx=10,pady=10)

root.mainloop()



