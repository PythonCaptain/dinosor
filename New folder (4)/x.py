import pgzrun
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1000
HEIGHT = 700

background_menu = Actor("background_menu" , (500 , 350))
button_start = Actor("button_start" , (500 , 350))
button_setting = Actor("button_start" , (100 , 100))
background_game1 = Actor("background_game" , (500 , 350))
background_game2 = Actor("background_game" , (1500 , 350))

setting = False
sound = False
game = False
text = "sound_on"

def update():
    global text

    if sound:
        text = "sound_off"
        sounds.sound.stop()
    else:
        text = "sound_on"
        sounds.sound.play()

    if keyboard.right:
        background_game1.x -= 2
        background_game2.x -= 2
    elif keyboard.left and (background_game1.x <= 500 or background_game2.x <= 500):
        background_game1.x += 2
        background_game2.x += 2

    if background_game2.x == 500:
        background_game1.x = 1500
    if background_game1.x == 500:
        background_game2.x = 1500

def draw():
    global menu 

    def menu():
        background_menu.draw()
        button_start.draw()
        button_setting.draw()
        screen.draw.text("Start" , topleft = (430,335) , color = "black" , fontsize = 80)
        screen.draw.text("Setting" , topleft = (28,77) , color = "black" , fontsize = 60)
    menu()

    if setting:
        background_menu.draw()
        button_start.draw()
        button_setting.draw()
        screen.draw.text(f"{text}" , topleft = (430,335) , color = "black" , fontsize = 35)
        screen.draw.text("back" , topleft = (35,80) , color = "black" , fontsize = 60)  
    
    if game:
        background_game1.draw()
        background_game2.draw()

def on_mouse_down(pos):
    global setting , sound , game
    if game == False:
        if button_setting.collidepoint(pos) and setting == False:
            setting = True

        elif button_setting.collidepoint(pos) and setting:
            setting = False
            menu()



        if button_start.collidepoint(pos) and setting and sound == False:
            sound = True

        elif button_start.collidepoint(pos) and setting and sound:
            sound = False

    if button_start.collidepoint(pos) and setting == False:
        game = True
pgzrun.go()