import csv
import json

# Функція для створення .csv файла
def create_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "city"])  # Header
        writer.writerow(["John", "23", "New York"])
        writer.writerow(["Anna", "31", "Berlin"])

# Функція для конвертації з .csv у .json
def csv_to_json(csv_filename, json_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Викликаємо функції
create_csv("data.csv")

csv_to_json("data.csv", "data.json")

# Функція для конвертації з .json у .csv і додавання даних

def json_to_csv(json_filename, csv_filename):
    try:
        with open(json_filename, 'r') as json_file:
            data = json.load(json_file)

        with open(csv_filename, 'w', newline='') as csv_file:
            fields = ["name", "age", "city"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
            csv_writer.writeheader()
            for row in data:
                csv_writer.writerow(row)
            # Додавання нових рядків
            csv_writer.writerow({"name": "Sophie", "age": "29", "city": "Paris"})
            csv_writer.writerow({"name": "Mike", "age": "21", "city": "Toronto"})
    except FileNotFoundError:
        print(f"Error: The file {json_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Викликаємо функцію
json_to_csv("data.json", "updated_data.csv")


