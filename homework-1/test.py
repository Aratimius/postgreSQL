import csv


# with open('north_data/orders_data.csv', encoding='utf-8') as r_file:
#     # Создаем объект reader, указываем символ-разделитель ","
#     file_reader = csv.reader(r_file, delimiter=",")
#     data = []
#     print(type(file_reader))
#     for row in file_reader:
#         data.append(tuple(row))
# data.pop(0)
# print(data)

users = [
    ("James", 25, "male", "USA"),
    ("Leila", 32, "female", "France"),
    ("Brigitte", 35, "female", "England"),
    ("Mike", 40, "male", "Denmark"),
    ("Elizabeth", 21, "female", "Canada"),
]

user_records = ", ".join(["%s"] * len(users))
print(user_records)

