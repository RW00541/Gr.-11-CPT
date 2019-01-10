import random
user_answer = []

def setup():
    size(640,480)
    background(0)
    
def math():
    num1 = random.randint(1,99)
    num2 = random.randint(1,12)
    num3 = random.randint(1,12)
    answer = num1 + num2 * num3
    textSize(100)
    fill(255,0,0)
    text("{} + {} x {}".format(num1, num2, num3),300, 200)    

def user_input():
    global user_answer
    if keyCode == 48:
        user_answer.append(0)
    if keyCode == 49:
        user_answer.append(1)
    if keyCode == 50:
        user_answer.append(2)
    if keyCode == 51:
        user_answer.append(3)
    if keyCode == 52:
        user_answer.append(4)
    if keyCode == 53:
        user_answer.append(5)
    if keyCode == 54:
        user_answer.append(6)
    if keyCode == 55:
        user_answer.append(7)
    if keyCode == 56:
        user_answer.append(8)
    if keyCode == 57:
        user_answer.append(9)
    
def answer_test():
    math()
    
    user_input()
    try:
        int(user_input)
    except:
        text("Invalid input: Please enter numbers")
        user_input()
    else:
        if answer == user_answer:
            text("correct")
        else:
            text("Wrong answer, try again!")

def keyPressed():
    while keyCode != 13:
        user_input()
        
        
def draw():
    math()
    

    
