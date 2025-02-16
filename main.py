import pgzrun
import random
WIDTH = 800
HEIGHT = 450
titlebox = Rect(0,0, 800,100) 
questionbox = Rect(0,110, 600,100)
anwserbox1 = Rect(0,220, 290,100)
anwserbox2 = Rect(310,220, 290,100 )
anwserbox3 = Rect(0,330, 290,100 )
anwserbox4 = Rect(310,330, 290,100 )
timerbox = Rect(610,110, 180,100)
skipbox = Rect(610,220, 180,100 )
resetbox = Rect(610,330, 180,100)
timeleft = 10
score = 0
questionfile = "question.txt"
questions = []
question_count = 0
question_index = 0
anwserbox = [anwserbox1, anwserbox2, anwserbox3, anwserbox4]
def draw():
    screen.fill("light green")
    screen.draw.filled_rect(titlebox, "pink")
    screen.draw.filled_rect(questionbox, "light blue")
    screen.draw.filled_rect(anwserbox1, (226, 184, 252))
    screen.draw.filled_rect(anwserbox2, (226, 184, 252))
    screen.draw.filled_rect(anwserbox3, (226, 184, 252))
    screen.draw.filled_rect(anwserbox4, (226, 184, 252))
    screen.draw.filled_rect(timerbox, (79, 201, 183))
    screen.draw.filled_rect(skipbox, (79, 201, 183))
    screen.draw.filled_rect(resetbox, (79, 201, 183))
    screen.draw.textbox("Welcome to a Christmas Trivia", titlebox, color="white")
    screen.draw.textbox("Reset", resetbox, color=(217, 251, 255))
    screen.draw.textbox("Skip", skipbox, color=(217, 251, 255))   
    screen.draw.textbox(str(timeleft), timerbox, color=(217, 251, 255))
    screen.draw.textbox(question[0], questionbox, color=(17, 2, 110))
    screen.draw.textbox(question[1], anwserbox1, color=(139, 25, 209))
    screen.draw.textbox(question[2], anwserbox2, color=(139, 25, 209))
    screen.draw.textbox(question[3], anwserbox3, color=(139, 25, 209))
    screen.draw.textbox(question[4], anwserbox4, color=(139, 25, 209))    
def readquestionfile():
    global question_count, questions
    file = open(questionfile, "r")
    print(file)
    for question in file:
        questions.append(question)
        question_count += 1
    
    print(questions)
    file.close()
def readnextquestion():
    global question_index
    question_index += 1
    return questions.pop(0).split("|")
def   on_mouse_down(pos):
    global timeleft, question, score
    index = 1
    for anwser in anwserbox:
        if anwser.collidepoint(pos):
            if index is int(question[5]):
                print("correct answer")
                score += 1
                if questions:
                    question = readnextquestion()
                    timeleft = 10
                else:
                    print("end of questions")
                    message = "game over your score is "+ str(score)
                    question = [message, "-", "-", "-", "-", 5]
                    timeleft = 0 


            else:
                print("you got it wrong LOL")
                message = "game over"
                question = [message, "-", "-", "-", "-", 5]
                timeleft = 0            
        index += 1
    if resetbox.collidepoint(pos):
        resetgame()

    if skipbox.collidepoint(pos):    
        skipquestion()
def skipquestion():
    global timeleft, questions, question
    if questions:
        question = readnextquestion()
        timeleft = 10
    else:
        print("end of questions")
        message = "game over your score is "+ str(score)
        question = [message, "-", "-", "-", "-", 5]
        timeleft = 0 

def updatetime():

    global timeleft, question
    if timeleft:

        timeleft-= 1
    else:
        message = "You Ran Out Of Time"
        question = [message, "-", "-", "-", "-", 5]

def resetgame():
    global timeleft, question, questions, score, question_count, question_index 
    timeleft = 10
    score = 0  
    question_count = 0
    question_index = 0
    questions = []
    readquestionfile()
    question = readnextquestion()






readquestionfile()
question = readnextquestion()
print(question)
clock.schedule_interval(updatetime,1)
pgzrun.go()
