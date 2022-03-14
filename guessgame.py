import random

colors=['blue','red','yellow','green','violet','white']

while True:
    selected_color = input("I'm thinking of a color. Can you guess it :").lower()
    random_color_index = random.randrange(len(colors))
    random_color = colors[random_color_index]
    while True:
        if selected_color == random_color:
            break
        else:
            selected_color = input("Nope. Guess again :").lower()
    print('You guessed it right! and the color is :',random_color)

    play_again = input("let's play again? Type 'no' to quit: ")
    if play_again.lower() == 'no':
     break
print('Hope you add fun playing this game')
            

    
       