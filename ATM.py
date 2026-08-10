from tkinter import *
import random
import json
from tkinter import messagebox
from jsonhandling import add_new_user
app = Tk()
register_page = Toplevel()
profile_page = Toplevel()
profile_page.geometry("400x400")
user_list = []
def change_window(a,b):
    a.withdraw()
    b.deiconify()

def createAccount():
    password = ent_passwordC.get()
    id = ent_id.get()
    full_name = ent_fullname.get()
    balance = ent_balance.get()
    base_card  = "603799"
    for i in range(10):
        base_card = base_card+str(random.randint(0,9))

    new_account = {
        "id":id,
        "full name":full_name,
        "balance":float(balance),
        "password":password,
        "card_number":base_card
    }
    print(new_account)
    add_new_user(json_file="account.json",new_user=new_account)
def login():
    login_id = ent_cardid.get()
    login_password = ent_password.get()
    with open("account.json","r") as file:
        data = json.load(file)
        for i in data:
            if i["card_number"] == login_id and i["password"] == login_password:
                print("login successful✅")
                messagebox.showinfo("sucess","Login Sucessful")
                change_window(app,profile_page)
                return
        else:
            messagebox.showerror("ERROR","Card Number or Password is not correct")
            print("User Not Found❌")

BG_COLOR = "#212121"
ENT_BG = "#3D3C3C"
profile_page["bg"] = BG_COLOR
app["bg"] = BG_COLOR
lbl_cardid = Label(app,text="Card ID",font=("arial",15),bg=BG_COLOR,fg="white")
lbl_cardid.pack(pady=10,padx=10)
ent_cardid = Entry(app,font=("arial",15),bg=ENT_BG,fg="white")
ent_cardid.pack(pady=10,padx=10)

lbl_password = Label(app,text="Password",font=("arial",15),bg=BG_COLOR,fg="white")
lbl_password.pack(pady=10,padx=10)
ent_password = Entry(app,font=("arial",15),bg=ENT_BG,fg="white")
ent_password.pack(pady=10,padx=10)

login_btn  = Button(app,text="Login",font=("arial",15),bg="dark blue",fg="white",command=login)
login_btn.pack(pady=10,padx=10)

register_btn  = Button(app,text="Create Account",font=("arial",15),bg="dark green",fg="white",command=lambda : change_window(app,register_page))
register_btn.pack(pady=10,padx=10)


register_page["bg"] = BG_COLOR
lbl_fullname  = Label(register_page,text="Full Name:",bg=BG_COLOR,fg="white",font=("arial",15))
lbl_fullname.grid(row=0,column=0,padx=10,pady=10)
ent_fullname = Entry(register_page,font=("arial",15),bg=ENT_BG,fg="white")
ent_fullname.grid(row=0,column=1,padx=10,pady=10)

lbl_id  = Label(register_page,text="ID:",bg=BG_COLOR,fg="white",font=("arial",15))
lbl_id.grid(row=1,column=0,padx=10,pady=10)
ent_id = Entry(register_page,font=("arial",15),bg=ENT_BG,fg="white")
ent_id.grid(row=1,column=1,padx=10,pady=10)


lbl_balance = Label(register_page,text="Balance:",bg=BG_COLOR,fg="white",font=("arial",15))
lbl_balance.grid(row=2,column=0,padx=10,pady=10)
ent_balance = Entry(register_page,font=("arial",15),bg=ENT_BG,fg="white")
ent_balance.grid(row=2,column=1,padx=10,pady=10)


lbl_password = Label(register_page,text="password:",bg=BG_COLOR,fg="white",font=("arial",15))
lbl_password.grid(row=3,column=0,padx=10,pady=10)
ent_passwordC = Entry(register_page,font=("arial",15),bg=ENT_BG,fg="white")
ent_passwordC.grid(row=3,column=1,padx=10,pady=10)

create_btn  = Button(register_page,text="Create Account",bg="dark green",fg="white",font=("arial",15),command=createAccount)
create_btn.grid(row=4,column=0,padx=10,pady=10)


signin_btn  = Button(register_page,text="Login",bg="dark blue",fg="white",font=("arial",15),command=lambda: change_window(register_page,app))
signin_btn.grid(row=4,column=1,padx=10,pady=10)
register_page.withdraw()
profile_page.withdraw()
app.mainloop()