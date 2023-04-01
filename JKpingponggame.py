from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pygame,random,math,time

def p2():
    global player1score,player2score,ballspeedx,ballspeedy,scoretime,win2time,win1time,winscore
    
    def playeranimation():
        if player1.top<=10:
            player1.top=10
        if player1.bottom>=screenheight-10:
            player1.bottom=screenheight-10
        if player2.top<=10:
            player2.top=10
        if player2.bottom>=screenheight-10:
            player2.bottom=screenheight-10

    def ballanimation():
        global ballspeedx,ballspeedy,scoretime,win1time,win2time,player1score,player2score
        
        ball.x+=ballspeedx
        ball.y+=ballspeedy   
        
        if ball.top<=10 or ball.bottom>=screenheight-10:
            ballspeedy*=-1
            pygame.mixer.Sound.play(pongsound)
        if ball.left<=10:
            pygame.mixer.Sound.play(scoresound)
            player2score+=1 
            if player2score==winscore:
                win2time=pygame.time.get_ticks()
            scoretime=pygame.time.get_ticks()
            
        if ball.right>=screenwidth-10:
            pygame.mixer.Sound.play(scoresound)
            player1score+=1  
            if player1score==winscore:
                win1time=pygame.time.get_ticks()  
            scoretime=pygame.time.get_ticks()
            
        if ball.colliderect(player2) and ballspeedx>0:
            pygame.mixer.Sound.play(pongsound)
            if abs(ball.right-player2.left)<10:
                ballspeedx*=-1          
            elif abs(ball.bottom-player2.top)<10 and ballspeedy>0:
                ballspeedy*=-1
            elif abs(ball.top-player2.bottom)<10 and ballspeedy<0:
                ballspeedy*=-1    
        if ball.colliderect(player1) and ballspeedx<0: 
            pygame.mixer.Sound.play(pongsound)
            if abs(ball.left-player1.right)<10:
                ballspeedx*=-1          
            elif abs(ball.bottom-player1.top)<10 and ballspeedy>0:
                ballspeedy*=-1
            elif abs(ball.top-player1.bottom)<10 and ballspeedy<0:
                ballspeedy*=-1           
                
    def ballstart():
        global ballspeedx,ballspeedy,scoretime
        currenttime=pygame.time.get_ticks()
        ball.center = (screenwidth/2, screenheight/2)
        if currenttime-scoretime<3000:
            ballspeedx,ballspeedy=0,0
            timetext=timefont.render(f"{math.floor(4-((currenttime-scoretime)/1000))}",False,timecolor)
            screen.blit(timetext,(screenwidth-30,20))
        else:
            ballspeedy=ballspeed*random.choice((1,-1))
            ballspeedx=ballspeed*random.choice((1,-1))
            scoretime=None    

    def display1win():
        global win1time,ballspeedx,ballspeedy
        ball.center = (screenwidth/2, screenheight/2)
        close1time=pygame.time.get_ticks()
        if close1time-win1time<2000:
            ballspeedx,ballspeedy=0,0
            win1text=winfont.render("!! Player1 wins !!",False,wincolor)
            screen.blit(win1text,(screenwidth/2-360,screenheight/2+100))
        else:
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
            pygame.quit()           

    pygame.mixer.pre_init(44100,-16,2,512)

    pygame.init()

    clock=pygame.time.Clock()

    screenwidth=1200
    screenheight=700
    screen=pygame.display.set_mode((screenwidth,screenheight)) 

    name=pygame.display.set_caption("Ping Pong Game")

    icon=pygame.image.load("image.jpg")
    pygame.display.set_icon(icon)

    bgcolor=(144,238,144)
    ballcolor=(255,165,0)
    player1color=(255,0,0)
    player2color=(0,0,0)
    linecolor=(0,0,0)
    scorecolor=(0,96,255)
    timecolor=(255,0,255)
    wincolor=(255,0,127)
    
    scoresound=pygame.mixer.Sound("score.wav")
    pongsound=pygame.mixer.Sound("pong.wav")

    ball=pygame.Rect(screenwidth/2-10,screenheight/2-10,20,20)
    player1=pygame.Rect(10, screenheight / 2 - 70,10,120)
    player2=pygame.Rect(screenwidth - 20, screenheight / 2 - 70,10,120) 

    ballspeed=6
    ballspeedx=ballspeed * random.choice((1,-1))
    ballspeedy=ballspeed * random.choice((1,-1))
    player1speed=0
    player2speed=0
    speed=4

    player1score=0
    player2score=0
    scorefont=pygame.font.SysFont("castellar",20)

    scoretime=True
    timefont=pygame.font.SysFont("algerian",32)

    win1time=None
    win2time=None
    winfont=pygame.font.SysFont("script",50)
    winscore=5
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()    
            
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
               
        screen.fill(bgcolor)        
        pygame.draw.rect(screen,player1color,player1)
        pygame.draw.rect(screen,player2color,player2)
        pygame.draw.line(screen,linecolor,[10,10],[screenwidth-10,10])
        pygame.draw.line(screen,linecolor,[10,10],[10,screenheight-10])
        pygame.draw.line(screen,linecolor,[10,screenheight-10],[screenwidth-10,screenheight-10])
        pygame.draw.line(screen,linecolor,[screenwidth-10,10],[screenwidth-10,screenheight-10])
        pygame.draw.line(screen,linecolor,[screenwidth/2,10],[screenwidth/2,screenheight-10])
          
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
                          
        pygame.display.flip() 
        clock.tick(144)

