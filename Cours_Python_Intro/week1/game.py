import random

number = random.randint(0, 101)

while True:

    answer = input('Enter the number: ')
    if not answer or answer == 'exit':
        print(number)
        break

    if not answer.isdigit():
        print('Enter correct number!')
        continue

    user_answer = int(answer)

    if user_answer > number:
        print('Correct number is less')
    elif user_answer < number:
        print('Correct number is bigger')
    else:
        print('You\'re right')
        break
