#import pygame library
import pygame,sys,random,math,os
from tkinter import messagebox

#player animation
def playeranimation():
    if player1.top<=10:
        player1.top=10
    if player1.bottom>=screenheight-10:
        player1.bottom=screenheight-10
    if player2.top<=10:
        player2.top=10
    if player2.bottom>=screenheight-10:
        player2.bottom=screenheight-10

#ball animation
def ballanimation():
    global ballspeedx,ballspeedy,player1score,player2score,scoretime,win1time,win2time
    
    #speed
    ball.x+=ballspeedx
    ball.y+=ballspeedy   
    
    #bounce back and regeneration
    if ball.top<=10 or ball.bottom>=screenheight-10:
        #pygame.mixer.Sound.play(pongsound)
        ballspeedy*=-1
    if ball.left<=10:
        #pygame.mixer.Sound.play(scoresound)
        player2score+=1 
        if player2score==winscore:
            win2time=pygame.time.get_ticks()#return present time in milliseconds
        scoretime=pygame.time.get_ticks()
        
    if ball.right>=screenwidth-10:
        #pygame.mixer.Sound.play(scoresound)
        player1score+=1  
        if player1score==winscore:
            win1time=pygame.time.get_ticks()  
        scoretime=pygame.time.get_ticks()
        
    #collide with player
    if ball.colliderect(player2) and ballspeedx>0:
        #pygame.mixer.Sound.play(pongsound)
        if abs(ball.right-player2.left)<10:
            ballspeedx*=-1          
        elif abs(ball.bottom-player2.top)<10 and ballspeedy>0:
            ballspeedy*=-1
        elif abs(ball.top-player2.bottom)<10 and ballspeedy<0:
            ballspeedy*=-1    
    if ball.colliderect(player1) and ballspeedx<0: 
       #pygame.mixer.Sound.play(pongsound)
        if abs(ball.left-player1.right)<10:
            ballspeedx*=-1          
        elif abs(ball.bottom-player1.top)<10 and ballspeedy>0:
            ballspeedy*=-1
        elif abs(ball.top-player1.bottom)<10 and ballspeedy<0:
            ballspeedy*=-1           
             
#ball regeneration
def ballstart():
    global ballspeedx,ballspeedy,scoretime
    currenttime=pygame.time.get_ticks()
    ball.center = (screenwidth/2, screenheight/2)
    if currenttime-scoretime<3000:
        ballspeedx,ballspeedy=0,0
        timetext=timefont.render(f"{math.floor(4-((currenttime-scoretime)/1000))}",False,timecolor)
        screen.blit(timetext,(screenwidth-30,20))
    else:
        ballspeedy=ballspeed*random.choice((1,-1)) # this is done to move the ball after colliding with side walls
        ballspeedx=ballspeed*random.choice((1,-1))
        scoretime=None    

#display win message
def display1win():
    global win1time,ballspeedx,ballspeedy
    ball.center = (screenwidth/2, screenheight/2)
    close1time=pygame.time.get_ticks()
    if close1time-win1time<2000:
        ballspeedx,ballspeedy=0,0
        win1text=winfont.render("!! Player1 wins !!",False,wincolor)   
        screen.blit(win1text,(screenwidth/2-360,screenheight/2+100))
    else:
        #pygame.quit()
        #sys.quit()
        #os.system("python jkpingpong.py") 
        messagebox.showinfo("Message","THANK YOU FOR PLAYING")
        pygame.quit()   
      
def display2win():
    global win2time,ballspeedx,ballspeedy
    ball.center = (screenwidth/2, screenheight/2)
    close2time=pygame.time.get_ticks()
    if close2time-win2time<2000:
        ballspeedx,ballspeedy=0,0
        win2text=winfont.render("!! Player2 wins !!",False,wincolor)   
        screen.blit(win2text,(screenwidth/2+20,screenheight/2+100))
    else:
        #pygame.quit()
        #sys.quit() 
        #os.system("python jkpingpong.py") 
        messagebox.showinfo("Message","THANK YOU FOR PLAYING")
        pygame.quit()           

pygame.mixer.pre_init(44100,-16,2,512)

pygame.init()

clock=pygame.time.Clock()

#creating new window
screenwidth=1200
screenheight=700
screen=pygame.display.set_mode((screenwidth,screenheight)) 