def cpu():
    global ballspeedx,ballspeedy,scoretime,player1score,player2score,win2time,win1time,winscore
    def playeranimation():
        if player1.top<=10:
            player1.top=10
        if player1.bottom>=screenheight-10:
            player1.bottom=screenheight-10
    
    def aianimation():
        if player2.top<ball.y:
            player2.top+=speed
        if player2.bottom>ball.y:
            player2.bottom-=speed
        if player2.top<=10:
            player2.top=10
        if player2.bottom>=screenheight-10:                
            player2.bottom=screenheight-10        

    def ballanimation():
        global ballspeedx,ballspeedy,player1score,player2score,scoretime,win1time,win2time
        
        ball.x+=ballspeedx
        ball.y+=ballspeedy   
        
        if ball.top<=10 or ball.bottom>=screenheight-10:
            pygame.mixer.Sound.play(pongsound)
            ballspeedy*=-1
        if ball.left<=10:
            pygame.mixer.Sound.play(scoresound)
            player2score+=1 
            if player2score==winscore:
                win2time=pygame.time.get_ticks()
            scoretime=pygame.time.get_ticks()
            
        if ball.right>=screenwidth-10:
            pygame.mixer.Sound.play(scoresound)
            player1score+=1  
            if player1score==winscore:
                win1time=pygame.time.get_ticks()  
            scoretime=pygame.time.get_ticks()
            
        if ball.colliderect(player2) and ballspeedx>0:
            pygame.mixer.Sound.play(pongsound)
            if abs(ball.right-player2.left)<10:
                ballspeedx*=-1          
            elif abs(ball.bottom-player2.top)<10 and ballspeedy>0:
                ballspeedy*=-1
            elif abs(ball.top-player2.bottom)<10 and ballspeedy<0:
                ballspeedy*=-1    
        if ball.colliderect(player1) and ballspeedx<0: 
            pygame.mixer.Sound.play(pongsound)
            if abs(ball.left-player1.right)<10:
                ballspeedx*=-1          
            elif abs(ball.bottom-player1.top)<10 and ballspeedy>0:
                ballspeedy*=-1
            elif abs(ball.top-player1.bottom)<10 and ballspeedy<0:
                ballspeedy*=-1           
                
    def ballstart():
        global ballspeedx,ballspeedy,scoretime
        currenttime=pygame.time.get_ticks()
        ball.center = (screenwidth/2, screenheight/2)
        if currenttime-scoretime<3000:
            ballspeedx,ballspeedy=0,0
            timetext=timefont.render(f"{math.floor(4-((currenttime-scoretime)/1000))}",False,timecolor)
            screen.blit(timetext,(screenwidth-30,20))
        else:
            ballspeedy=ballspeed*random.choice((1,-1))
            ballspeedx=ballspeed*random.choice((1,-1))
            scoretime=None    

    def display1win():
        global win1time,ballspeedx,ballspeedy
        ball.center = (screenwidth/2, screenheight/2)
        close1time=pygame.time.get_ticks()
        if close1time-win1time<2000:
            ballspeedx,ballspeedy=0,0
            win1text=winfont.render("!! Player1 wins !!",False,wincolor)   
            screen.blit(win1text,(screenwidth/2-360,screenheight/2+100))
        else:
            pygame.quit()   
            
        
    def display2win():
        global win2time,ballspeedx,ballspeedy
        ball.center = (screenwidth/2, screenheight/2)
        close2time=pygame.time.get_ticks()
        if close2time-win2time<2000:
            ballspeedx,ballspeedy=0,0
            win2text=winfont.render("!! CPU wins !!",False,wincolor)   
            screen.blit(win2text,(screenwidth/2+20,screenheight/2+100))
        else:
            pygame.quit()   

    pygame.mixer.pre_init(44100,-16,2,512)

    pygame.init()

    clock=pygame.time.Clock()

    screenwidth=1200
    screenheight=700
    screen=pygame.display.set_mode((screenwidth,screenheight)) 

    name=pygame.display.set_caption("Ping Pong Game")

    icon=pygame.image.load("image.jpg")
    pygame.display.set_icon(icon)

    bgcolor=(144,238,144)
    ballcolor=(255,165,0)
    player1color=(255,0,0)
    player2color=(0,0,0)
    linecolor=(0,0,0)
    scorecolor=(0,96,255)
    timecolor=(255,0,255)
    wincolor=(255,0,127)
    
    scoresound=pygame.mixer.Sound("score.wav")
    pongsound=pygame.mixer.Sound("pong.wav")

    ball=pygame.Rect(screenwidth/2-10,screenheight/2-10,20,20)
    player1=pygame.Rect(10, screenheight / 2 - 70,10,120)
    player2=pygame.Rect(screenwidth - 20, screenheight / 2 - 70,10,120) 

    ballspeed=5
    ballspeedx=ballspeed * random.choice((1,-1))
    ballspeedy=ballspeed * random.choice((1,-1))
    player1speed=0
    player2speed=0
    speed=5

    player1score=0
    player2score=0
    scorefont=pygame.font.SysFont("castellar",20)

    scoretime=True
    timefont=pygame.font.SysFont("algerian",32)

    win1time=None
    win2time=None
    winfont=pygame.font.SysFont("script",50)
    winscore=5
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()  
            
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
        
        player1.y+=player1speed
        player2.y+=player2speed
        
        ballanimation()
        
        playeranimation()
        
        aianimation()
                
        screen.fill(bgcolor)        
        pygame.draw.rect(screen,player1color,player1)
        pygame.draw.rect(screen,player2color,player2)
        pygame.draw.line(screen,linecolor,[10,10],[screenwidth-10,10])
        pygame.draw.line(screen,linecolor,[10,10],[10,screenheight-10])
        pygame.draw.line(screen,linecolor,[10,screenheight-10],[screenwidth-10,screenheight-10])
        pygame.draw.line(screen,linecolor,[screenwidth-10,10],[screenwidth-10,screenheight-10])
        pygame.draw.line(screen,linecolor,[screenwidth/2,10],[screenwidth/2,screenheight-10])
         
        player1text=scorefont.render(f"{player1score}",False,scorecolor)   
        screen.blit(player1text,(screenwidth/2-32,screenheight/2))
        player2text=scorefont.render(f"{player2score}",False,scorecolor)   
        screen.blit(player2text,(screenwidth/2+20,screenheight/2))
        playername1text=scorefont.render("Player 1",False,scorecolor)   
        screen.blit(playername1text,(screenwidth/2-115,screenheight/2-20))
        playername2text=scorefont.render("CPU",False,scorecolor)   
        screen.blit(playername2text,(screenwidth/2+20,screenheight/2-20))
        
        pygame.draw.ellipse(screen,ballcolor,ball) 
            
        if win1time:
            display1win()
        if win2time:
            display2win()
        
        if scoretime:
            ballstart()
                          
        pygame.display.flip() 
        clock.tick(144)            

