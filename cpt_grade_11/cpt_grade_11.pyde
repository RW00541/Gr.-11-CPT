import random
SKY_BLUE = color(0, 191, 255)
flashes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
computers_choices = []
users_choices = []
square_list = []
counter = 0
lives = 3
colors = []
player_turn = False
num_of_flashes = 50
gamestatus = 'startscreen'
user_math_anw = ''
num1 = num2 = num3 = score = math_counter = 0
error = ''
incorrect = ''
difficulty = ''
hearts = []


def setup():
    global hearts
    size(640, 480)
    colors.append(color(255))
    colors.append(color(255, 0, 0))
    colors.append(color(0, 255, 0))
    colors.append(color(0, 0, 255))
    colors.append(color(0, 255, 255))
    colors.append(color(255, 255, 0))
    colors.append(color(255, 234, 126))
    colors.append(color(255, 0, 123))
    colors.append(color(255, 125, 0))
    square_list.append(squares(colors[0], 50, 50))
    square_list.append(squares(colors[1], 50, 200))
    square_list.append(squares(colors[2], 50, 350))
    square_list.append(squares(colors[3], 250, 50))
    square_list.append(squares(colors[4], 250, 200))
    square_list.append(squares(colors[5], 250, 350))
    square_list.append(squares(colors[6], 450, 50))
    square_list.append(squares(colors[7], 450, 200))
    square_list.append(squares(colors[8], 450, 350))


def display_squares(counter):
    if counter % 10 == 5:
        ran = random.choice(flashes)
        square_list[ran].colour = color(0)
        computers_choices.append(ran)
    elif counter % 10 == 0:
        for square in range(len(square_list)):
            square_list[square].colour = colors[square]
    for square in square_list:
        square.drawsquare()


def choose_num():
    num = random.randint(1, 12)
    return num


def testplayer():
    global player_turn
    player_turn = True


class squares:
    def __init__(self, colour, location_x, location_y):
        self.colour = color(colour)
        self.location_x = location_x
        self.location_y = location_y
        self.width = 100
        self.height = 100

    def drawsquare(self):
        fill(self.colour)
        rect(self.location_x, self.location_y, self.width, self.height)


def end_screen():
    textSize(100)
    fill(255, 0, 0)
    text("GAME OVER!", 20, 125)
    textSize(20)
    text("You completed {} levels on {} before running out of lives".format(score, difficulty), 10, 175)
    fill(255, 0, 0)
    rect(170, 300, 300, 120)
    fill(255)
    textSize(75)
    text("Restart", 190, 390)


def level_screen():
    fill(255)
    rect(120, 80, 100, 100)
    fill(255, 0, 0)
    rect(120, 260, 100, 100)
    fill(0, 255, 0)
    rect(380, 80, 100, 100)
    fill(0, 0, 255)
    rect(380, 260, 100, 100)
    fill(255, 165, 0)
    textSize(35)
    text("Easy", 130, 140)
    textSize(26)
    text("Normal", 385, 140)
    textSize(33)
    text("Hard", 130, 320)
    text("Very", 390, 305)
    text("Hard", 390, 350)


def display_math(num1, num2, num3, user_math_anw):
    textSize(30)
    fill(255, 0, 0)
    text("Now answer this math question", 100, 100)
    textSize(50)
    text("{} + {} x {} = {}".format(num1, num2, num3, user_math_anw), 100, 200)
    textSize(30)
    text('press "a" to enter', 100, 350)
    text("{}".format(error), 100, 400)
    text("{}".format(incorrect), 100, 300)
    text("After that, repeat the sequence", 100, 450)


def start_screen():
    textSize(180)
    fill(0, 0, 255)
    text("G", 10, 200)
    fill(0, 255, 0)
    text("e", 140, 200)
    fill(255, 0, 0)
    text("o", 240, 200)
    fill(255, 255, 0)
    text("r", 350, 200)
    fill(0, 255, 255)
    text("g", 430, 200)
    fill(255, 0, 255)
    text("e", 540, 200)
    fill(255)
    rect(200, 300, 225, 90)
    fill(255, 0, 0)
    textSize(65)
    text("START", 210, 370)


