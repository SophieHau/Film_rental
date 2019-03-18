import sqlite3

SAKILA_DB_PATH = 'data/sakila.db'

class Rental():
	def __init__(self, rental_id, rental_date, inventory_id, customer_id, return_date, staff_id):
		self.rental_id = rental_id
		self.rental_date = rental_date
		self.inventory_id = inventory_id
		self.customer_id = customer_id
		self.return_date = return_date
		self.staff_id = staff_id
		
		self.connection = sqlite3.connect(SAKILA_DB_PATH)
		self.cursor = self.connection.cursor()

	def return_rental(self, rental_id):
		query = "UPDATE rental SET return_date = CURRENT_DATE WHERE rental_id = ?"
		self.cursor.execute(query, (rental_id,))
		self.connection.commit()


new_rental = Rental(16200, "2019-03-18", 746, 34, "2019-03-18", 2)

