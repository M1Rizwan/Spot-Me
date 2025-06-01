# The main file for the game logic. 

# Import requirements.
import turtle, pandas, random

screen = turtle.Screen()    
screen.title("Spot Me")
screen.setup(width=1300, height=700)
screen.addshape("House Objects2.gif")
turtle.shape("House Objects2.gif")

mdf = pandas.read_csv("cordinates.csv")   #Cordinates for each object on image, saved in the file.
objects_list = mdf["objects"].tolist()

correct_answer = []
answer = ""
score =0
while answer!= "exit":
    if score < 31:
        answer = screen.textinput(title=f"Score: {score}/31", prompt="Enter Object Name").lower()
    if answer=="exit" or score == 31:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(-256.0 , 296.0)
        tim.pencolor("red")
        if score == 31:
            tim.write(f"HURRAY!!! YOU GOT ALL CORRECT.", font=('Arial', 21, 'bold italic'))
        else:
            tim.write(f"THANKS!! YOU GOT {score} CORRECT OUT OF 31.", font=('Arial', 21, 'bold italic'))
        break

    if answer.replace(" ", "") in objects_list:
        if answer.replace(" ", "") not in correct_answer:
            score += 1
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        tom.goto(int(mdf[mdf["objects"] == answer.replace(" ", "")]["x"]), int(mdf[mdf["objects"] == answer.replace(" ", "")]["y"]))
        tom.pencolor(random.choice(["red","blue","green","black"]))
        tom.write(answer.title(), font=('Arial', 18, 'bold'))
        correct_answer.append(answer.replace(" ", ""))

if score < 31:
    help = screen.textinput(title=f"Need Answers?", prompt="Yes/No").lower()
    if help == "yes":
        turtle.clearscreen()
        screen.addshape("House Objects2.gif")
        turtle.shape("House Objects2.gif")
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        for item in objects_list:
            tom.goto(int(mdf[mdf["objects"] == item]["x"]), int(mdf[mdf["objects"] == item]["y"]))
            tom.pencolor(random.choice(["red", "blue", "green", "black"]))
            tom.write(item.title(), font=('Arial', 18, 'bold'))

screen.exitonclick()

