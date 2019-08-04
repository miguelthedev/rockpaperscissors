# ROCK PAPER SCISSORS GAME

print('...rock...')
print('...paper...')
print('...scissors...')

p1_choice = input('Player 1, what\'s your choice? ')
p2_choice = input('Player 2, what\'s your choice? ')

print("SHOWTIME!")

if p1_choice == 'rock' and p2_choice == 'rock':
    print("It's a tie!")
elif p1_choice == 'paper' and p2_choice == 'rock':
    print("Player 1 wins!")
elif p1_choice == 'scissors' and p2_choice == 'rock':
    print("Player 2 wins!")
elif p1_choice == 'rock' and p2_choice == 'paper':
    print("Player 2 wins!")
elif p1_choice == 'paper' and p2_choice == 'paper':
    print("It's a tie!")
elif p1_choice == 'scissors' and p2_choice == 'paper':
    print("Player 1 wins!")
elif p1_choice == 'rock' and p2_choice == 'scissors':
    print("Player 1 wins!")
elif p1_choice == 'paper' and p2_choice == 'scissors':
    print("Player 2 wins!")
elif p1_choice == 'scissors' and p2_choice == 'scissors':
    print("It's a tie!")
else:
    print("Invalid choices")