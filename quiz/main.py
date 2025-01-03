	#QUIZ LOGIC
		#display question 1 with multiple choice answers
		#choose answer
		#if its correct add point to total
		#display next question
		#if no more questions then end quiz
		#display final score and percentage
		#play again yes/no
		#no - save local db -> exit
		#yes - save local db -> main menu


import sqlite3
from player import Player

#Creating a local data base
connect = sqlite3.connect("scores-database.db")
cursor = connect.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS scores ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT(15),  score INT)
""")
connect.commit()

#Functions

def main_menu(player, score):
    print("\n_=_= Main Menu =_=_")
    print("\n\n1)Start A Quiz\n2)View Top 5 Scores\n3)View All Scores\n4)Exit")

    try:
        choice = int(input("\nEnter: "))
        if choice == 1:
            # quiz_menu
            pass
        elif choice == 2:
            get_top_five()
            pass
        elif choice == 3:
            view_all_scores()
            pass
        elif choice == 4:
            print("...Goodbye!")
            player = player.name
            cursor.execute("INSERT INTO scores (id, name, score) VALUES (NULL, ?, ?)", (player, score))
            connect.commit()
            connect.close()
            exit()
    except ValueError:
        print("Enter a valid number (1, 2, 3 or 4)!!")

def get_top_five():
	cursor.execute("""SELECT * FROM scores ORDER BY score DESC LIMIT 5""")
	rows = cursor.fetchall()
	print("_=_= Top 5 Players =_=_")
	for index, row in enumerate(rows, start=1):
		print(f"--- {index} ---")
		print(f"PlayerID: {row[0]}\nName: {row[1]}\nScore: {row[2]}")
		print("----------")

def view_all_scores():
	cursor.execute("""SELECT * FROM scores ORDER BY name ASC""")
	rows = cursor.fetchall()
	print("_=_= All Players =_=_")
	for row in rows:
		print("--------------------------------------------------")
		print(f"PlayerID: {row[0]} Name: {row[1]} Score: {row[2]}")
		print("--------------------------------------------------")


# main game logic
def main():

	player = ""
	score = 25000

	print("\n_=_= Welcome to T-Quzzil =_=_")
	player = Player(input("\nEnter name: "))
	print(f"\nHello {player.name}, Good Luck!!")

	while True:

		main_menu(player, score)

if __name__ == '__main__':
	main()