import random
import pandas as pd
import matplotlib.pyplot as plt

def winner(a,b):
    if(a=='s'):
        if(b=='w'):
            return 1
        elif(b=='s'):
            return 0
        else:
            return 2
    elif(a=='w'):
        if(b=='g'):
            return 1
        elif(b=='w'):
            return 0
        else:
            return 2
    elif(a=='g'):
        if(b=='s'):
            return 1
        elif(b=='g'):
            return 0
        else:
            return 2


user_wins = 0
computer_wins = 0
total_games = 0
results = []

for i in range(10):
    a = input("Enter your choice Gun(g) Water(w) Snake(s) ")

    randno = random.randint(1, 3)

    if randno == 1:
        b = 'g'
    elif randno == 2:
        b = 'w'
    else:
        b = 's'

    print(f"The choice of the player 1 was {a}")
    print(f"The choice of the computer was {b}")

    if a in ('w', 'g', 's'):
        if b in ('w', 'g', 's'):
            result = winner(a, b)
            if result == 1:
                print("Player 1 won the game")
                user_wins += 1
            elif result == 2:
                print("Computer won the game")
                computer_wins += 1
            else:
                print("Draw")

            results.append(result)
            total_games += 1
        else:
            print("Invalid choice entered")
    else:
        print("Invalid choice entered")

# Record results in an Excel file
data = {'Result': results}
df = pd.DataFrame(data)
df.to_excel('game_results.xlsx', index=False)

# Calculate success rates
user_success_rate = user_wins / total_games
computer_success_rate = computer_wins / total_games

# Plot success rates
labels = ['User', 'Computer']
success_rates = [user_success_rate, computer_success_rate]
colors = ['blue', 'red']

plt.bar(labels, success_rates, color=colors)
plt.xlabel('Player')
plt.ylabel('Success Rate')
plt.title('Game Success Rates')
plt.show()