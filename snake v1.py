import pygame
import time
import random
import math

screen_high=500
screen_width=600

pygame.init()
screen=pygame.display.set_mode((screen_width, screen_high),pygame.RESIZABLE)
pygame.display.set_caption("  Snake  By (c)TPC")
icon=pygame.image.load("data\\icon.png")
background=pygame.image.load("data\\background.jpg")
pygame.display.set_icon(icon)
speed=10
#fonts
score_font=pygame.font.Font('freesansbold.ttf',32)
font=pygame.font.Font('freesansbold.ttf',32)
ofont=pygame.font.Font('freesansbold.ttf',15)
over_font=pygame.font.Font('freesansbold.ttf',64)
textx,texty=10,10
mscore=0

#owner
ox=500
rrr=random.randint(0,255)
ggg=random.randint(0,255)
bbb=random.randint(0,255)

def player():
  global body_img
  global head_img
  global partx
  global party
  global x_change
  global speed
  global y_change
  global new_part
  global score
  global mega_food_available
  global time_bar
  global mscore

  body_img=pygame.image.load("data\\body.png")
  head_img=pygame.image.load("data\\head.png")
  partx=screen_width/2
  party=screen_high*4/5
  x_change=speed
  y_change=0
  score=0
  mega_food_available=False
  time_bar=0
  mscore=0
  #player_speed_change=speed
  num_of_parts=4
  partx=[]
  party=[]
  partx.append(screen_width/2)
  party.append(screen_high*4/5)
  partx.append(screen_width/2-20)
  party.append(screen_high*4/5)
  partx.append(screen_width/2-20)
  party.append(screen_high*4/5)
  partx.append(screen_width/2-20)
  party.append(screen_high*4/5)
player()

#food
food_img_1=pygame.image.load("data\\food1.png")
food_img_2=pygame.image.load("data\\food2.png")
mega_food_icon1=pygame.image.load("data\\mfood1.png")
mega_food_icon2=pygame.image.load("data\\mfood2.png")
foodx=random.randint(10,screen_width-50)
foody=random.randint(10,screen_high-50)
food_img=food_img_1

def show_body():
  global partx
  global party
  global num_of_parts
  global body_img1

  for i in range (len(partx)):
    x=partx[i]
    y=party[i]
    screen.blit(body_img,(x,y))
  screen.blit(head_img,(partx[-1],party[-1]))
  #print("aaa")

def show_food (x,y):
  screen.blit(food_img,(x,y))

def show_mfood (x,y):
  aa=random.randint(0,10)
  if aa<5:
    screen.blit(food_img_1,(x+10,y+10))
  else:
    screen.blit(mega_food_icon2,(x,y))

def iseat(x,y):
  global foodx
  global foody


  distance=math.sqrt((math.pow(x-foodx,2))+(math.pow(y-foody,2)))
  if distance<30:
    return True
  else:
    return False

def iseat_m(x,y):
  global mfoodx
  global mfoody
  global mscore
  global mega_food_available
  
  distance=math.sqrt((math.pow(x-mfoodx,2))+(math.pow(y-mfoody,2)))
  if distance<40:
    mscore+=1
    mega_food_available=False
    mfoodx=-1000
    mfoody=-1000
    

def move():
  global partx
  global party
  global num_of_parts
  global x_change
  global y_change
  global screen_width
  global screen_high

  if num_of_parts>1:
    current_part=0
    while (current_part+1)<num_of_parts:
      partx[current_part]=partx[(current_part+1)]
      party[current_part]=party[(current_part+1)]
      current_part+=1
  if partx[-1]>screen_width-25:
    partx[-1]=0
  elif partx[-1]<0:
    partx[-1]=screen_width-26
  else:
    partx[-1]=(int(partx[-1])+int(x_change))
  if party[-1]>screen_high-25:
    party[-1]=0
  elif party[-1]<0:
    party[-1]=screen_high-26
  else:
    party[-1]=(int(party[-1])+int(y_change))

def game_over_text():
  over_img=over_font.render("GAME OVER",True,(255,000,000))
  screen.blit(over_img,(screen_width*0.13,screen_high*2/5))
  show_score_o()
  pygame.display.update()

  

def new_part(x,y):
  global x_change
  global y_change
  global partx
  global party
  global num_of_parts
  global foodx
  global foody
  global score
  global food_img
  global mega_food_available

  num_of_parts+=1
  foodx=random.randint(10,screen_width-50)
  foody=random.randint(50,screen_high-50)
  food_pic_num=random.randint(0,1)
  if food_pic_num==0:
    food_img=food_img_1
  else:
    food_img=food_img_2

  score+=1
  if score%5==0:
    mega_food_available=True
    mega_food()
  #print ("aaaaaaaaaaaaaaaaaaaaaa")
  if x_change>0:
    partx.append(x+speed)
    party.append(y)

  elif x_change<0:
    partx.append(x-speed)
    party.append(y)

  elif y_change>0:
    partx.append(x)
    party.append(y+speed)

  elif x_change<0:
    partx.append(x)
    party.append(y+speed)

def is_crash():
  global partx
  global party
  head_x=partx[-1]
  head_y=party[-1]
  current_part=0
  while current_part<len(partx)-2:
    dis2=math.sqrt((math.pow(head_x-partx[current_part],2))+(math.pow(head_y-party[current_part],2)))
    current_part+=1
    if dis2<10:
      game_over=True
      game_over_text()
      player()
      time.sleep(5)
      break

def show_score():
  global score
  global mscore
  score_img=score_font.render("Score : "+str(score+mscore*5),True,(255,255,000))
  screen.blit(score_img,(10,10))

def show_score_o():
  global score
  score_img=score_font.render("Your Total Score : "+str(score+mscore*5),True,(255,255,000))
  screen.blit(score_img,(150,screen_high*1/4))

def mega_food():
  global time_bar
  global mfoodx
  global mfoody

  mfoodx=random.randint(10,screen_width-50)
  mfoody=random.randint(50,screen_high-50)
  time_bar=50





running=True

while running:
  screen.fill((0,0,0))
  screen.blit(background,(0,0))
  time.sleep(1/(screen_width/20))
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
        x_change=-speed
        y_change=0
      elif event.key==pygame.K_RIGHT:
        x_change=speed
        y_change=0
      elif event.key==pygame.K_UP:
        y_change=-speed
        x_change=0
      elif event.key==pygame.K_DOWN:
        y_change=speed
        x_change=0
  num_of_parts=len(partx)
  move()
  aaa=iseat(partx[-1],party[-1])
  if mega_food_available:
    if time_bar>0:
      if time_bar==1:
        mfoodx=-1000
        mfoody=-1000
        mega_food_available=False
      else:
        
        show_mfood(mfoodx,mfoody)
        iseat_m(partx[-1],party[-1])
    time_bar-=1

  if aaa:
    new_part(partx[-1],party[-1])

  show_body()
  show_food(foodx,foody)
  
  #print (partx)
  is_crash()
  show_score()
  pygame.display.update()
















pygame.quit() 
