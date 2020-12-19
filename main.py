import turtle as t
from playsound import playsound
import multiprocessing
import os
import sys
from time import sleep

# i was getting tired so i had to cut content

# necesary for the multiprocceing
if __name__ == '__main__':
    # turtle setup
    wn = t.Screen()
    canvas = wn.getcanvas()
    ui = t.Turtle()
    ui.speed(0)
    ui2 = t.Turtle()
    ui2.speed(0)

    ui.hideturtle()
    ui2.hideturtle()

    # Varuble setup
    colors = ["#000000", "#ffee36", "#4287f5"]

    # get sound file location
    sound = os.getcwd() + "/cyberpunk.wav"
    
    # replace backslashes with forward slashes to make it compatible with playsound
    sound = sound.replace(os.sep, '/')

    # Play the sound in a different procces so that turtle can still draw
    s = multiprocessing.Process(target = playsound, args = (sound,))
    s.start()

    # Functions

    def center_square(x,y,w,h):
        ui.penup()
        ui.goto(x,y)
        ui.pendown()
        ui.forward(w/2)
        ui.right(90)
        ui.forward(h)
        ui.right(90)
        ui.forward(w)
        ui.right(90)
        ui.forward(h)
        ui.right(90)
        ui.forward(w/2)
        ui.penup()

    def menu():
        wn.bgpic("tittle.png")
        center_square(0,-235,250,50)
        ui.goto(0,-275)
        ui.write("Press SPACE to start", align="center", font=("Arial",18, "normal"))
        
    def loading():
        ui.clear()
        center_square(0,-270,600,30)
        ui.goto(0,-270)
        ui.write("Loading...", align="center", font=("Arial",18, "normal"))
        ui2.pencolor(colors[2])
        ui2.penup()
        ui2.goto(0,-300)
        ui2.pendown()
        ui2.write("0%", align="center", font=("Arial",18, "normal"))
        ui.goto(-299, -299)
        ui.pendown()
        ui.pencolor(colors[1])
        ui2.pencolor(colors[0])
        for i in range(599):
            j = i/6
            k = str(int(j)) + "%"
            ui.left(90)
            ui.forward(28)
            ui.left(180)
            ui.forward(28)
            ui.left(90)
            ui.forward(1)
            ui2.clear()
            ui2.write(k, align="center", font=("Arial",18, "normal"))
        sleep(5)
        blue()

    def blue():
        wn.clear()
        wn.bgpic("blue.png")
        s.terminate()


    menu()

    wn.onkeypress(loading, "space")

    wn.listen()
    wn.mainloop()
