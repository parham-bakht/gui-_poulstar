import json
from tkinter import *
import random
from tkinter import messagebox
app = Tk()
def change_window(a,b):
    a.withdraw()
    b.deiconify()

account_list = []
def create_account():
    card_base = "62198619"
    for i in range(8):
        card_base+=str(random.randint(0,9))
    print(card_base)
    full_name = fullname_ent.get()
    userid = userid_ent.get()
    password = password_ent.get()
    balance = balance_ent.get()
    new_user = {
        "card_number":card_base,
        "full_name":full_name,
        "id":userid,
        "password":password,
        "balance":balance
    }
    account_list.append(new_user)
    with open("account.json","w") as file:
        json.dump(account_list,file,indent=4)
    messagebox.showinfo(title="success",message="Account Created Succesfuly")
register_page = Toplevel()
register_page.title("Register")
app.title("Login Page")
BG_COLOR = "#ede0d4"
BUTTON_COLOR = "#9c6644"
BUTTON2_COLOR = "#b08968"
register_page["bg"] = BG_COLOR
app["bg"] = BG_COLOR

login_cardid_lbl = Label(app,text="CARD ID",font=("arial",15),bg=BG_COLOR)
login_cardid_lbl.pack(padx=20,pady=10)
login_cardid_ent = Entry(app,font=("arial",15))
login_cardid_ent.pack(padx=20,pady=10)
login_password_lbl = Label(app,text="PASSWORD",font=("arial",15),bg=BG_COLOR)
login_password_lbl.pack(padx=20,pady=10)
login_password_ent = Entry(app,font=("arial",15))
login_password_ent.pack(padx=20,pady=10)
login1_btn = Button(app,text="Login",font=("arial",15),bg=BUTTON_COLOR,fg="white")
login1_btn.pack(padx=20,pady=10)
register1_btn = Button(app,text="Create Account",font=("arial",15),bg=BUTTON2_COLOR,fg="white",command=lambda:change_window(app,register_page))
register1_btn.pack(padx=20,pady=10)
register_page.withdraw()

fullname_lbl = Label(register_page,text="FULL NAME",font=("arial",15),bg=BG_COLOR)
fullname_lbl.grid(row=0,column=0,padx=20,pady=10)
fullname_ent = Entry(register_page,font=("arial",15))
fullname_ent.grid(row=0,column=1,padx=20,pady=10)
userid_lbl  = Label(register_page,text="ID",font=("arial",15),bg=BG_COLOR)
userid_lbl.grid(row=1,column=0,padx=20,pady=10)
userid_ent = Entry(register_page,font=("arial",15))
userid_ent.grid(row=1,column=1,padx=20,pady=10)
balance_lbl = Label(register_page,text="BALANCE",font=("arial",15),bg=BG_COLOR)
balance_lbl.grid(row=2,column=0,padx=20,pady=10)
balance_ent = Entry(register_page,font=("arial",15))
balance_ent.grid(row=2,column=1,padx=20,pady=10)
password_lbl = Label(register_page,text="PASSWORD",font=("arial",15),bg=BG_COLOR)
password_lbl.grid(row=3,column=0,padx=20,pady=10)
password_ent = Entry(register_page,font=("arial",15))
password_ent.grid(row=3,column=1,padx=20,pady=10)
login2_btn = Button(register_page,text="Login",bg=BUTTON_COLOR,font=("arial",15),command=lambda:change_window(register_page,app))
login2_btn.grid(row=4,column=0,padx=20,pady=10)
register2_btn = Button(register_page,text="Register",bg=BUTTON2_COLOR,font=("arial",15),command=create_account)
register2_btn.grid(row=4,column=1,padx=20,pady=10)
app.mainloop()