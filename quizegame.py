import requests
import json
import pprint
import random
import html

options =[]
correct_score = 0
incorrect_score = 0
total_qustion_answered = 0
while True:
    r = requests.get('https://opentdb.com/api.php?amount=1')
    if(r.status_code!=200):
        print('\nSorry there is a network error. Failed to get the question from server')
    else:
        question = json.loads(r.text)
        correct_answer = question['results'][0]['correct_answer']
        options.append(correct_answer)
        for asw in question['results'][0]['incorrect_answers']:
            options.append(asw)
        print('\n')
        print(html.unescape(question['results'][0]['question']))
        total_qustion_answered+=1
        random.shuffle(options)
        print('\nchoose answer from the options below:\n')
        option_number = 1
        valid_answer = False
        for option in options:
            print(str(option_number)+' '+html.unescape(option))
            option_number += 1
        while valid_answer==False:
            answer = input('\nType the number of coreect answer: ')
            try:
                answer  = int(answer )
                if answer > len(options) or answer <=0:
                    print('\nInvalid answer.')
                else:
                    valid_answer=True #jump out of the loop
            except:
                print('\nInvalide answer. Use only numbers')
        while True:
            if correct_answer==options[answer-1]:
                correct_score+=1
                print('\nCongratulation! the answer', html.unescape(correct_answer), 'is correct')
                break
            else:
                print('\nYour answer is incorrect. correct answer is:',html.unescape(correct_answer))
                incorrect_score+=1
                break
        options.clear()
        play_again = input("\nPress enter to continue or Type 'quit' to quit end game: ")
        if play_again.lower() == 'quit':
            break
print('\nHope you add fun playing this game')
print('Your correct answer(s) is', correct_score)
print('Your incorrect answer(s) is', incorrect_score)
print('Your total question(s) is', total_qustion_answered,'\n')


    
