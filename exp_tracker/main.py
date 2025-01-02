import csv, time

def load_expenses(filename="expenses.csv"):

	expenses = []

	try:
		with open(filename, "r") as file:
			reader = csv.reader(file)
			for line in reader:
				expenses.append(line)
	except FileNotFoundError:
		print('\nStarting fresh...')

	return expenses

def save_expenses(expenses, filename="expenses.csv"):
	with open(filename, "w", newline="") as file:
		writer = csv.writer(file)
		expense = ["Description", "Amount", "Date"]
		for expense in expenses:
			writer.writerow(expense)

def menu_options(expenses):
	while True:
		try:
			choice = int(input("\n1)View Expenses\n2)Add Expense\n3)Total Spent\n4)Exit\n\nEnter: "))

			if choice == 1:
				time.sleep(0.3)
				view_expenses(expenses)
				break
			elif choice == 2:
				time.sleep(0.3)
				add_expense(expenses)
				break
			elif choice == 3:
				time.sleep(0.3)
				total_spent(expenses)
				break
			elif choice == 4:
				save_expenses(expenses)
				print("...Goodbye!")
				time.sleep(0.5)
				quit()

		except ValueError:
			print("Please choose a valid number between: 1,2, 3, 4 and 5.")

def add_expense(expenses):

	curr_date = time.strftime("%a,%H:%M:%S")
	category = input("\nCategory: ")
	description = input("\nExpense: ")
	amount = int(input("\nAmount: £"))
	expenses.append([category, description, amount, curr_date])
	print(f"\nExpence Added!\n\nCategory: {category}\nExpense: {description}\nAmount: £{amount}")

def view_expenses(expenses):
	if not expenses:
		print("\nNothing here....")
	else:
		print("\n------ Current Expenses ------\n")
		for index, expense in enumerate(expenses, start=1):
			print(f"{index}) Category: {expense[0]} | Expense: {expense[1]} | Amount: £{expense[2]} | {expense[3]}\n")
		total_spent(expenses)
		print("\n---------------------------")

def total_spent (expenses):

	total = 0

	for expense in expenses:
		amount = float(expense[2])
		total += amount

	print(f"Total spent: £{total:.2f}")

def main():

	print("\n_=_= Expense Tracker =_=_")
	expenses = load_expenses()

	while True:
		time.sleep(0.3)
		print("\nPlease choose an option:")
		menu_options(expenses)

if __name__ == "__main__":
	main()