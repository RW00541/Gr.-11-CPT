def setup():
    size(640,480)
    background(0)
    
def draw(): 
    fill(255)
    rect(120, 80, 100, 100)
    fill(255,0,0)
    rect(120, 260, 100, 100)
    fill(0,255,0)
    rect(380, 80, 100, 100)
    fill(0,0,255)
    rect(380, 260, 100, 100)
    fill(255,165,0)
    textSize(35)
    text("Easy", 130, 140)
    textSize(26)
    text("Normal", 385, 140)
    textSize(33)
    text("Hard", 130, 320)
    text("Very", 390, 305)
    text("Hard", 390, 350)
    
def mouseClicked():
    if mouseX >= 120 and mouseX <= 200 and mouseY >= 80 and mouseY <= 180:
        print("Easy")
    if mouseX >= 380 and mouseX <= 480 and mouseY >= 80 and mouseY <= 180:
        print("Normal")
    if mouseX >= 120 and mouseX <= 200 and mouseY >= 260 and mouseY <= 360:
        print("Hard")
    if mouseX >= 380 and mouseX <= 480 and mouseY >= 260 and mouseY <= 360:
        print("Very Hard")