#name for window
name=pygame.display.set_caption("Ping Pong Game")

#icon for game
icon=pygame.image.load("image.jpg")
pygame.display.set_icon(icon)

#colours
bgcolor=(144,238,144)
ballcolor=(255,165,0)
player1color=(255,0,0)
player2color=(0,0,0)
linecolor=(0,0,0)
scorecolor=(0,96,255)
timecolor=(255,0,255)
welcomecolor=(255,0,0)
wincolor=(255,0,127)
aimcolor=(81,4,0)

#creating shapes
ball=pygame.Rect(screenwidth/2-10,screenheight/2-10,20,20)
player1=pygame.Rect(10, screenheight / 2 - 70,10,120)
player2=pygame.Rect(screenwidth - 20, screenheight / 2 - 70,10,120) 

#speed 
ballspeed=6
ballspeedx=ballspeed * random.choice((1,-1))#this is done so that ball will move in random direction after colliding with side walls
ballspeedy=ballspeed * random.choice((1,-1))
player1speed=0
player2speed=0
speed=4

#score details
player1score=0
player2score=0
scorefont=pygame.font.SysFont("castellar",20)

#score time
scoretime=True
timefont=pygame.font.SysFont("algerian",32)

#welcome
welcomefont=pygame.font.SysFont("algerian",32)

#win
win1time=None
win2time=None
winfont=pygame.font.SysFont("script",50)
winscore=5

#aim
aimfont=pygame.font.SysFont("algerian",25)

#sound
#pongsound=pygame.mixer.Sound("pong.ogg")
#wscoresound=pygame.mixer.Sound("score.ogg")


#run the window
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #pygame.quit()
            #sys.quit()
            #os.system("python jkpingpong.py") 
            messagebox.showinfo("Message","THANK YOU FOR PLAYING")
            pygame.quit()    
        
        #configuring buttons
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                player1speed+=speed
            if event.key==pygame.K_w:
                player1speed-=speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_s:
                player1speed-=speed
            if event.key==pygame.K_w:
                player1speed+=speed 
                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player2speed+=speed
            if event.key==pygame.K_UP:
                player2speed-=speed 
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player2speed-=speed
            if event.key==pygame.K_UP:
                player2speed+=speed    
    
    player1.y+=player1speed
    player2.y+=player2speed
    
    ballanimation()
    
    playeranimation()
    
    #drawing objects and Lines        
    screen.fill(bgcolor)        
    pygame.draw.rect(screen,player1color,player1)
    pygame.draw.rect(screen,player2color,player2)
    pygame.draw.line(screen,linecolor,[10,10],[screenwidth-10,10])
    pygame.draw.line(screen,linecolor,[10,10],[10,screenheight-10])
    pygame.draw.line(screen,linecolor,[10,screenheight-10],[screenwidth-10,screenheight-10])
    pygame.draw.line(screen,linecolor,[screenwidth-10,10],[screenwidth-10,screenheight-10])
    pygame.draw.line(screen,linecolor,[screenwidth/2,10],[screenwidth/2,screenheight-10])
    
    #displays welcome message
    #welcometext=welcomefont.render("Welcome to my ping pong game",False,welcomecolor)   
    #screen.blit(welcometext,(screenwidth/2-250,20))
    
    #aimtext=aimfont.render(f"First to score {winscore} point wins",False,aimcolor)
    #screen.blit(aimtext,(screenwidth/2-175,screenheight-50))
    
    #displaying scores   
    player1text=scorefont.render(f"{player1score}",False,scorecolor)   
    screen.blit(player1text,(screenwidth/2-32,screenheight/2))
    player2text=scorefont.render(f"{player2score}",False,scorecolor)   
    screen.blit(player2text,(screenwidth/2+20,screenheight/2))
    playername1text=scorefont.render("Player 1",False,scorecolor)   
    screen.blit(playername1text,(screenwidth/2-115,screenheight/2-20))
    playername2text=scorefont.render("Player 2",False,scorecolor)   
    screen.blit(playername2text,(screenwidth/2+20,screenheight/2-20))
    
    pygame.draw.ellipse(screen,ballcolor,ball) 
           
    if win1time:
        display1win()
    if win2time:
        display2win()
    
    if scoretime:
        ballstart()
                   
    #updating window       
    pygame.display.flip() 
    clock.tick(144)            