#PaintProjectSavio.py
from pygame import *
from math import *
from tkinter import *
from tkinter import filedialog
root=Tk()
root.withdraw() #allows font,file, math, and pygame
font.init()
init()
####colours and screen
title=display.set_caption("Chess Paint")

width,height=1100,700
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)   #creates screen and colours
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
r=0
b=0
g=0
col=(r,g,b)


#####Background
screen.fill(WHITE)
chbrd = image.load("pics/bkgnds.jpg").convert_alpha()

bkgnd=transform.scale(chbrd,(1100,700)) #creates background
screen.blit(bkgnd,(0,0))
fontSize=60
raleway=font.SysFont("Raleway",fontSize) #makes title
chess=raleway.render("Chess",True,WHITE)
paint=raleway.render("Paint",True,WHITE)
screen.blit(chess,(220,35))
screen.blit(paint,(360,35))


##########Stamps
down=False
left=True #sets bool variables so that they can be used later
right=False
stamp=""
stampLis=["pics/king.png", "pics/queen.png", "pics/knight.png", "pics/rook.png", "pics/pawn.png",
 "pics/bking.png", "pics/bqueen.png", "pics/bknight.png", "pics/brook.png", "pics/bpawn.png"]

stamps=[]
for s in stampLis:
    lStamp=image.load(s).convert()
    tStamp=transform.scale(lStamp,(50,50))
    stamps.append(tStamp)  #loads and transforms stamps

##Stamp rect
dropArrow=image.load("pics/dropArrowStamp.png").convert_alpha()
tDropArrow=transform.scale(dropArrow,(20,20)) #loads down arrow
upArrow=transform.flip(tDropArrow,False,True) #flips down arrow so I don't have  to load anything else
stampRect=Rect(45,370,125,35)
dropRect=Rect(140,370,30,35)
draw.rect(screen,BLACK,stampRect)
draw.rect(screen,GREEN,stampRect,2) #draws the design
draw.rect(screen,BLACK,dropRect)
screen.blit(tDropArrow,(145,377))
draw.rect(screen,GREEN,dropRect,2)

##Stamp title
fontSize=35
raleway=font.SysFont("Raleway",fontSize) #makes stamp title
stampTitle=raleway.render("Sta",True,WHITE)
stampMp=raleway.render("mps",True,WHITE)
screen.blit(stampTitle,(53,375))
screen.blit(stampMp,(90,375))

normCap=screen.subsurface(stampRect).copy() #takes screnshot of the stamp title and arrow so that later, the up and down arrow don't overlap
downRect=Rect(15,405,155,200)
downScreenCap=screen.subsurface(downRect).copy() #takes screenshot of normal background behind downRect

rightRect=Rect(135,570,30,30)
leftRect=Rect(20,570,30,30)
rightPic=image.load("pics/right.png").convert_alpha()
leftPic=image.load("pics/left.png").convert_alpha()   #loads and transforms left and right pic for the pages in stamps
tRightPic=transform.scale(rightPic,(30,30))
tLeftPic=transform.scale(leftPic,(30,30))


kingRect=Rect(30,415,50,50)
queenRect=Rect(105,415,50,50)
knightRect=Rect(30,475,50,50)
rookRect=Rect(105,475,50,50)
pawnRect=Rect(67,540,50,50)


##canvas
canvasRect=Rect(200,90,750,450)
draw.rect(screen,WHITE,canvasRect) #draws canvas


##File/Redo/Undo
screenCap1st=screen.subsurface(canvasRect).copy()
undo=[screenCap1st] #allows undo to have a sreen shot of original screen
redo=[]
saveRect=Rect(0,0,40,40)
loadRect=Rect(45,0,40,40)
undoRect=Rect(90,0,40,40)
redoRect=Rect(135,0,40,40)
clearRect=Rect(175,0,40,40)

fileList=["pics/save.png","pics/load.png","pics/undo.png","pics/redo.png","pics/clear.png"]
fileRects=[saveRect,loadRect,undoRect,redoRect,clearRect]
files=[]
for f in fileList:
    fileEdit=image.load(f).convert_alpha()
    tfileEdit=transform.scale(fileEdit,(40,40))
    files.append(tfileEdit) #this way loaded and transform pictures are saved somewhere
