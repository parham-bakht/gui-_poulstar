import requests
from customtkinter import *
app = CTk()
app.geometry("400x400")
app.title("قیمت لحظه ای ارز و طلا")
currency_api = "https://api.one-api.ir/currency/v1/navasan/currency"
gold_api = "https://api.one-api.ir/currency/v1/navasan/gold"
token = "993228:688a82b1bd11a"
def get_prices():
    header = {
        "one-api-token":token
    }
    response = requests.get(url=gold_api ,headers=header)
    response2 = requests.get(url=currency_api,headers=header)
    currency_data = response2.json()
    gold_data = response.json()
    sekkeh = gold_data["result"]["sekkeh"]["value"]
    print(sekkeh)
    bahar = gold_data["result"]["bahar"]["value"]
    print(bahar)
    nim = gold_data["result"]["nim"]["value"]
    print(nim)
    rob = gold_data["result"]["rob"]["value"]
    print(rob)
    ayar18 = gold_data["result"]["18ayar"]["value"]
    print(ayar18)
    usd = currency_data["result"]["usd"]["value"]
    print(usd)
    eur = currency_data["result"]["eur"]["value"]
    print(eur)
    aed = currency_data["result"]["aed"]["value"]
    print(aed)
    turkish = currency_data["result"]["try"]["value"]
    print(turkish)
    user_choice  = combo.get()
    if user_choice == "دلار آمریکا":
        result.configure(text=f"{usd} تومان")

assets = ["دلار آمریکا",
          "یورو",
          "لیر ترکیه",
          "درهم امارات",
          "طلا 18 عیار",
          "سکه امامی",
          "سکه بهار آزادی",
          "نیم سکه",
          "ربع سکه"]
CTkLabel(app,text="دارایی مورد نظر خود را انتخاب کنید",font=("arial",20)).pack(pady=10)
combo = CTkComboBox(app,values=assets,font=("arial",20),width=200)
combo.pack(pady=10)
result = CTkLabel(app,text="",font=("arial",20,"bold"))
result.pack(pady=20)
app.mainloop()
