import random
def gamein(computer,you):
    if computer == you:
        return None
    elif computer == 'Rock':
        if you == 'Scissor':
            return True
        elif you == 'Paper':
            return False
    elif computer == 'Paper':
        if you == 'Rock':
            return True
        elif you == 'Scissor':
            return False
    elif computer == 'Scissor':
        if you == 'Paper':
            return True
        elif you == 'Rock':
            return False


#print('computer turn : Rock ,Paper or Scissor ?')
randno = random.randint(1,3)
if randno == 1:
    computer = 'Rock'
elif randno == 2:
    computer = 'Paper'
elif randno == 3:
    computer = 'Scissor'

you = input('your turn : Rock, Paper or Scissor? = ')
a = gamein(computer,you)
print(f'computer choose {computer}')
print(f'your choose {you}')

if a == None:
    print('match is tie')
elif a == True:
    print('you losse shhhh')
else :
    print('you win hurray ')
