
def get_num ():
	try:
		num = int(input("Please enter a number: "))
	except ValueError:
		print("Error!! Please enter a valid number!")
		main()

	return num

def get_operator ():
	
	operator = input("Please choose an operatorator: \n+ - / or *: ")
	
	while operator not in ["+","-","/","*"]:
		print("Error!! Choose a valid operatorator.")
		main()

	return operator

def get_total (num1, num2, operator):
	if operator == "+":
		total = num1 + num2
	elif operator == "-":
		total = num1 - num2
	elif operator == "/":
		if num2 == 0:
			print("\n!! Can not divide by 0 !!")
			main()
		else:
			total = num1 / num2
	elif operator == "*":
		total = num1 * num2
	
	return total

def main():
	while True:
		print("\n_=_= Calculator =_=_\n\n")

		num1 = get_num()
		operator = get_operator()
		num2 = get_num()
		total = get_total(num1, num2, operator)

		print(f"Total = {total}")


if __name__ == '__main__':
	main()