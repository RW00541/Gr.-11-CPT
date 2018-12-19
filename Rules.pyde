def setup():
    size(640,480)
    background(0)
    
def draw():
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
    
def mouseClicked():
    if mouseX >= 520 and mouseY <= 70:
        print("All Good")
