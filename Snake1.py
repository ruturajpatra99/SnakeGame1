from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)

wn = Screen()
wn.title("Snake game by Ruturaj")
wn.bgcolor("brown")
wn.setup(width=458, height=558)
def change(x,y):     # CHANGE SNAKE DIRECTION
    aim.x = x
    aim.y = y

def inside(head):    # RETURN TRUE IF HEAD INSIDE THE BOUNDARIES
    return -230 < head.x < 210 and -270 < head.y < 265

def move():    # MOVE SNAKE IN FORWARD DIRECTION
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 10, 'red')
        update()
        return
    snake.append((head))

    if head == food:
        print('snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()


    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'orange')
    update()
    ontimer(move, 100)
print("press '2' for down\n\t'4' for left\n\t'6' for right\n\t'8' for up")
print("* SET YOUR HIGHSCORE *")

hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), '6')
onkey(lambda: change(-10, 0), '4')
onkey(lambda: change(0, 10), '8')
onkey(lambda: change(0, -10), '2')
move()
done()







