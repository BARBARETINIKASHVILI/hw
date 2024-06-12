# car = ['ford', 'mustang', 1964]

# car = {
#     "brand":'ford',
#     "model": "mustang",
#     "year": 1964
# }

# print(car["bsand"])

# acc = {
#     "fullname": "Barbare Tinikashvili",
#     "brother": "Nika",
#     "born":{
#         "year": 2009,
#         "month": "December",
#         "day": 2
#     }
# }

# print(acc["born"]["year"])

#შექმენით ექაუნთის dict სადაჩ შეინახავთ fullname / email / address / password შემდეგ გამოიყენეთ for ციკლი და გადაუარეთ 
# dictს თვითოეული მნიშვნელობა დიქტიდან გამოიტანეთ როგორც ვისწავლეთ ისე

# acc = {
#     "fullname": "Barbare Tinikashvili",
#     "email": "email2@",
#     "address":{
#         "city": "Mtskxeta"
#     },
#     "password": "0009019"

    
# }

# for i in acc:
#     print(i)


# for i in acc.keys():
#     print(i)

# for key in acc:
#     print(acc[key])
     

# print(acc.values())
# print(acc.keys())
# print(acc.items())

# შექმენით ფუნქცია manual_items გადაეცით dict 
# და დააბრუნეთ სია მხოლოდ key value 
# !გამოიყენეთ For ციკლი!

# def manual_items(dict):
#     item = []
#     for key in dict:
#         item.append((key, dict))
#     return item

# test = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# print(manual_items(test))



# def manual(dict1):
#     items = []

#     for key in dict1:
#         items.append([key, dict1[key]])

#     return items

# acc = {
#     "fullname": "Barbare Tinikashvili",
#     "email": "email2@",
#     "address":{
#         "city": "Mtskxeta"
#     },
#     "password": "0009019"
# }

# print(manual(acc))

# value metodi abrunebs mnishvnelobebs
# item abrunebs keys da values wyvilebad
# key abrunebs kutvnilebebs

# def manual_get(dict, key, default_value = None):
#     if key in dict:
#         return dict[key]
#     return default_value

# number = [10, 20, 25]

# # print(5 in number)

# acc = {
#     "fullname": "Barbare Tinikashvili",
#     "email": "email2@",
#     "address":{
#         "city": "Mtskxeta"
#     },
#     "password": "0009019"
# }

# print(manual_get(acc, "fullname"))

# print("Barbare Tinikashvili" in acc)
# print(acc["fullname"])
# print(acc.get("fullname", "Kay nt found"))