for i in range(5): #draws background
    draw.rect(screen,WHITE,fileRects[i])
for i in range(5): #draws icon
    screen.blit(files[i],fileRects[i])
for i in range(5): #draws outline
    draw.rect(screen,BLUE,fileRects[i],2)
    
  




##Pixel
pixelRect=Rect(960,250,140,90)
draw.rect(screen,GREEN,pixelRect,2)
pixelCap=screen.subsurface(pixelRect).copy() #allows me to get the normal background behind pixelRect

##RGB slider
redRect=Rect(650,550,275,30)
draw.rect(screen,RED,redRect) #draws rect for red,green,blue so that it shows up when screen first opened
draw.rect(screen,WHITE,(650,550,20,30))
blueRect=Rect(650,590,275,30)
draw.rect(screen,BLUE,blueRect)    
draw.rect(screen,WHITE,(650,590,20,30))
greenRect=Rect(650,630,275,30)
draw.rect(screen,GREEN,greenRect)
draw.rect(screen,WHITE,(650,630,20,30))
colourRect=Rect(1000,580,60,60)

##Tools
tool=""
pencilRect=Rect(30,90,60,60)
eraserRect=Rect(120,90,60,60)
brushRect=Rect(30,160,60,60)
ovalRect=Rect(120,160,60,60)
rectRect=Rect(30,230,60,60)
lineRect=Rect(120,230,60,60)
fillRect=Rect(30,300,60,60)
unfillRect=Rect(120,300,60,60)
toolRect=[pencilRect,eraserRect,brushRect,ovalRect,rectRect,lineRect,
          fillRect,unfillRect]
toolList=["pics/pencil.png","pics/eraser.png","pics/brush.png","pics/oval.png","pics/rect.jpg","pics/line.png","pics/fill.png","pics/unfill.png"]
tools=[]
for t in toolList:
    tool=image.load(t).convert_alpha()
    tTool=transform.scale(tool,(60,60))
    tools.append(tTool) #this way loaded and transform pictures are saved somewhere
for i in range(8): #draws backgrounds
    draw.rect(screen,WHITE,toolRect[i])
for i in range(8): #draws icons
    screen.blit(tools[i],toolRect[i])
##Music player
p=0
musState=""
pause=False
popSongs=[]
musics=[]
musicRect=Rect(200,545,440,150)
playRect=Rect(360,630,50,50)
pauseRect=Rect(420,630,50,50)
nextRect=Rect(475,630,41,43)
songRect=Rect(235,575,365,30)
songs=["pics/Erik Satie - Jazzopedie","pics/Joplin - The Entertainer",
    "pics/Beethoven - Fur Elise","pics/Chopin - Nocturne",
       "pics/Beethoven-Turkish March"]
musicList=["pics/play.png","pics/pauses.png","pics/nextt.png"]
musicRect=[playRect,pauseRect,nextRect]
for m in musicList:
    music=image.load(m).convert_alpha()
    if m=="nextt.png":
        tMusic=transform.scale(music,(40,40)) #since nexttRect is smaller I have to do this
    else:
        tMusic=transform.scale(music,(50,50))
    musics.append(tMusic)


##Thickness slider
thick=1 #initalzing vairables
fillThick=1
thickRect=Rect(750,25,320,50)
draw.rect(screen,BLACK,thickRect) #drawing it before event loop so that user sees it when screen first opened
draw.rect(screen,RED,(750,25,20,50))




