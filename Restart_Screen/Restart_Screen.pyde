def setup():
    size(640, 480)
    background(0)
    
def draw():
    fill(255,0,0)
    rect(170, 300, 300, 120)
    fill(255)
    textSize(75)
    text("Restart", 190, 390)
    
def mouseClicked():
    if mouseX >= 170 and mouseX <= 470 and mouseY >= 300 and mouseY <= 420:
        print("success")
    
