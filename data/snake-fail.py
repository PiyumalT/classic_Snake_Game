import pygame
import time
import random
import math

screen_high=500
screen_width=600

pygame.init()
screen=pygame.display.set_mode((screen_width, screen_high),pygame.RESIZABLE)
pygame.display.set_caption("  Snake ")
icon=pygame.image.load("icon.png")
#background=pygame.image.load("bg.png")
pygame.display.set_icon(icon)
speed=1
score=0
#fonts
font=pygame.font.Font('freesansbold.ttf',32)
ofont=pygame.font.Font('freesansbold.ttf',15)
over_font=pygame.font.Font('freesansbold.ttf',64)
textx,texty=10,10

#owner
ox=500
rrr=random.randint(0,255)
ggg=random.randint(0,255)
bbb=random.randint(0,255)

#player
body_img1=pygame.image.load("body.png")
playerx=screen_width/2
playery=screen_high*4/5
player_d="right"
#player_speed_change=speed
num_of_parts=1
playerx=[]
playery=[]
playerx.append(screen_width/2)
playery.append(screen_high*4/5)
playerx.append(screen_width/2-29)
playery.append(screen_high*4/5)
gapx=[]
gapy=[]


#food
food_img=pygame.image.load("food.png")
foodx=random.randint(10,screen_width-50)
foody=random.randint(10,screen_high-50)
"""
#enemy
enemyr_img=[]
enemyl_img=[]
enemyx=[]
enemyy=[]
enemyx_change =[]
enemyy_change =[]
num_of_enemys=6
num_of_drops=0
dropx=[]
dropy=[]
dropn=[]
enemy_drop_img=pygame.image.load("enemy_drop.png")

for i in range(num_of_enemys):
  enemyr_img.append(pygame.image.load("enemyr.png"))
  enemyl_img.append(pygame.image.load("enemyl.png"))
  enemyx.append(random.randint(0,screen_width-60))
  enemyy.append(random.randint(40,screen_high*2/5))
  temp=random.randint(0,1)
  if temp==0:
    enemyx_change.append(2*speed)
  else:
    enemyx_change.append(-2*speed)
  enemyy_change.append(random.randint(25,50))
  
#bullet
bullet_img=pygame.image.load("bullet.png")
bullety_change = -10*speed
bulletx=[]
bullety=[]
bullet_available = []
bullet_fire=[]
num_of_bullets=5
bullet_speed_change=0

for i in range(num_of_bullets):
  bulletx.append(0)
  bullety.append(playery)
  bullet_available.append( True)
  bullet_fire.append(False)
  
"""
def player():
  global playerx
  global playerx
  global num_of_parts
  for i in range (num_of_parts):
    x=playerx[i]
    y=playery[i]
    screen.blit(body_img1,(x,y))

def food (x,y):
  screen.blit(food_img,(x,y))

def iseat(x,y,foodx,foody):
  distance=math.sqrt((math.pow(x-foodx,2))+(math.pow(y-foody,2)))
  if distance<30:
    return True
  else:
    return False

"""def enemy (enemy_img,x,y):
  screen.blit(enemy_img,(x,y))

def fire (x,y):
  screen.blit(bullet_img,(x,y))
  
def iscollision(enemyx,enemyy,bulletx,bullety):
  distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
  if distance<30:
    return True
  else:
    return False
  
def show_score(x,y):
  score_img=font.render("Score :"+str(score),True,(255,255,000))
  screen.blit(score_img,(x,y))

def game_over_text():
  over_img=over_font.render("GAME OVER",True,(255,000,000))
  screen.blit(over_img,(screen_width*0.13,screen_high*2/5))
"""  
running=True

