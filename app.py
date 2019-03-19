from customer import Customer
from inventory import Inventory
from rental import Rental



c = Customer(734657, 2, "first_name", "last_name", "email", 2, 1, "2019-03-19", "2019-03-19")
i = Inventory(10, 438, 1, "2019-03-19")
r = Rental(324, "2019-03-19", 425, 43, "2019-03-19", 3)


while True:
	user_input = input("Enter 's' to search a customer, 'c' to get a list of customers, 'k' to search for a DVD by keyword, 'r' to return a DVD, 'x' to exit  ")
	if user_input == 's':
		email = ((input('Please enter the email of the customer: '),))
		if c.search_by_email(email) is not None:
			customer = c.search_by_email(email)
			print("Customer: First name: {}\n  Last name: {}\n email: {}".format(customer.first_name, customer.last_name, customer.email))
		else:
			print("This customer is not in our database")
	elif user_input == 'c':
		customers = c.get_all()
		for customer in customers:
			print("Customer: \n Customer_id: {} \n Name: {} {} \n Email: {}".format(customer.customer_id, customer.first_name, customer.last_name, customer.email))
	elif user_input == 'k':
		text = input('Text in the title or description: ')
		store_id = input('Enter your store id: ')
		dvds = i.search_by_text(store_id, text)
	elif user_input == 'r':
		rental_id = input("Enter the rental id: ")
		r.return_rental(rental_id)
	elif user_input == 'x':
		exit()














