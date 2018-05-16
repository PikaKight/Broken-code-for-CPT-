import pygame
from pygame.locals import*
import time

pygame.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

sc = (100, 250 , 0) #start button colour 

hc = (100, 255, 150) #highlight colour

timer = pygame.time.Clock()

def textObj(msg, text):
    textcolour =  textfont.render(msg, 1,  recc)
    return textcolour, textcolour.get_rect()

def text(msg, x, y, w, h, size):
    global textfont
    textfont = pygame.font.SysFont('forte', size)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = ((x+(w/2)) , (y+(h/2)))
    screen.blit(textscreen, textrecc)
    
def button(msg, x, y, w, h, sc, hc, a):
    global mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hc,(x,y,w,h))
        if click[0] == 1 and a == 1:
                Startaction()
    else:
        pygame.draw.rect(screen, sc, (x,y,w,h))

    global textfont
    textfont = pygame.font.SysFont('forte', 72)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = ((x+(w/2)) , (y+(h/2)))
    screen.blit(textscreen, textrecc)

def game(): #this is for the title
    global start
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        screen.fill(colr)
        button("Start", 465,350,350,100, sc, hc, 1)
        pygame.display.flip()
        pygame.display.update()
        timer.tick(15)
 
def Startaction():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):#The range of which the mouse clicks 
                    print ("Hello")
                    screen.fill(colr)
                    text("Don't click the Screen! ", 100,300,1080,150, 100)
                    pygame.display.update()
                    timer.tick(30)
                    pygame.time.delay(1500)
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc,[100,50,335,400],5)
                    pygame.draw.rect(screen, recc,[470,50,335,400],5)
                    pygame.draw.rect(screen, recc,[840,50,335,400],5)
                    text("Choose a character using 1, 2 or 3, Don't use Numb Pad", 50,500,1080,150, 50)
                    pygame.display.flip()
                    Cchoice()
                    
def Cchoice():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.draw.rect(screen, hc,[100,50,335,400],5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("M")
                    pygame.display.update()
                    timer.tick(60)
                    start = False

                if event.key == pygame.K_2:
                    pygame.draw.rect(screen, hc, [470,50,335,400], 5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("F")
                    pygame.display.update()
                    timer.tick(10)
                    start = False
                    
                if event.key == pygame.K_3:
                    pygame.draw.rect(screen, hc,[840,50,335,400],5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("O")
                    pygame.display.update()
                    timer.tick(10)
                    start = False

def story(a):
    global char
    char = 0
    text("Greeting Player, I am  ", 100, 75, 1100, 100, 50)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("You are Trapped  ", 100, 175, 1100, 100, 50)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("To escape", 100, 275, 1100, 100, 50)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("Listen to my intrustion carefully.", 100, 375, 1100, 100, 50)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("Be cautious, you are about to wake up.", 100, 475, 1100, 100, 50)
    pygame.display.update()
    timer.tick(30)
    text("Click space to continue -->", 100, 575, 1100, 100, 50)
    pygame.display.update()
    timer.tick(30)
    
    if a == "M":
        char = 1
        keypress = True
        while keypress:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keypress = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(colr)
                        pygame.time.delay(1000)
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 50)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("He's been asleep for a while now", 100, 175, 1100, 100, 50)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial()

    if a == "F":
        char = 2
        keypress = True
        while keypress:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keypress = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(colr)
                        pygame.time.delay(1000)
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 50)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("She's been asleep for a while now", 100, 175, 1100, 100, 50)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial()

    if a == "O":
        char = 3
        keypress = True
        while keypress:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keypress = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(colr)
                        pygame.time.delay(1000)
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 50)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("They've been asleep for a while now", 100, 175, 1100, 100, 50)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial()

def Chr( x, y):
    if char == 2:
     Chrct = pygame.image.load('Girl drawing Larger.png')
     screen.blit(Chrct, (x, y))

def tutorial():
       screen.fill(colr)
       pygame.draw.rect(screen, recc, [50, 50, 1000, 500], 5)
       pygame.display.flip()
       movement()

def movement():
    x = 100
    y = 100
    xc = 0
    yc = 0
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    yc -= 2
                if event.key == K_a:
                    xc -= 2
                if event.key == K_s:
                    yc += 2
                if event.key == K_d:
                    xc += 2
                    
        x += xc
        y+= yc
        Chr( x, y)
        if x <= 34: #these if statement are for the boundry of the charcter, BTW the top left corner is (0,0)
            x *= -1
        if  x >= 1170:
            x *= -1
        if  y <= 20:
            y *= -1
        if  y >= 570:
            y *= -1        
        pygame.display.update()
        timer.tick(30)
            
   
game()
pygame.quit()   