while running:
  screen.fill((0,0,0))
  #screen.blit(background,(0,0))
  time.sleep(1/(100+score*10))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type== pygame.VIDEORESIZE:
      screen_width=event.w
      screen_high=event.h
      #print (screen_high)
      screen=pygame.display.set_mode((screen_width, screen_high),pygame.RESIZABLE)

    if event.type== pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        player_d="left"
      if event.key==pygame.K_RIGHT:
        player_d="right"
      if event.key==pygame.K_UP:
        player_d="up"
      if event.key==pygame.K_DOWN:
        player_d="down"
     
    if event.type==pygame.KEYUP:
      if event.key==pygame.K_LEFT:
        player_d="left"
      if event.key==pygame.K_RIGHT:
        player_d="right"
      if event.key==pygame.K_UP:
        player_d="up"
      if event.key==pygame.K_DOWN:
        player_d="down"
   
  #player
  list_tempx=playerx
  list_tempy=playery
  for i in range (num_of_parts):  
    if playerx[i]<0:
      playerx[i]=screen_width-30
    elif playerx[i]>screen_width-30:
      playerx[i]=0
    elif playery[i]<0:
      playery[i]=screen_high-30
    elif playery[i]>screen_high-30:
      playery[i]=0
    lastx,lasty=playerx[i],playery[i]
  for i in range (num_of_parts-1):
    gapx.append(list_tempx[i+1]-list_tempx[i])
    gapy.append(list_tempy[i+1]-list_tempy[i])
  #print (playerx)


  part_run=0
  while part_run<num_of_parts:
    playerx[part_run]=playerx[part_run+1]
    playery[part_run]=playery[part_run+1]
    part_run+=1


  if player_d=="left":
    playerx[-1]-=speed
  elif player_d=="right":
    playerx[-1]+=speed
  elif player_d=="up":
    playery[-1]-=speed
  elif player_d=="down":
    playery[-1]+=speed
    
  #print (playerx)
  #print (list_tempx)
  #for i in range (num_of_parts-1):
   # playerx[i+1]=list_tempx[i]-gapx[i]
   # playery[i+1]=list_tempy[i]-gapy[i]
  
        


 # print (playery)
 # print (playerx)
  player()
  #eat
  eat=iseat(playerx[0],playery[0],foodx,foody)
  if eat:
    foodx=random.randint(10,screen_width-50)
    foody=random.randint(10,screen_high-50)
    score+=1
    if player_d=="left":
      playerx.append(lastx+29)
      playery.append(lasty)
    elif player_d=="right":
      playerx.append(lastx-29)
      playery.append(lasty)
    elif player_d=="up":
      playery.append(lasty+29)
      playerx.append(lastx)
    elif player_d=="down":
      playery.append(lasty-29)
      playerx.append(lastx)
    num_of_parts+=1
        

  food(foodx,foody)
  pygame.display.update()

"""  
  #enemy
  for i in range(num_of_enemys):
    if enemyy[i]>screen_high*4.2/5:
      for j in range (num_of_enemys):
        enemyy[j]=screen_high*200
      game_over_text()
      break
    
    if enemyx[i]<-10:
      enemyx_change[i]=2*speed
      #enemyy+=enemyy_change
    elif enemyx[i]>screen_width-50:
      enemyx_change[i]=-2*speed
      #enemyy+=enemyy_change
    if enemyy[i]> screen_high-50:
      enemyy[i]-=screen_high*4/5

    enemyx[i]+=enemyx_change[i]
    enemyy[i]+=(enemyy_change[i]/250)*(score/10)
    
    
    #random
    enemy_rand=random.randint(1,3)
    if enemy_rand>1:
      enemy_img=enemyr_img[i]
    else:
      enemy_img=enemyl_img[i]

    #collision
    for q in range(num_of_bullets):
      collision=iscollision(enemyx[i],enemyy[i],bulletx[q],bullety[q])
      if collision:
        bullet_fire[q]=False
        bullet_available[q]=True
        bulletx[q]=0
        bullety[q]=playery
        score+=1
        dropx.append(enemyx[i])
        dropy.append(enemyy[i])
        dropn.append(i)
        num_of_drops+=1
        enemyx[i]=-1000#random.randint(0,screen_width-60)
        enemyy[i]=-1000#random.randint(40,screen_high*2/5)

    for j in range (num_of_drops) :
      if dropy[j]<=screen_high+10:
        dropy[j]+=(speed*2)
        enemy(enemy_drop_img,dropx[j],dropy[j])
      else:
        dropy.pop(j)
        dropx.pop(j)
        num_of_drops-=1
        jjj=dropn[j]
        dropn.pop(j)
        enemyx[jjj]=random.randint(0,screen_width-60)
        enemyy[jjj]=random.randint(40,200)
        break
      
    enemy(enemy_img,enemyx[i],enemyy[i])
  
  #dropping

    
  #bullet
  for r in range(num_of_bullets):
    if bullet_fire[r]:
      if bullety[r]<-10:
        bullet_fire[r]=False
        bullet_available[r]=True
      else:
        bullet_speed_change=-score/10
        bullety[r]+=bullety_change+bullet_speed_change
        fire(bulletx[r],bullety[r])

  #owner
  if ox<-270:
    ox=screen_width
    rrr=random.randint(0,255)
    ggg=random.randint(0,255)
    bbb=random.randint(0,255)
  else:
    ox-=speed
   
  
#  show_score(textx,texty)
#  creater_img=ofont.render("This Game Created by : (c) TPC - 2020 ",True,(rrr,ggg,bbb))
#  screen.blit(creater_img,(ox,screen_high-20))
  

""" 
pygame.quit() 
