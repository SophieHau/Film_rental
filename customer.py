import sqlite3

SAKILA_DB_PATH = 'data/sakila.db'

class Customer():
	def __init__(self, customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update):
		self.customer_id = customer_id
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.store_id = store_id
		self.address_id = address_id
		self.active = 1
		self.create_date = create_date
		self.last_update = last_update

		self.connection = sqlite3.connect(SAKILA_DB_PATH)
		self.cursor = self.connection.cursor()

	def save(self):
		query = '''
				INSERT INTO customer (customer_id, store_id, first_name, last_name, email, address_id, create_date, last_update)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
				'''
		self.cursor.execute(query, (self.customer_id, self.store_id, self.first_name, self.last_name, self.email, self.address_id, self.create_date, self.last_update))
		self.connection.commit()

	def search_by_email(self, email):
		query = '''
				SELECT * FROM customer
				WHERE lower(email) = lower(?)
				'''
		self.cursor.execute(query, (self.email))
		customer = self.cursor.fetchone()
		if customer is not None:
			(c1, c2, c3, c4, c5, c6, c7, c8, c9) = customer
			c = Customer(c1, c2, c3, c4, c5, c6, c7, c8, c9)
			return c
		else: 
			return None

	def get_all(self):
		query = '''
				SELECT * FROM customer
				'''
		self.cursor.execute(query)
		customers = self.cursor.fethall()
		customers_list = []
		for customer in customers:
			(c1, c2, c3, c4, c5, c6, c7, c8, c9) = customer
			c = Customer(c1, c2, c3, c4, c5, c6, c7, c8, c9)
			customers_list.append(c)
		return customers_list


new_customer = Customer(1000, 1, "John", "Smith", "john@smith.com", 2, 1, "2019-03-17", "2019-03-17")



