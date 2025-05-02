from BTrees.OOBTree import OOBTree
import csv
import timeit


# Створення OOBTree
tree = OOBTree()


# Створення словника
dict = {}


# Отримання даних з файлу
def get_data(file):
    data = []
    with open(file, newline="", encoding="utf-8") as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),
            }
            data.append(item)
    return data


# Функція для додавання товарів у OOBTree
def add_item_to_tree(item):
    tree[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


# Функція для додавання товарів у dict
def add_item_to_dict(item):
    dict[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


# Функція для виконання діапазонного запиту, де потрібно знайти всі товари у визначеному діапазоні цін. OOBTree
def range_query_tree(min_price=10.0, max_price=100.0):
    result = []
    for key, value in tree.items():
        if min_price <= value["Price"] <= max_price:
            result.append((key, value))
    return result


# Функція для виконання діапазонного запиту, де потрібно знайти всі товари у визначеному діапазоні цін. dict
def range_query_dict(min_price=10.0, max_price=100.0):
    result = []
    for key, value in dict.items():
        if min_price <= value["Price"] <= max_price:
            result.append((key, value))
    return result


def main():

    # Витягуємо дані
    data = get_data("generated_items_data.csv")

    # Додаємо товари до обох структур
    for item in data:
        add_item_to_tree(item)
        add_item_to_dict(item)

    # Вимірювання часу виконання діапазонних запитів
    tree_time = timeit.timeit("range_query_tree()", globals=globals(), number=100)
    dict_time = timeit.timeit("range_query_dict()", globals=globals(), number=100)

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")


if __name__ == "__main__":
    main()
