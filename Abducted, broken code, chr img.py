import pygame, time
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((1280,680)) #the screen size

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

sc = (100, 250 , 0) #start button colour 

hc = (100, 255, 150) #highlight colour

timer = pygame.time.Clock() #lets us use the clock more easily

def textObj(msg, text): #this function mainly handles what colour the text has 
    textcolour =  textfont.render(msg, 1,  recc)
    return textcolour, textcolour.get_rect()

def text(msg, x, y, w, h, size): #this is the main function that creates the text and the position 
    global textfont
    textfont = pygame.font.SysFont('forte', size) #this is for the font of the text
    textscreen, textrecc = textObj(msg, textfont) #lets the text have colour and the font
    textrecc.center = ((x+(w/2)) , (y+(h/2))) #for the position of th text
    screen.blit(textscreen, textrecc) #puts the text on the screen
    
def button(msg, x, y, w, h, sc, hc, a): #creates a button the works and has words on it
    global mouse
    mouse = pygame.mouse.get_pos() #find where the mouse is
    click = pygame.mouse.get_pressed() #finds which mouse button is pressed
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y: # check is the mouse is with in the range of the button 
        pygame.draw.rect(screen, hc,(x,y,w,h)) #makes the button highlighted
        if click[0] == 1 and a == 1: #check if the left button is click
            Startaction() #calls for this action
        if click[0] == 1 and a == 2:
            Load()
    else:
        pygame.draw.rect(screen, sc, (x,y,w,h)) #or it would put back the button back to normal

    global textfont #the next few lines are just the text code just for the buttons
    textfont = pygame.font.SysFont('forte', 72)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = ((x+(w/2)) , (y+(h/2)))
    screen.blit(textscreen, textrecc)

def game(): #this is for the game to run
    global start
    start = True
    while start: # as long as start is true it will run continuously
        for event in pygame.event.get(): #gets the different events in pygame
            if event.type == pygame.QUIT: #if the user quit the game, this will in turn end the program    
                start = False

        screen.fill(colr) #makes the screen black
        button("Start", 465,350,350,100, sc, hc, 1) #creates a start button
        button("Load", 465,460,350,100, sc, hc, 2) #load button
        pygame.display.flip() #puts everything on to the display, which lets the user see it
        pygame.display.update()#updates the screen depending on the tick time
        timer.tick(15)#gives a tick time of 15 nino secons 
 
def Startaction(): #this lets the user click on the start button
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):#The range of which the mouse clicks 
                    print ("Hello") #just there to check if it works and still on the screen
                    screen.fill(colr)
                    text("Don't click the Screen! ", 100,300,1080,150, 100) 
                    pygame.display.update()
                    timer.tick(30) #updates the screen with a text to tell the user to not click the screen
                    pygame.time.delay(1500) #puts the code on  pause for a bit of time
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc,[100,50,335,400],5) #Draws rectangles on the screen
                    global ChrF
                    ChrF = pygame.image.load('Character - GirlV2.png')
                    screen.blit(ChrF, (100, 50))
                    pygame.display.update()
                    timer.tick(30)
                    pygame.draw.rect(screen, recc,[470,50,335,400],5)
                    pygame.draw.rect(screen, recc,[840,50,335,400],5)
                    text("Choose a character using 1, 2 or 3, Don't use Numb Pad", 50,500,1080,150, 50) #another text that tells the user what to do
                    pygame.display.flip()
                    Cchoice() #calls for the Cchoice functions

def Load():
    start = True
    while start:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             start = False
         if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
             if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 465 and mouse[1] < 565): #if within range, then fill the screen black and do the load screen
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc, [100, 50, 600, 200], 5)
                    pygame.display.flip()
                    
                    
def Cchoice(): # lets the user choose the character
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:# check if the the keyboard key is pressed
                if event.key == pygame.K_1: #check if the user press 1 
                    pygame.draw.rect(screen, hc,[100,50,335,400],5) #highlighs the box and let it stay there for a short amount of time
                    screen.blit(ChrF, (100, 50))
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("F") #calls for the female story and character 
                    pygame.display.update()
                    timer.tick(60)
                    start = False

                if event.key == pygame.K_2: #check if the user pressed 2 and calls for the male story
                    pygame.draw.rect(screen, hc, [470,50,335,400], 5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("M")
                    pygame.display.update()
                    timer.tick(10)
                    start = False
                    
                if event.key == pygame.K_3: #check if the user pressed 3 and plays the other story
                    pygame.draw.rect(screen, hc,[840,50,335,400],5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("O")
                    pygame.display.update()
                    timer.tick(10)
                    start = False

def story(a): #story function
    global char
    char = 0 #this is to help indicate which character is chosen 
    text("Greeting Player, I am  ", 100, 75, 1100, 100, 36) #general story 
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("You are Trapped  ", 100, 175, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("To escape", 100, 275, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("Listen to my intrustion carefully.", 100, 375, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("Be cautious, you are about to wake up.", 100, 475, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    text("Click space to continue -->", 100, 575, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    
    if a == "M": #this is the male sorry
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
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("He's been asleep for a while now", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial() #starts the actual game

    if a == "F":#female story
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
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("She's been asleep for a while now", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial()

    if a == "O": #other's story
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
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("They've been asleep for a while now", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial()

def Chr( x, y): #this is to load the character pic
    if char == 1: #female character
     Chrct = pygame.image.load('Girl drawing Larger.png') #loads the female character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(30)
    if char == 2: #male
     Chrct = pygame.image.load('Girl drawing Larger.png') #loads the male character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(30)
    if char == 3: #other
     Chrct = pygame.image.load('Girl drawing Larger.png') #loads the other character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(30)

def tutorial(): #starts the game and places the setting
       screen.fill(colr)
       pygame.draw.rect(screen, recc, [25, 25, 1230, 630])
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
        pygame.display.update()
        if x <= 38:
            x *= -1
        timer.tick(30)
            
   
game()
pygame.quit()   
