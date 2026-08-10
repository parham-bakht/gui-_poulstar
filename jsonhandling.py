import json
# read
# file = open("new.json","r")
# with open("new.json","r") as file:
#     data = json.load(file)
#     print(data["full_name"])
#     print(data["card_number"])

#write
# with open("new.json","w") as file:
#     user = {
#         "full_name":"parham bakhtiari",
#         "card_number":"20230203232",
#         "password":"123456"
#     }
#     json.dump(user,file,indent=4)

# add
def add_new_user(json_file,new_user):
    with open(json_file,"r") as file:
        data = json.load(file)
        data.append(new_user)
    with open(json_file,"w") as file:
        json.dump(data,file,indent=4)
