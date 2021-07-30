
from random import choice
rounds = 3
print('Lets play Rock Paper Scissors')
print(f'GAME TO {rounds}')

user_score = 0
comp_score = 0


def play_game():
	global user_score
	global comp_score

	#computer move
	rand_num = choice(range(0,3))
	moves = ['ROCK','PAPER','SCISSORS'] 
	computer_play = moves[rand_num]
	
	user_play = input('What is your move: Rock, Paper, or Scissors?  ').upper()

	if user_play == 'ROCK':
		if computer_play == 'PAPER':
			print(f'Computer Wins by {computer_play}')
			comp_score += 1
		elif computer_play == 'SCISSORS':
			print(f'Player Wins by {user_play}')
			user_score += 1
		else:
			print('Tie')
	if user_play == 'PAPER':
		if computer_play == 'SCISSORS':
			print(f'Computer Wins by {computer_play}')
			comp_score += 1
		elif computer_play == 'ROCK':
			print(f'Player Wins by {user_play}')
			user_score += 1
		else:
			print('Tie')
	if user_play == 'SCISSORS':
		if computer_play == 'ROCK':
			print(f'Computer Wins by {computer_play}')
			comp_score += 1
		elif computer_play == 'PAPER':
			print(f'Player Wins by {user_play}')
			user_score += 1
		else:
			print('Tie')
	print(f'\nComputer Move: {computer_play} Player Move: {user_play}')
	print(f'Player Score: {user_score}  Computer Score: {comp_score}')


while user_score < rounds and comp_score < rounds:
	play_game()




