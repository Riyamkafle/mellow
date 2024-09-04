user_information = {
    "name": "Aashish Dahal",
    "age": 23,
    "city": "Kathmandu",
    "country": "Nepal",
}

information_list = ["Manik Shretha", 24, "Biratnagar", "Nepal"]
information_list.append(user_information)
print(information_list)


user_information["name"] = "Riyam Kafle"
print(user_information)


for item in user_information:
    print(user_information[item])