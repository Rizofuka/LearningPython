# Lesson_2 10.11.2024 start 02:30 end

# Тренируем операторы: + - = * ==(равно) !=(не равно) / % // < >
# num_1 = 10
# num_2 = 5
# num_3 = num_1 + num_2
# print(num_3)

# Логические операторы 1: and (Логическое "и". True - если оба выражения True)
# num = 10
# Name = "Tom"
# result = num > 5 and Name == "Tom"
# print(result)

# Логические операторы 2: or (Логическое "или". True - если хотя бы одно из выражений True)
# num = 10
# Name = "Tom"
# result = num < 5 or Name == "Jon"
# print(result)

# Логические операторы 3: in (Логическое "в")
# num = 10
# Name = "Tom"
# message = "Tom got some money"
# print(Name in message)

# Логические операторы 4: not in (Инвертирует True на False и наоборот)
# num = 10
# Name = "Tom"
# message = "Tom got some money"
# print(Name not in message)

# Логические операторы 5: Смена имени in
# num = 10
# Name = "Tom"
# message = "Tom got some money"
# print(Name in message)
#
# Name = "John"
# message = "You won!"
# print(Name in message)

# Логические операторы 6: Пробую разненькое 1
# age = 35
# name = "Pipa"
# animal = "Hyrax"
# print(age == 35 and "i" in name and animal != "Capibara")

# Логические операторы 6: Пробую разненькое 2
# age = 35
# name = "Pipa"
# animal = "Hyrax"
# print(age == 35 and "W" in name and animal == "Capibara")

# Логические операторы 6: Пробую разненькое 3
# age = 35
# name = "Pipa"
# animal = "Hyrax"
# print(age == 35 and "P" in name or animal == "Capibara")

# Типы данных 1: int (целое число: 5, 7)
# num_1 = 5
# print(type(num_1)) # Что-то трудно понятное

# Типы данных 2: float (Числа с плавающей точкой: 5.13, 7.10)
# num_1 = 3.14
# print(type(num_1))

# Типы данных 3: string, str (Строчка)
# string = "Hi, Mr.Cat! :3"
# print(string)

# Типы данных 4: boolean, bool (Булевые значения: True/False)
# check = True
# print(type(check))

# Типы данных 5: list (Список [","])
# lst = ["Mr. Capibara", "Mrs. Hyrax", "Dr.Goose", "Lady Lama"]
# print(type(lst))

# Типы данных 6: tuple (Кортеж (,) - похож на список, НО он неизменяем!)
# tpl = (1, 2, 3)
# print(type(tpl))

# Типы данных 7: dictionary, dict (Словарь {":,":} - пары ключ-значение)
# dct = {"Name" : "Mrs. Chicken", "Age" : 2}
# print(type(dct))

# Типы данных 8: set (Коллекция {,} уникальных (не может быть повторок) элементов без порядка)
# set_ex = {1, 2, 3}
# print(type(set_ex))

# Типы данных 9: "None" (Нет данных или значения)
# print(type(None))

# Типы данных 10: class and object (Можно создавать собственные типы данных используя классы)

# Типы данных: Пробую разненькое 1
# lst = ["Potato", "Melon", "Grape"]
# dct = {"Name" : "Potato", "County" : "Poland"}
# tpl = (109, 33)
# result = dct["Name"] in lst # есть ли в словаре имя Картошки?
# print(result)

# Типы данных: Пробую разненькое 2
# lst = ["Potato", "Melon", "Grape"]
# dct = {"Name" : "Potato", "County" : "Poland"}
# tpl = (109, 33)
# print(dct["Name"] == "Potato") #Картошкино ли имя Картошка из словаря?

# Типы данных: Пробую разненькое 3
# Name = "Mr.Humster"
# Age = 0.5
# Fav_books = ["Fall is coming", "Seeds and flowers"]
# Location = ( 33, 42)
# print("Name:", Name)
# print("Age:", Age)
# print("Favorite books:", Fav_books)
# print("Location:", Location)

# Типы данных: Пробую разненькое 4
# Mr_1 = ("Mr.Humster", 0.5, ["Fall is coming", "Seeds and flowers"],("Latitude", 33, "Longitude", 42))
# Mr_2 = ("Mr.Pony", 2, ["The best hay in the stall", "How to choose carrots?"],("Latitude", 79, "Longitude", 55))
# dict_of_misters = {
#     "Mr.Humster" : Mr_1,
#     "Mr.Pony" : Mr_2
# }
# for name, profile in dict_of_misters.items():
#     print(f"Name: {name}")
#     print(f"Age: {profile[1]}")
#     print(f"Favorite books: {profile[2]}")
#     print(f"Location: {profile[3]}")
#     print()
