levels_completed = [1,2,3,4,5,6,7,8,9,10]

def setup():
    size(640,480)
    background(0)
    
def final_scores(levels_completed):
    total = 0
    for level in levels_completed:
        total += 1
    return total

def draw():
    textSize(100)
    fill(255,0,0)
    text("GAME OVER!",20, 125)
    textSize(20)
    fill(255)
    total = final_scores(levels_completed)
    text("You completed {} levels before running out of lives".format(total), 80, 175)
    textSize(35)
    text("Levels completed on Easy: ", 20, 240)
    text("Levels completed on Medium: ", 20, 300)
    text("Levels completed on Hard: ", 20, 360)
    text("Levels completed on Very Hard: ", 20, 420)
    
    


    
