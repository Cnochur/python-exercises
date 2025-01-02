import time
import csv 
def save_to_file (todos, filename="todos.txt"):
	with open(filename, "w") as file:
		for task in todos:
			file.write(task + "\n")


def load_from_file (filename="todos.txt"):

	todos = []
	try:
		with open(filename, "r") as file:
			for task in file.readlines():
				todos.append(task.strip())
	except FileNotFoundError:
		print("\nStarting Fresh....")
		time.sleep(0.3)

	return todos

def menu_option(todos):

	while True:
		try:
			choice = int(input("\n1)View ToDos\n2)Add ToDo\n3)Delete ToDo\n4)Exit\n\nEnter: "))

			if choice == 1:
				time.sleep(0.3)
				view_todos(todos)
				break
			elif choice == 2:
				time.sleep(0.3)
				add_task(todos)
				break
			elif choice == 3:
				time.sleep(0.3)
				delete_task(todos)
				break
			elif choice == 4:
				save_to_file(todos)
				print("...Goodbye!")
				time.sleep(0.5)
				quit()
		except ValueError:
			
			print("Please choose a valid number between: 1,2, 3 and 4.")

def view_todos(todos):

	if not todos:
		print("\nNothing here....")
	else:
		print("\n------ Current Tasks ------\n")
		for index, task in enumerate(todos, start=1):
			print(f"{index}) {task}")
		print("\n---------------------------")

def add_task(todos):

	curr_time = time.strftime("%a, %d %b %Y %H:%M:%S")
	new_entry = input("New Entry: ")
	todos.append(new_entry + f"	({curr_time})")
	save_to_file(todos)
	print(f"\nAdded: {new_entry} @ {curr_time}")
	return todos

def delete_task(todos):

	if not todos:
		print("No tasks to delete...")
		return
	else:
		view_todos(todos)
	try:
		choice = int(input(f"Which task would you like to delete? \nBetween 1 - {len(todos)}: "))

		for index, task in enumerate(todos, start=1):
			if choice == index:
				todos.pop(index - 1)
				save_to_file(todos)
				print("\n...task deleted successfully!")
	except ValueError:
		print("Invalid input, please provide a number.")


def main():

	print("\n_=_= ToDo List =_=_")
	todos = load_from_file()

	while True:
		time.sleep(0.3)
		print("\nPlease choose an option:")
		menu_option(todos)


if __name__ == '__main__':
	main()