import json
from csv import DictReader


def work_with_test_data():
    with open("../users.json", "r") as f:
        users = json.loads(f.read())
        user_mas = []
        for i in range(len(users)):
            user = {
                "name": users[i].get("name"),
                "gender": users[i].get("gender"),
                "address": users[i].get("address"),
                "age": users[i].get("age"),
                "books": [],
            }
            user_mas.append(user)

    with open("../books.csv", newline="") as f:
        reader = DictReader(f)
        book_mas = []
        for row in reader:
            book_mas.append(row)
        books = []
        for i in range(len(book_mas)):
            book = {
                "title": book_mas[i].get("Title"),
                "author": book_mas[i].get("Author"),
                "pages": int(book_mas[i].get("Pages")),
                "genre": book_mas[i].get("Genre"),
            }
            books.append(book)

    i, j = 0, 0
    while i < len(books):
        if j < len(user_mas):
            user_mas[j]["books"].append(books[i])
            j += 1
        else:
            j = 0
        i += 1

    with open("result.json", "w") as result_out:
        result_out.write(json.dumps(user_mas, indent=4))


work_with_test_data()
