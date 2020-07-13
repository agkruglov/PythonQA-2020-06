import json
from collections import OrderedDict
from csv import DictReader

with open('./data/users.json', 'r') as users_file:
    users = json.load(users_file)
with open('./data/books.csv', 'r') as books_file:
    books = [book for book in DictReader(books_file)]
users_with_books = []
books_len = len(books)
for user_id, user in enumerate(users):
    user_with_books = OrderedDict([('name', user['name']),
                                   ('gender', user['gender']),
                                   ('address', user['address']),
                                   ('books', [])])
    if user_id < books_len:
        user_with_books['books'].append(OrderedDict([('title', books[user_id]['Title']),
                                                     ('author', books[user_id]['Author']),
                                                     ('height', books[user_id]['Height'])]))
    users_with_books.append(user_with_books)
with open('./data/users_with_books.json', 'w') as result_file:
    json.dump(users_with_books, result_file, indent=2)
