import random
# from flask import Flask

# app = Flask(__name__)
# @app.route("/")

def play():
    user = input("'r' for rock, 'p' for paper, or 's' for scissors /n What's your choice? \n type here: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "<h2>tie</h2>"
    
    if is_win(user, computer):
        return "<h2>you win</h2>"
    
    return "<h2>you lose</h2>"
        
def is_win(user, computer):
    if (user == 'p' and computer == 'r') or (user == 's' and computer == 'p') or (user == 'r' and computer == 's'): 
        return True
    
print (play())