def rule_screen():
    textSize(150)
    fill(255)
    text("RULES", 40, 140)
    textSize(25)
    text("1: Select your difficulty", 10, 180)
    text("2: The squares at the center of the screen will flash", 10, 220)
    text("3: Memorize the sequence as it flashes", 10, 260)
    text("4: Repeat the sequence by clicking the squares", 10, 300)
    text("5: If you are wrong, you lose a life, be careful!!!", 10, 340)
    text("6: For every level you pass, you get 1 point", 10, 380)
    text("7: You only have 3 lives, don't get things wrong!", 10, 420)
    text("8: Play until your lives are gone, aim for the top", 10, 460)
    textSize(18)
    text("Click here", 520, 40)
    text("to continue", 520, 60)


def draw():
    global counter
    global lives
    global num_of_flashes
    global score
    global computers_choices
    global users_choices
    global num1
    global num2
    global num3
    global gamestatus
    global math_counter
    background(SKY_BLUE)
    if gamestatus == 'startscreen':
        start_screen()
    elif gamestatus == 'rulescreen':
        rule_screen()
    elif gamestatus == 'levelscreen':
        for life in range(lives):
            hearts.append(loadImage("heart.png"))
        lives = 3
        level_screen()
    else:
        if lives != 0:
            if gamestatus == 'math':
                display_math(num1, num2, num3, user_math_anw)
            else:
                for num in range(lives):
                    image(hearts[num], num*20 + 550, 10, 20, 20)
                fill(255)
                textSize(20)
                text("score: {}".format(score), 20, 20)
                if counter <= num_of_flashes:
                    counter += 0.5
                    display_squares(counter)
                    num1 = choose_num()
                    num2 = choose_num()
                    num3 = choose_num()
                elif math_counter % 4 == 3:
                    gamestatus = 'math'
                else:
                    counter += 0.5
                    display_squares(0)
                    fill(255)
                    text("users choice: {}".format(users_choices), 20, height - 5)
                    testplayer()
                    if len(users_choices) == len(computers_choices):
                        correctness = check_if_correct(users_choices, computers_choices)
                        print(users_choices)
                        print(computers_choices)
                        if correctness:
                            score += 1
                            counter = -5
                            users_choices = []
                            computers_choices = []
                            if difficulty == 'easy':
                                if score % 5 == 4:
                                    num_of_flashes += 10
                            elif difficulty == 'medium':
                                if score % 3 == 2:
                                    num_of_flashes += 10
                            elif difficulty == 'hard':
                                math_counter += 1
                                if score % 3 == 2:
                                    num_of_flashes += 10
                            elif difficulty == 'very hard':
                                math_counter += 2
                                num_of_flashes += 20
                        else:
                            lives -= 1
                            hearts.pop(len(hearts)-1)
                            counter = -5
                            users_choices = []
                            computers_choices = []
        else:
            gamestatus = 'endscreen'
        if gamestatus == 'endscreen':
            end_screen()


def check_if_correct(users_choices, computers_choices):
    if users_choices == computers_choices:
        return True
    else:
        return False


def check_math(num1, num2, num3, user_math_anw):
    global error
    global incorrect
    math_anwser = num2*num3+num1
    try:
        user_math_anw = int(user_math_anw)
    except:
        error = 'Please enter a number'
    else:
        if math_anwser == user_math_anw:
            return True
        else:
            incorrect = 'Incorrect anwser'


def test():
    assert check_if_correct([1, 2, 3, 4, 5], [8, 7, 8, 1, 3]) == False, 'should return false'
    assert check_if_correct([], []) == True, 'should return true'
    assert check_if_correct([2, 3, 1, 4, 5, 8], [2, 3, 1, 4, 5, 8]) == True, 'should return true'
    assert check_math(1, 1, 5, 6) == True, 'should return true'
    assert check_math(69, 21, 144, 3093) == True, 'should be true'
    assert check_math(11, 11, 11, 132) == True, 'should be true'
    print('all passed')

test()


