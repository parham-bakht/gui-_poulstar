import json

user_list = []
new_user = {
    "name":"parham",
    "password":"123456"
}
user_list.append(new_user)

# file = open("account.json","w")
with open("account.json","w") as file:
    json.dump(user_list,file,indent=4)