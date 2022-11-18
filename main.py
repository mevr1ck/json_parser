import csv
import json
import time

from files import BOOKS_FILE, USERS_FILE

result_file = "result.json"

USER_ATTRS = ('name', 'gender', 'address', 'age', 'books')
BOOK_ATTRS = ('title', 'author', 'pages', 'genre')


def benchmark(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		t = end - start
		print('Время выполнения:', t)
		return result
	
	return wrapper


@benchmark
def get_result():
	with open(BOOKS_FILE, 'r') as b:
		books = list(csv.DictReader(b))
		for i in books:
			del i['Publisher']
	
	with open(USERS_FILE, 'r') as u:
		new_users = []
		for i in json.load(u):
			new_users.append(
				{'name': i.get('name'),
				 'gender': i.get('gender'),
				 'address': i.get('address'),
				 'age': i.get('age'),
				 'books': []})
	
	while len(books) > 0:
		for i_user in new_users:
			if len(books) > 0:
				i_user['books'].append(books.pop())
	
	with open('result.json', 'w') as r:
		result = json.dumps(new_users, indent=4)
		r.write(result)


get_result()
