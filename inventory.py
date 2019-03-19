import sqlite3

SAKILA_DB_PATH = 'data/sakila.db'

class Inventory():
	def __init__(self, inventory_id, film_id, store_id, last_uodate):
		self.inventory_id = inventory_id
		self.film_id = film_id
		self.store_id = store_id
		self.last_uodate = last_uodate

		self.connection = sqlite3.connect(SAKILA_DB_PATH)
		self.cursor = self.connection.cursor()

	def search_by_text(self, store_id, text):
		text = '%{}%'.format(text)
		query = '''
				SELECT inventory.inventory_id, inventory.film_id, film.title, film.rating, film.rental_rate from inventory
				JOIN film
				ON inventory.film_id = film.film_id
				WHERE store_id = ? 
				AND (film.title LIKE ?
				OR film.description LIKE ?)
				'''
		self.cursor.execute(query, (store_id, text, text))
		movies = self.cursor.fetchall()
		return movies


