import pygame
import random
pygame.init()
#colors
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
#creating game window
displayWidth=800
displayHeight=600
gamedisplay=pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('One-Piece')
img=pygame.image.load('snakehead.png')
img1=pygame.image.load('snakehead2.png')

apple=pygame.image.load('apple.png')
clock=pygame.time.Clock()
direction="right"
#game methods
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)
def textObjects(msg,color,size):
    if size=="small":
        textsurf=smallfont.render(msg,True,color)
    if size=="medium":
        textsurf=medfont.render(msg,True,color)
    if size=="large":
        textsurf=largefont.render(msg,True,color)        
    return textsurf,textsurf.get_rect()
def message(msg,color,y_displace=0,size="small"):
    #screenDisplay=font.render(msg,True,color)
    #gamedisplay.blit(screenDisplay,[displayWidth/2,displayHeight/2])
    textsurf,textRect=textObjects(msg,color,size)
    textRect.center=(displayWidth/2),(displayHeight/2)+y_displace
    gamedisplay.blit(textsurf,textRect)
def points(text,score,color):
    text=text+score
    text_surf=smallfont.render(text,True,color)
    text_rect=text_surf.get_rect()
    text_rect.x=displayWidth-125
    text_rect.y=0
    gamedisplay.blit(text_surf,text_rect)
    
def snake(blocksize,snakelist):
    if direction=="right":
        head=pygame.transform.rotate(img,270)
    if direction=="left":
        head=pygame.transform.rotate(img,90)
    if direction=="up":
        head=img
    if direction=="down":
        head=pygame.transform.rotate(img,180)
    
    gamedisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))
    pygame.display.update()
    for xny in snakelist[:-1]:
        
        pygame.draw.rect(gamedisplay,green,[xny[0],xny[1],blocksize,blocksize])
        
def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_c:
                    paused=False
        gamedisplay.fill(black)
        message("paused",white,-50,"large")
        message("press c to continue q to quit",green,50)
        pygame.display.update()
        clock.tick(10)
                    
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gamedisplay.fill(black)
        message("Welcome to One-Piece",red,-60,"medium")
        message("press s to start q to quit and p to pause ",white,50)
        pygame.display.update()
        clock.tick(10)
    
    




#game loop
def game():
    #game objects
    global direction
    blocksize=20
    lead_x=displayWidth/2
    lead_y=displayHeight/2
    lead_x_change=10
    lead_y_change=0
    randApplex=round(random.randrange(0,displayWidth-blocksize))#/10.0)*10.0
    randAppley=round(random.randrange(30,displayHeight-blocksize))#/10.0)*10.0
    appleSize=20
    snakelist=[]
    snakelength=1
    
    FPS=15
    score=0
    #loop variables
    gameExit=False
    gameOver=False
    while not gameExit:
        while gameOver==True:
            gamedisplay.fill(black)
            message("score: "+str(score),green,-200,"medium")
            message("Game Over",red,-50,"large")
            message("Press c to play again q to quit",white,50,"medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                    gameOver=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        game()
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-10
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change=10
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_x_change=0
                    lead_y_change=-10
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead_x_change=0
                    lead_y_change=10  
                elif event.key==pygame.K_p:
                    pause()
                    
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
         # no chance should be given to cross over so making collision of every pixel so accurate eventhough if we do not round 
         # co ordinates of apple 
        if (lead_x>=randApplex and lead_x<=randApplex+appleSize) or (lead_x+blocksize>=randApplex and lead_x+blocksize<=randApplex+appleSize):
            if lead_y>=randAppley and lead_y<=randAppley+appleSize:
                randApplex=round(random.randrange(0,displayWidth-blocksize))#/10.0)*10.0
                randAppley=round(random.randrange(0,displayHeight-blocksize))#/10.0)*10.0
                snakelength+=1
                score+=1
            elif lead_y+blocksize>=randAppley and lead_y+blocksize<=randAppley+appleSize:
                randApplex=round(random.randrange(0,displayWidth-blocksize))#/10.0)*10.0
                randAppley=round(random.randrange(0,displayHeight-blocksize))#/10.0)*10.0
                snakelength+=1
                score+=1
               
            
            
        if lead_x>=displayWidth or lead_x<=0 or lead_y>=displayHeight or lead_y<=0:
            gameOver=True
        for eachsegement in snakelist[:-1]:
            if eachsegement==snakehead:
                gameOver=True
        
        gamedisplay.fill(black)
        snake(blocksize, snakelist)
        gamedisplay.blit(apple,[randApplex,randAppley])
        #pygame.draw.rect(gamedisplay,white,[randApplex,randAppley,appleSize,appleSize])
        points("score : ",str(score),red)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

game_intro()
game()
