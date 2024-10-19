
import pgzrun

TITLE = "Quiz Master"


marquee_box = Rect(0,0,700,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,100,100)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,200,380)

score = 0
time_left = 10
question_file_name = "questions.txt"
marquee_message = ""
is_game_over = False

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip_box, "dark green")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark orange")
    

    marquee_message = f"Welcome To Quiz Master ... Q: {question_index} of {question_count}"

    screen.draw.textbox( marquee_message ,marquee_box,color="white")
    screen.draw.textbox( str(time_left) ,timer_box,color="white")
    screen.draw.textbox("Skip" ,skip_box,color="black",angle=-90)
    screen.draw.textbox(quest[0] ,question_box,color="white",)

    index=1
    for i in answer_boxes:
     screen.draw.textbox(quest[index] ,i,color="black")
     index+=1

def mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(quest[5]):
                correct_answer()
            else:
                game_over()
        index+=1
def correct_answer():
    global quest,score,questions
    score+=1
    if questions:
        quest=read_next_question()
    else:
        game_over()

def game_over():
    global is_game_over,message,time_left
    message=f"Game over ! you got {score} questions corrct!"
    quset=[message,"-","-","-","-",5]
    time_left=0
    is_game_over=True






def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for i in q_file:
        questions.append(i)
        question_count+=1
    q_file.close()

def read_next_question():
    global question_index
    question_index+=1
    return questions.pop(0).split(",")

read_question_file()
quest=read_next_question()
print(quest)
pgzrun.go()