root=Tk()

pygame.init()

r=IntVar()
r.set("1")

def startgame(number):
    if number==1:
        cpu()
    if number==2:
        p2()       
 
def quitgame():
    messagebox.showinfo("Message","THANK YOU FOR PLAYING")
    root.destroy()  
    
def control():
    messagebox.showinfo("CONTROLS","MOVEMENT\nCPU -- W,S\n2 PLAYERS -- W,S/UPARROW,DOWNARROW\n4 PLAYERS -- W,S/UPARROW,DOWNARROW/O,P/N,M")      

root.title("JK PING PONG")

root.attributes("-fullscreen",True)

root.configure(bg="black")

image1=PhotoImage(file="tkimage.png")
root.iconphoto(False,image1)

label1=Label(root,text="JK PING PONG",font=("algerian",50),fg="red",bg="black").pack()

img=ImageTk.PhotoImage(Image.open("imagenew2.jpg"))
imagelabel=Label(root,image=img)
imagelabel.pack()

label2=Label(root,text="\n\n\tABOUT THE GAME :-",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label3=Label(root,text="\t-> THIS IS A BASIC PING PONG GAME",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label5=Label(root,text="\t-> FIRST PLAYER TO SCORE 5 POINTS WINS",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")
label6=Label(root,text="\t-> A RELAX TIME OF 3 SECONDS WILL BE GIVEN AT THE START AND ALSO AFTER EACH POINT\n",font=("algerian",20),bg="black",fg="orange").pack(anchor="w")

label10=Label(root,text="SELECT MODE : ",font=("algerian",20),bg="black",fg="orange").pack()

Radiobutton(root,text="CPU",variable=r,value=1,bg="yellow",width=10).pack()
Radiobutton(root,text="2 PLAYERS",variable=r,value=2,bg="yellow",width=10).pack()
label7=Label(root,text="\n",bg="black").pack()

button1=Button(root,text="\nCONTROLS\n",command=control,bg="lightgreen",width=20).pack()
label8=Label(root,text="\n",bg="black").pack()
button2=Button(root,text="\nSTART THE GAME\n",bg="lightgreen",command=lambda:startgame(r.get()),width=20).pack()
label9=Label(root,text="\n",bg="black").pack()
button3=Button(root,text="\nQUIT GAME\n",bg="lightgreen",command=quitgame,width=20).pack()

root.mainloop()