running=True
while running:
    mx,my=mouse.get_pos()#getting the current mx and my
    mb=mouse.get_pressed()

    ##Pixel bliting
    fontSize=60
    raleway=font.SysFont("Raleway",fontSize) #creates pixel location
    if my-90>0 and mx-200>0 and mx<951 and my<541: #check if mouse is inside 
        x=raleway.render(("X "+str(mx-200)),True,WHITE) #-200 and -90 to get 0,0 to be the top-right corner of canvas
        y=raleway.render(("Y "+str(my-90)),True,WHITE)
        screen.blit(pixelCap,(960,250)) #makes sure previous coordinates don't overlap with current ones
        screen.blit(x,(960,250))
        screen.blit(y,(960,300))

    ########Event Loop
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy=evt.pos
        if evt.type==MOUSEBUTTONUP:
            if musState=="next": #changes the pos in songs
                if p<4:
                    p+=1
                else: #resets playlist if last song is played
                    p=0
            screenCap=screen.subsurface(canvasRect).copy()
            screen.set_clip(canvasRect)
            if tool=="pencil":
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="eraser":
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="line":
                screen.blit(screenCap,canvasRect)
                draw.line(screen,col,(sx,sy),(mx,my),thick)
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="rect":
                screen.blit(screenCap,canvasRect)
                nRect=Rect(sx,sy,(mx-sx),(my-sy))
                nRect.normalize()
                draw.rect(screen,col,nRect,fillThick)
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="oval":
                screen.blit(screenCap,canvasRect)
                ellRect=Rect(sx,sy,(mx-sx),(my-sy))
                ellRect.normalize()
                draw.ellipse(screen,col,ellRect,fillThick)
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="brush":
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
                
            if tool=="king.png": #can't do a loop because then undo for stamps doesn't work
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[0],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="queen.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[1],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="knight.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[2],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="rook.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[3],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="pawn.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[4],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="bking.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[5],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="bqueen.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[6],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="bknight.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[7],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="brook.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[8],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)
            if tool=="bpawn.png":
                screen.blit(screenCap,canvasRect)
                screen.blit(stamps[9],(mx-12,my-12))
                screenCap=screen.subsurface(canvasRect).copy()
                undo.append(screenCap)


                
            
                

        screen.set_clip(None)

        ##Thickness slider 
        if thickRect.collidepoint(mx,my)and mb[0] and mx<=1050:
           draw.rect(screen,BLACK,thickRect) #makes it so that the final position of the slider is shown
           draw.rect(screen,RED,(mx,25,20,50)) #makes sliders at mouse x pos
           thick=mx//10-70
           fillThick=mx//10-70 #does fillThick as well so rect and oval thickness can change
           
        ##Save
        if mb[0] and saveRect.collidepoint(mx,my):
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            if fname: #checks if they entered anything
                image.save(screen.subsurface(canvasRect),fname)
                
        ##Load         
        if mb[0] and loadRect.collidepoint(mx,my):
            tool="load"
            fname=filedialog.askopenfilename()
            if fname: #checks if the user entered a file name
                fileName=image.load(fname)
                w=fileName.get_width()
                h=fileName.get_width()
                if w>750 or h>450: #if too big resize
                    canvasPic=transform.scale(fileName,(750,450))
                    screen.blit(canvasPic,(200,90))
                else:
                    screen.blit(fileName,(200,90)) #if not just blit at corner for canvas
                
        ##Undo       
        if undoRect.collidepoint(mx,my) and mb[0]: 
            if len(undo)>1:
                undoTemp=undo.pop() #last item in undolist is screenshot before current screen
                redo.append(undoTemp) #appends that to redo
                screen.blit(undo[-1],canvasRect) #blits the screenshot that came directly before the current screen

        ##Redo
        if redoRect.collidepoint(mx,my)and mb[0]: 
            if len(redo)>=1:
                screen.blit(redo[-1],canvasRect) #blits the most current undo screen
                redoTemp=redo.pop() #gets rid of it so that it doesn't blit it again
                undo.append(redoTemp) #gives it to undo this way you can undo a redo
                
        if len(redo)>=1 and canvasRect.collidepoint(mx,my) and mb[0]: #makes it so that if they draw something new, it creates a new redo 'path'
            redo=[]

        ##RGB sliders       
        if redRect.collidepoint(mx,my)and mb[0] and mx<=905: #checks if mx went beyond the slider 
           draw.rect(screen,RED,redRect) #draws over the slider so that only the final version shows
           draw.rect(screen,WHITE,(mx,550,20,30)) #draws rect at mouse x pos
           r=mx-650 #sets red value
        if blueRect.collidepoint(mx,my) and mb[0] and mx<=905:
           draw.rect(screen,BLUE,blueRect)
           draw.rect(screen,WHITE,(mx,590,20,30))
           b=mx-650 #sets blue value
        if greenRect.collidepoint(mx,my) and mb[0] and mx<=905:
           draw.rect(screen,GREEN,greenRect)
           draw.rect(screen,WHITE,(mx,630,20,30))
           g=mx-650 #sets green value
        col=(r,g,b) #creates the colour based on the rgb values
      
        ##Music Player
        if playRect.collidepoint and mb[0] and musState=="play": #if play clicked then it will play a song or unpause
            if pause:#if currently paused then unpaus
                mixer.music.unpause()
                pause=False #since not paused, it should be false
                
            else: #if not paused then means that user wants a song to start
                mixer.music.load(songs[p]+".ogg")
                mixer.music.play()
            
                
        if musState=="pause":#if pause was clicked then pause 
            mixer.music.pause()
            pause=True #since paused then it should be true
            
        fontSize=25 
        raleway=font.SysFont("Raleway",fontSize) #font 
        
        
        musicName=raleway.render(songs[p],True,BLACK) #allows the song name to be displayed
        draw.rect(screen,BLACK,(200,545,440,150))#draws black background for entire player (its coordinates not musicRect because putting musicRect gave me an error)
        draw.rect(screen,GREEN,(200,545,440,150),2)# draws outline for design
        draw.rect(screen,GREEN,(200,545,440,150),2) #draws outline for design
        draw.rect(screen,WHITE,songRect) #draws white background for song name
        draw.rect(screen,GREEN,songRect,2) #draws outline for design
        
        draw.rect(screen,WHITE,playRect) #draws background for the play,pause,and next buttons
        draw.rect(screen,WHITE,pauseRect)
        draw.rect(screen,WHITE,nextRect)
        
        screen.blit(musicName,(330,582)) #drawn here so that other drawings down draw over it

        for i in range(3):
            screen.blit(musics[i],musicRect[i])



        
        ##Stamps

        
        if dropRect.collidepoint(mx,my) and mb[0]:
            if down: #if drop-down menu is showing or 'down'
                down=False #if clicked on dropRect and drop-menu down
                #then it means user wants to close menu
            else: #if drop-down menu is not showing
                down=True #conversly, if drop-down menu down and clicked then means open menu
            screen.blit(normCap,(45,370)) #allows arrows to not overlap
            screen.blit(downScreenCap,(15,405)) #blits the regular surface behind downRect so that if down is false
            screen.blit(normCap,(45,370)) #allows arrows to not overlap
        if leftRect.collidepoint(mx,my) and mb[0]:
            left=True #left page shows
            right=False #right page doesn't
        if rightRect.collidepoint(mx,my) and mb[0]:
            left=False #left page doesn't show
            right=True #right page shows
                
               
        if down: #if True, creates the drop-down menu, if False, it doesn't and normal screen shows because of earlier code
                draw.rect(screen,BLACK,downRect) #drop-down menu background
                draw.rect(screen,BLACK,downRect) #drop-down menu background
                screen.blit(upArrow,(145,375)) #arrow up indicating to user that if arrow clicked then menu will close or go 'up' 
                draw.rect(screen,GREEN,dropRect,2) #outline for design
                draw.rect(screen,WHITE,rightRect)
                draw.rect(screen,WHITE,leftRect)
                draw.rect(screen,GREEN,rightRect,2)
                draw.rect(screen,GREEN,leftRect,2)
                screen.blit(tRightPic,rightRect)
                screen.blit(tLeftPic,leftRect)
                if left: #if clicked on left button, show first page
                    screen.blit(stamps[0],(30,415))
                    screen.blit(stamps[1],(105,415))
                    screen.blit(stamps[2],(30,475))
                    screen.blit(stamps[3],(105,475))
                    screen.blit(stamps[4],(67,540))
                if right: #if clicked on right button, show second page
                    screen.blit(stamps[5],(30,415))
                    screen.blit(stamps[6],(105,415))
                    screen.blit(stamps[7],(30,475))
                    screen.blit(stamps[8],(105,475))
                    screen.blit(stamps[9],(67,540))
                
                draw.rect(screen,GREEN,kingRect,2)
                draw.rect(screen,GREEN,queenRect,2)
                draw.rect(screen,GREEN,knightRect,2)
                draw.rect(screen,GREEN,rookRect,2)
                draw.rect(screen,GREEN,pawnRect,2)
       
            

                       

    #drawing all buttons and sliders
        
        
    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,ovalRect,2)
    draw.rect(screen,GREEN,rectRect,2)
    draw.rect(screen,GREEN,lineRect,2)
    draw.rect(screen,GREEN,brushRect,2)

    draw.rect(screen,GREEN,thickRect,2)

    draw.rect(screen,GREEN,(200,545,440,150),2) #was giving error if I put musicRect so I just put coordinates
    draw.rect(screen,GREEN,playRect,2)
    draw.rect(screen,GREEN,pauseRect,2)
    draw.rect(screen,GREEN,nextRect,2)
    
    draw.rect(screen,BLUE,saveRect,2)
    draw.rect(screen,BLUE,loadRect,2)
    draw.rect(screen,BLUE,redoRect,2)
    draw.rect(screen,BLUE,undoRect,2)
    draw.rect(screen,BLUE,clearRect,2)
    
    draw.rect(screen,GREEN,fillRect,2)
    draw.rect(screen,GREEN,unfillRect,2)
    

    draw.rect(screen,BLACK,redRect,2)
    draw.rect(screen,BLACK,blueRect,2)
    draw.rect(screen,BLACK,greenRect,2)
    
    draw.rect(screen,col,colourRect)

    
    

    #selecting the tools and stamps and the music state
    if mb[0]:
        if pencilRect.collidepoint(mx,my):
           tool="pencil"
        if eraserRect.collidepoint(mx,my):
           tool="eraser"
        if ovalRect.collidepoint(mx,my):
           tool="oval"
        if rectRect.collidepoint(mx,my):
           tool="rect"
        if lineRect.collidepoint(mx,my):
           tool="line"
        if brushRect.collidepoint(mx,my):
           tool="brush"
        if loadRect.collidepoint(mx,my):
            tool="load"

        if saveRect.collidepoint(mx,my):
            tool="save"
        if undoRect.collidepoint(mx,my):
            tool="undo"
        if redoRect.collidepoint(mx,my):
            tool="redo"
            
        if fillRect.collidepoint(mx,my):
            tool="fill"
            fillThick=0  #sets fillThick to zero because rect and oval should be filled
        if unfillRect.collidepoint(mx,my):
            tool="unfill"
            fillThick=thick #sets to the thickness before fill

        if playRect.collidepoint(mx,my): 
            musState="play"
        if pauseRect.collidepoint(mx,my):
            musState="pause"
        if nextRect.collidepoint(mx,my):
            musState="next"
            
       
        if kingRect.collidepoint(mx,my):
            if left:
                tool="king.png"
            if right:
                tool="bking.png"
        if queenRect.collidepoint(mx,my):
            if left:
                tool="queen.png"
            if right:
                tool="bqueen.png"
        if knightRect.collidepoint(mx,my):
            if left:
                tool="knight.png"
            if right:
                tool="bknight.png"
        if rookRect.collidepoint(mx,my):
            if left:
                tool="rook.png"    #if it is left page then its the white piece
            if right:           
                tool="brook.png"   #conversely, if right page then black piece
        if pawnRect.collidepoint(mx,my):
            if left:
                tool="pawn.png"  
            if right:
                tool="bpawn.png"
        if clearRect.collidepoint(mx,my):
            screen.blit(screenCap1st,canvasRect)
        
       
    
        

    ### If selected, then it highlights tool
    if tool=="pencil": #if tool matchs specific rect then user has clicked so therefore, they selected it
        draw.rect(screen,RED,pencilRect,2)
    if tool=="eraser":
        draw.rect(screen,RED,eraserRect,2)
    if tool=="oval":
        draw.rect(screen,RED,ovalRect,2)
    if tool=="rect":
        draw.rect(screen,RED,rectRect,2)
    if tool=="line":
        draw.rect(screen,RED,lineRect,2)
    if tool=="brush":
        draw.rect(screen,RED,brushRect,2)
    if tool=="redo":
        draw.rect(screen,RED,redoRect,2)
    if tool=="undo":
        draw.rect(screen,RED,undoRect,2)
    if tool=="fill":
        draw.rect(screen,RED,fillRect,2)
    if tool=="unfill":
        draw.rect(screen,RED,unfillRect,2)

            
    ##Allows the hovering effect
    if tool!="pencil" and pencilRect.collidepoint(mx,my): #if its not tool of specific rect and mouse on ret then means user not clicked yet so therefore, they hovering
        draw.rect(screen,RED,pencilRect,2)
    if tool!="eraser" and eraserRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraserRect,2)
    if tool!="oval" and ovalRect.collidepoint(mx,my):
        draw.rect(screen,RED,ovalRect,2)
    if tool!="rect" and rectRect.collidepoint(mx,my):
        draw.rect(screen,RED,rectRect,2)
    if tool!="line" and lineRect.collidepoint(mx,my):
        draw.rect(screen,RED,lineRect,2)
    if tool!="brush" and brushRect.collidepoint(mx,my):
        draw.rect(screen,RED,brushRect,2)
    if tool!="load" and loadRect.collidepoint(mx,my):
        draw.rect(screen,RED,loadRect,2)
    if tool!="save" and saveRect.collidepoint(mx,my) and mx and my: #makes sure saveRect isn't red when program is started with the mouse outside of screen
        draw.rect(screen,RED,saveRect,2)
    if tool!="undo" and undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
    if tool!="redo" and redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
    if tool=="fill" and fillRect.collidepoint(mx,my):
        draw.rect(screen,RED,fillRect,2)
    if tool=="unfill" and unfillRect.collidepoint(mx,my):
        draw.rect(screen,RED,unfillRect,2)
    

    
           
    #use the tool/ stamp
    if canvasRect.collidepoint(mx,my) and mb[0]:
       screen.set_clip(canvasRect)#only the canvas area can be updated
       if tool=="pencil":
          draw.line(screen,col,(oldmx,oldmy),(mx,my),1) #draws line between coords in previous frame
          #to coords in current frame giving it the pencil effect
       if tool=="eraser":
          draw.circle(screen,WHITE,(mx,my),thick) 
        #allows user to see where there drawing the polygon before it finalizes
       if tool=="oval": 
          screen.blit(screenCap,canvasRect) #blits previous screenshot so everything drawn before is on screen
          ellRect=Rect(sx,sy,(mx-sx),(my-sy)) #defines rect
          ellRect.normalize() #takes care of negative values
          draw.ellipse(screen,col,ellRect,fillThick)#draws it using fillThick because different thickness variable needed because of fill and unfill
       if tool=="rect":
           screen.blit(screenCap,canvasRect)
           nRect=Rect(sx,sy,(mx-sx),(my-sy))
           nRect.normalize()
           draw.rect(screen,col,nRect,fillThick)
       if tool=="line":
            screen.blit(screenCap,canvasRect)
            draw.line(screen,col,(sx,sy),(mx,my),thick)
       if tool=="brush":#uses rise and run to make circles in between two circles already drawn
           dx=mx-oldmx
           dy=my-oldmy
           dist=(dx**2+dy**2)**0.5
           for d in range(int(dist)):
               dotX=d*dx/dist+oldmx
               dotY=d*dy/dist+oldmy
               draw.circle(screen,col,(int(dotX),int(dotY)),thick)
       for s in stamps:
            if tool==s:
              screen.blit(screenCap,canvasRect)
              ind=stamps.index(s)
              screen.blit(stamps[ind],(mx-12,my-12))
##       if tool=="king.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[0],(mx-12,my-12))
##       if tool=="queen.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[1],(mx-12,my-12))
##       if tool=="knight.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[2],(mx-12,my-12))
##       if tool=="rook.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[3],(mx-12,my-12))
##       if tool=="pawn.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[4],(mx-12,my-12))
##       if tool=="bking.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[5],(mx-12,my-12))
##       if tool=="bqueen.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[6],(mx-12,my-12))
##       if tool=="bknight.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[7],(mx-12,my-12))
##       if tool=="brook.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[8],(mx-12,my-12))
##       if tool=="bpawn.png":
##           screen.blit(screenCap,canvasRect)
##           screen.blit(stamps[9],(mx-12,my-12))
##      
            
       
    screen.set_clip(None) #going back to "normal"
    

    
    oldmx,oldmy=mx,my #oldmx oldmy is the location of the mouse in the PREVIOUS FRAME
    display.flip()
##    print(pause)
##    print(songs[p]+".ogg")
##    print(p)
## 
            
quit()

