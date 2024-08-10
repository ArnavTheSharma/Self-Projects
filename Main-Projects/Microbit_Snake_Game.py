from microbit import *
# https://python.microbit.org/v/3

import random
dir == 0   #directions: 0=East, 1=South, 2=West, 3=North
end = False
dict = {0: [-1, -1], 1: [0,0]} #key=time(starts at 1), value=coordinates
apples = []
t = 1
xcor = 0
ycor = 0
length = 1
start = Image('50000:'
              '00000:'
              '00000:'
              '00000:'
              '00000')
display.show(start)

       
def stop(xcor, ycor, dict): #stops if snake touches edges or body
    if xcor==5 or xcor==-1 or ycor==5 or ycor==-1:
        display.show('Game Over')
        end == True
    for i in range(t-length, t):
        dict2 = dict[i]
        if xcor==dict2[0] and ycor==dict2[1]:
            end == True
    return end

def tail(xcor, ycor, t, dict, length): #deletes excess tail length and adds length if snake eats apple
    length1 = length
    apples1 = apple(dict, t, apples)
    t += 1
    dict[t] = [xcor, ycor]
    if t > length1:
        display.set_pixel(dict[t-length1][0],dict[t-length1][0],0)
    for k in range(0, len(apples)):
        if apples1[k][0] == xcor and apples1[k][1] == ycor:
            length1 += 1
    return length1
       
def apple(dict, t, apples): #creates apples and adds them to matrix 'apples'
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    for j in range(t-length, t):
        if x==dict[j][0] or y==dict[j][1]:
            apple(dict, t, apples)
    else:
        display.set_pixel(x, y, 10)
        apples.append([x, y])
    return apples

def main(dir, xcor, ycor):
    #directions: 0=East, 1=South, 2=West, 3=North
    if button_a.was_pressed():
        dir = (dir + 1) % 4
    if button_b.was_pressed():
        dir = (dir - 1) % 4
    if dir == 0:
        xcor += 1
    if dir == 1:
        ycor += 1
    if dir == 2:
        xcor -= 1
    if dir == 3:
        ycor -= 1
    display.set_pixel(xcor,ycor,3)
    return dir

from microbit import *
import random
dir == 0   #directions: 0=East, 1=South, 2=West, 3=North
end = False
dict = {0: [-1, -1], 1: [0,0]} #key=time(starts at 1), value=coordinates
apples = []
t = 1
xcor = 0
ycor = 0
length = 1
start = Image('50000:'
              '00000:'
              '00000:'
              '00000:'
              '00000')
display.show(start)

       
def stop(xcor, ycor, dict): #stops if snake touches walls or body
    if xcor==5 or xcor==-1 or ycor==5 or ycor==-1:
        display.show('Game Over')
        end == True
    for i in range(t-length, t):
        dict2 = dict[i]
        if xcor==dict2[0] and ycor==dict2[1]:
            end == True
    return end

def tail(xcor, ycor, t, dict, length): #deletes excess tail length and adds length if snake eats apple
    length1 = length
    apples1 = apple(dict, t, apples)
    t += 1
    dict[t] = [xcor, ycor]
    if t > length1:
        display.set_pixel(dict[t-length1][0],dict[t-length1][0],0)
    for k in range(0, len(apples)):
        if apples1[k][0] == xcor and apples1[k][1] == ycor:
            length1 += 1
    return length1
       
def apple(dict, t, apples): #creates apples and adds them to matrix 'apples'
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    for j in range(t-length, t):
        if x==dict[j][0] or y==dict[j][1]:
            apple(dict, t, apples)
    else:
        display.set_pixel(x, y, 10)
        apples.append([x, y])
    return apples

def main(dir, xcor, ycor):
    #directions: 0=East, 1=South, 2=West, 3=North
    if button_a.was_pressed():
        dir = (dir + 1) % 4
    if button_b.was_pressed():
        dir = (dir - 1) % 4
    if dir == 0:
        xcor += 1
    if dir == 1:
        ycor += 1
    if dir == 2:
        xcor -= 1
    if dir == 3:
        ycor -= 1
    display.set_pixel(xcor,ycor,3)
    return dir


while end == False:
    main(dir, xcor, ycor)
    sleep(200)
     
while end == False:
    main(dir, xcor, ycor)
    sleep(200)
