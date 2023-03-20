#dictionaries - in a dictionary we can store a bunch of key value pairs
#each key should be unique in dictionay
# customers = {
#     "name":"john smith",
#     "age" : 30,
#     "is varified": True
# }
# print(customers["name"])
# print(customers.get("names")) #instead of getting error we get none and none is the value that represents the absence of value
# print(customers.get("birthday", "jan 1 1980"))  # if the dictionary doesn't have the key we can supply default value
# customers["birthdate"] = "jan 1 1981" # we can add new value
# customers["name"] = " vijay rai" # we can edit the value
# print(customers)

#example - to print phone numbers in words
phone = input("Phone:")
number={
    "0":"zaro",
    '1':"one",
    '2':"two",
    '3':"three",
    '4':"four"
}
output = ""
for i in phone:
    output += number.get(i,"!")+ " "
print(output)