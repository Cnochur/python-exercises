class Player:
	def __init__(self, name):
		self.name = name



	def get_name(self, name):
		try:
			name = innput("Enter Name: ")
		except Exception as e:
			print(f"Unexpected input: {e=}, {type(e)=}")
		return name