def mouseClicked():
    global gamestatus
    global computers_choices
    global users_choices
    global num_of_flashes
    global score
    global math_counter
    global difficulty
    while gamestatus == 'startscreen':
        if mouseY >= 300 and mouseY <= 390 and mouseX >= 200 and mouseX <= 425:
            gamestatus = 'rulescreen'
    if gamestatus == 'rulescreen':
        if mouseX >= 520 and mouseY <= 70:
            gamestatus = 'levelscreen'
    if gamestatus == 'levelscreen':
        if mouseX >= 120 and mouseX <= 200 and mouseY >= 80 and mouseY <= 180:
            gamestatus = 'playing'
            difficulty = 'easy'
        if mouseX >= 380 and mouseX <= 480 and mouseY >= 80 and mouseY <= 180:
            gamestatus = 'playing'
            difficulty = 'medium'
        if mouseX >= 120 and mouseX <= 200 and mouseY >= 260 and mouseY <= 360:
            gamestatus = 'playing'
            difficulty = 'hard'
        if mouseX >= 380 and mouseX <= 480 and mouseY >= 260 and mouseY <= 360:
            gamestatus = 'playing'
            difficulty = 'very hard'
    if player_turn == True:
        if len(users_choices) == len(computers_choices):
            player_turn == False
        elif mouseX > square_list[0].location_x and mouseX < square_list[0].location_x+100 and mouseY > square_list[0].location_y and mouseY < square_list[0].location_y+100:
            users_choices.append(0)
        elif mouseX > square_list[1].location_x and mouseX < square_list[1].location_x+100 and mouseY > square_list[1].location_y and mouseY < square_list[1].location_y+100:
            users_choices.append(1)
        elif mouseX > square_list[2].location_x and mouseX < square_list[2].location_x+100 and mouseY > square_list[2].location_y and mouseY < square_list[2].location_y+100:
            users_choices.append(2)
        elif mouseX > square_list[3].location_x and mouseX < square_list[3].location_x+100 and mouseY > square_list[3].location_y and mouseY < square_list[3].location_y+100:
            users_choices.append(3)
        elif mouseX > square_list[4].location_x and mouseX < square_list[4].location_x+100 and mouseY > square_list[4].location_y and mouseY < square_list[4].location_y+100:
            users_choices.append(4)
        elif mouseX > square_list[5].location_x and mouseX < square_list[5].location_x+100 and mouseY > square_list[5].location_y and mouseY < square_list[5].location_y+100:
            users_choices.append(5)
        elif mouseX > square_list[6].location_x and mouseX < square_list[6].location_x+100 and mouseY > square_list[6].location_y and mouseY < square_list[6].location_y+100:
            users_choices.append(6)
        elif mouseX > square_list[7].location_x and mouseX < square_list[7].location_x+100 and mouseY > square_list[7].location_y and mouseY < square_list[7].location_y+100:
            users_choices.append(7)
        elif mouseX > square_list[8].location_x and mouseX < square_list[8].location_x+100 and mouseY > square_list[8].location_y and mouseY < square_list[8].location_y+100:
            users_choices.append(8)
    if gamestatus == 'endscreen':
        if mouseX >= 170 and mouseX <= 470 and mouseY >= 300 and mouseY <= 420:
            num_of_flashes = 50
            score = 0
            math_counter = 0
            gamestatus = 'levelscreen'


def keyPressed():
    global user_math_anw
    global gamestatus
    global math_counter
    if gamestatus == 'math':
        if keyCode == 48:
            user_math_anw += '0'
        if keyCode == 49:
            user_math_anw += '1'
        if keyCode == 50:
            user_math_anw += '2'
        if keyCode == 51:
            user_math_anw += '3'
        if keyCode == 52:
            user_math_anw += '4'
        if keyCode == 53:
            user_math_anw += '5'
        if keyCode == 54:
            user_math_anw += '6'
        if keyCode == 55:
            user_math_anw += '7'
        if keyCode == 56:
            user_math_anw += '8'
        if keyCode == 57:
            user_math_anw += '9'
        if keyCode == 8:
            user_math_anw = user_math_anw[:-1]
        if keyCode == 65:
            math_correctness = check_math(num1, num2, num3, user_math_anw)
            if math_correctness:
                math_counter += 1
                gamestatus = 'playing'
