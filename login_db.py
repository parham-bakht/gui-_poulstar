from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client["my_accounts_new"]
coll = db["users"]
def register():
    username = username_entry.get()
    password = password_entry.get()
    new_user = {"username":username,"password":password}
    if len(username) < 3 or len(password) < 4:
        messagebox.showerror("error","invalid inputs")

    data = coll.find_one({"username":username})
    if data:
        messagebox.showerror("error","This Username is Taken")
    else:
        coll.insert_one(new_user)
        messagebox.showinfo("ok","Your Account is Ready")
    
def login():
    ...
root = Tk()
root.title("Login Form")
Label(root,text="Username: ",font=("arial",15)).grid(row=0,column=0,padx=10,pady=10)
username_entry = Entry(root,font=("arial",15))
username_entry.grid(row=0,column=1,padx=10,pady=10)
Label(root,text="Password: ",font=("arial",15)).grid(row=1,column=0,padx=10,pady=10)
password_entry = Entry(root,font=("arial",15))
password_entry.grid(row=1,column=1,padx=10,pady=10)
Button(root,text="Login",font=("arial",15),bg="light green").grid(row=2,column=0,padx=10,pady=10)
Button(root,text="Register",font=("arial",15),bg="blue",command=register).grid(row=2,column=1,padx=10,pady=10)

root.mainloop()



