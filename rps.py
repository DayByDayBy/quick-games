import random

def play():
    user = input("'r' for rock, 'p' for paper, or 's' for scissors /n What's your choice? \n type here: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    
    if is_win(user, computer):
        return 'you win'
    
    return 'you lose'
        
def is_win(user, computer):
    if (user == 'p' and computer == 'r') or (user == 's' and computer == 'p') or (user == 'r' and computer == 's'): 
        return True
    
print (play())