# import os

# db_path = os.path.abspath("../itids.db")  # Получаем полный путь
# print("Абсолютный путь к БД:", db_path)

# # Проверяем, существует ли файл
# if os.path.exists(db_path):
#     print("Файл найден!")
# else:
#     print("Файл НЕ найден!")

# services_path = os.path.join(os.path.dirname(__file__), 'services')
# sys.path.append(services_path)

# print("sys.path:", sys.path)
# print("Файлы в директории services:", os.listdir(services_path))