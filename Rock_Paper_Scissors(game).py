rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choose=eval(input('What do you choose? Type 0 for Rock, 1 for Paper,2 for Scissors.'))

computer_chose = random.randint(0,2)
if choose==0 and computer_chose==0:
  print(rock)
  print(rock)
  print('Draw')
elif choose==0 and computer_chose==1:
  print(rock)
  print(paper)
  print('You lose')
elif choose==0 and computer_chose==2:
  print(rock)
  print(scissors)
  print('You win')
elif choose==1 and computer_chose==0:
  print(paper)
  print('computer chose\n:',rock)
  print('You win')
elif choose==1 and computer_chose==1:
  print('Draw')
elif choose==1 and computer_chose==2:
  print('You lose')
elif choose==2 and computer_chose==0:
  print('You lose')
elif choose==2 and computer_chose==1:
  print('You win')
elif choose==2 and computer_chose==2:
  print('Draw')


