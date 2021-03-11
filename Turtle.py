from random import randint
from swampy.TurtleWorld import *
world=TurtleWorld()
import math
import turtle
# here i splitted the colors
colors="red,yellow,blue"
colors_pick=colors.split(",")
# here i gave the random numbers
random=randint(1,3)
probablity = randint(1, 99)
# this function does the semi circle
def yarim_daire(turtle,x):
    degree = 180.0 / (x*2)
    lt(turtle, 90)
    for i in range(x*2):
        fd(turtle, 1), rt(turtle, degree)

    lt(turtle, 90)
# this function does the whole things
def turtle(turn,name1,name2,color1,color2,bob,bob2):
    step_count1 = 0
    step_count2 = 0
    round = 0

    bob2.delay = 0.01
    bob.delay = 0.01
    bob.set_color(color1),bob2.set_color(color2),bob2.set_pen_color("white"),bob.set_pen_color("white"),bob.bk(180),bob2.set_pen_color("white"),bob2.rt(90),bob2.fd(80),bob2.rt(90),bob2.fd(180),bob2.lt(180),bob2.set_pen_color("blue") ,bob.set_pen_color("blue")

    while True:

        random_style=None
        random_style = randint(0, 2)
        if turn == 0:
            print name1 + " plays"
            print "******************Round %i *********************" % round

            step1 = input("How many steps would you like to take?:")
            percent1 = (100 - int(step1))
            if step1 > 100 or step1 < 0:
                round+=1
                step1=input("How many steps would you like to take?:")
                continue
            if probablity>=percent1:
                print "You Failed :(((("

            elif probablity <= percent1:
                print "success :)))))"
                step_count1+=percent1
                print "{} s score is {} ".format(name1,step_count1)

                if random_style==0:
                    fd(bob,percent1/5),lt(bob,90),fd(bob,percent1/5),rt(bob,90),fd(bob,percent1/5),lt(bob,90),fd(bob,percent1/5),rt(bob,90),fd(bob,percent1/5),rt(bob,90),fd(bob,percent1/5),lt(bob,90),fd(bob,percent1/5),rt(bob,90),fd(bob,percent1/5),lt(bob,90),fd(bob,percent1/5)
                elif random_style==1:
                    fd(bob,percent1)
                elif random_style==2:
                    yarim_daire(bob,percent1)

            if step_count1 >= 200:
                print "+++++++++++++++ %s WINS!!!!! +++++++++++++++" % name1
                ask1 = raw_input("Do you want to play another round(yes/no)? :")
                if ask1 == "yes":
                    step_count1 = 0
                    step_count2 = 0
                    bob2.die()
                    bob.die()
                    world.clear()
                    turtle2()
                elif ask1 == "no":
                    break
                elif ask1 != "yes" or ask1 != "no":
                    ask1 = raw_input("Do you want to play another round(yes/no)? :")
                    continue
            turn = 1
        else:
            print name2 + " plays"
            round += 1
            print "******************Round %i *********************" % round

            print "How many steps would you like to take?:"

            step2=input()
            percent2=100-int(step2)
            if step2>100 or step2<0:
                continue

            if probablity >=percent2:
                print "You Failed :(((("

            elif probablity <= percent2:
                print "sucecess :)))))"
                step_count2 +=percent2
                print "{} s score is {} ".format(name2,step_count2)

                if random_style==0:
                    fd(bob2, percent2 / 5), lt(bob2, 90), fd(bob2, percent2 / 5), rt(bob2, 90), fd(bob2, percent2 / 5), lt(bob2, 90), fd(bob2, percent2 / 5), rt(bob2, 90), fd(bob2, percent2 / 5), rt(bob2, 90), fd(bob2,percent2 / 5), lt( bob2, 90), fd(bob2, percent2 / 5), rt(bob2, 90), fd(bob2, percent2 / 5), lt(bob2, 90), fd(bob2,percent2 / 5)
                elif random_style == 1:
                    fd(bob2, percent2)

                elif random_style == 2:
                    yarim_daire(bob2, percent2)

            if step_count2 >= 200:
                print "+++++++++++++++ %s WINS!!!!! +++++++++++++++" % name1
                ask2 = raw_input("Do you want to play another round(yes/no)? :")
                if ask2 == "yes":
                    step_count1 = 0
                    step_count2 = 0
                    bob2.die()
                    bob.die()
                    world.clear()
                    turtle2()
                elif ask2 == "no":
                    break
                elif ask2 != "yes" or ask1 != "no":
                    ask2= raw_input("Do you want to play another round(yes/no)? :")
                    continue
            turn = 0

    print "BYE BYE"
    quit()
    return turn, name1, name2, color1, color2, bob, bob2
# in this function does the naming and and givinf colors
def turtle2():
    bob = Turtle()
    bob2 = Turtle()
    # turtle()
    turn = randint(0, 1)
    while True:
        print "---- FIRST Turtle----"
        name1 = raw_input("What is the name of first Turtle ?:")
        while name1 == "" or name1 == " ":
            print "Denominate a name for your Turtle"
            name1 = raw_input("What is the name of first Turtle ?")

        color1 = raw_input("Please select a color for your Turtle red-blue-yellow?").lower()
        while color1 not in colors_pick:
            print "{} is not a valid color, please select one of red-blue-yellow colors".format(color1)
            color1 = raw_input("Please select a color for your Turtle red-blue-yellow?").lower()

        print "---- SECOND Turtle----"
        name2 = raw_input("What is the name of second Turtle ?")
        while name1 == name2:
            name2 = raw_input("This Turtle name has taken !, please choose another name:")

        while name2 == "" or name2 == " ":
            print "Denomiate a name for your Turtle"
            name2 = raw_input("What is the name of second Turtle ?")
            continue
        color2 = raw_input("Please select a color for your Turtle red-blue-yellow?").lower()

        while color2 not in colors_pick or color2 == color1:
            print "{} is not a valid color or taken by first user please select one of red-blue-yellow colors".format(
                color2)
            color2 = raw_input("Please select a color for your Turtle red-blue-yellow?").lower()
            print type(color1)

        turn, name1, name2, color1, color2, bob, bob2 = turtle(turn, name1, name2, color1, color2, bob, bob2)
        break

turtle2()

wait_for_user()



