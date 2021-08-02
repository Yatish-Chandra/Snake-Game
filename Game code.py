from turtle import *
import random
from freegames import square as sq
from freegames import vector as vc


food = vc(0,0)
snake = [vc(10,0)]
aim = vc(0,-10)


def change(x,y):
    aim.x = x
    aim.y = y

def inside (head):
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    head = snake[-1].copy()
    head.move(aim)


    if head in snake or not inside (head):
        sq(head.x, head.y, 9, 'red')
        update()
        return
    snake.append(head)

    if head == food:
        print('Snake : ',len(snake))
        food.x = random.randrange(-15,15)*10
        food.y = random.randrange(-15,15)*10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        sq(body.x, body.y, 9, 'green')

    sq(food.x, food.y, 9 , 'black')
    update()
    ontimer(move,100)


setup(420,420,370,0)

hideturtle()
tracer(False)


listen()
onkey( lambda : change(10,0), 'Right')
onkey( lambda : change(-10,0), 'Left')
onkey( lambda : change(0,10), 'Up')
onkey( lambda : change(0,-10), 'Down')
move()
done()
