import turtle as t
import random

game_on =False
ycor = 0
my_screen = t.Screen()
my_screen.setup(width = 500, height= 400)
color_list = ['pink', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


def moveahead(T):
    n = random.randint(10,50)
    T.fd(n)


def moveback(T):
    n = random.randint(9,10)
    T.bk(n)

#user guesses the color
guess = my_screen.textinput(title = "Place bet", prompt="Which color will win ? ")
if guess:
    game_on = True

#Create a list and append the turtles with color as random, in a for loop
turtle_list = []
for i in range (7):
    
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[i])
    new_turtle.goto(x= -230, y= -105+ycor)
    ycor += 35
    turtle_list.append(new_turtle)



while game_on:
    #start the race 
    for cartel in turtle_list:
        if cartel.xcor() > 230:
            game_on= False
            winner = cartel.pencolor()
            if guess == winner:
                print(f"Lesss Go!, {winner.title()} Won")
            
            else:
                print(f"Better luck next time! {winner.title()} Won")
        else:
            random.choice([moveahead(cartel),moveback(cartel)])

my_screen.exitonclick()