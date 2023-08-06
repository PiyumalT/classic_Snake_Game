import pygame
import time
import random

screen_high=500
screen_width=600

pygame.init()
screen=pygame.display.set_mode((screen_width, screen_high))
pygame.display.set_caption("  Bar game ")
speed=3
score=0
game_over=False

#owner
ox=screen_width
ox2=True

#font
score_font=pygame.font.Font('freesansbold.ttf',32)
o_font=pygame.font.Font('freesansbold.ttf',15)
over_font=pygame.font.Font('freesansbold.ttf',64)


#ball
ball_img=pygame.image.load("ball.png")
ballx=screen_width/2
bally=screen_high*4/5
ball_speed=speed*0.2
ballx_change=ball_speed
bally_change=ball_speed

#bar
bar_img=pygame.image.load("bar.png")
barx1=-25
barx2=screen_width-40
bary=screen_high*4/5
bar_change=0
bar_high=92

#secbar
secbar_img=pygame.image.load("bar2.png")
secbary1=0
secbary2=screen_high-30
secbarx=screen_width/2
secbar_change=0
secbar_high=92

def bar(y):
  screen.blit(bar_img,(barx1,y))
  screen.blit(bar_img,(barx2,y))

def secbar(x):
  screen.blit(secbar_img,(x,secbary1))
  screen.blit(secbar_img,(x,secbary2))
  
def ball (x,y):
  screen.blit(ball_img,(x,y))

def show_score():
  score_img=score_font.render("Score : "+str(score),True,(255,255,000))
  screen.blit(score_img,(10,10))

def game_over_text():
  over_img=over_font.render("GAME OVER",True,(255,000,000))
  screen.blit(over_img,(screen_width*0.13,screen_high*2/5))
  
def owner(ofont):
  global ox
  global ox2
  global rrr,ggg,bbb
  if ox2:
    rrr,ggg,bbb=000,222,000
    ox2=False
  if ox<-270:
    ox=screen_width
    rrr=r=random.randint(0,255)
    ggg=random.randint(0,255)
    bbb=random.randint(0,255)
  else:
    ox-=speed/20
  creater_img=ofont.render("This Game Created by : (c) TPC - 2020 ",True,(rrr,ggg,bbb))
  screen.blit(creater_img,(ox,screen_high-20))


running=True

while running:
  screen.fill((0,0,0))
  #screen.blit(background,(0,0))
  ttt=score*10
  time.sleep(1/(300+ttt))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type== pygame.KEYDOWN:
      if event.key==pygame.K_UP:
        bar_change=-speed
      if event.key==pygame.K_DOWN:
        bar_change=speed
      if event.key==pygame.K_RIGHT:
        secbar_change=speed
      if event.key==pygame.K_LEFT:
        secbar_change=-speed

    if event.type==pygame.KEYUP:
      if event.key==pygame.K_UP or event.key ==pygame.K_DOWN:
        bar_change=0
      if event.key==pygame.K_RIGHT or event.key ==pygame.K_LEFT:
        secbar_change=0

  #bar     
  if bary<-5:
    bary=-5
  elif bary>screen_high-bar_high-4:
    bary=screen_high-bar_high-4
  if secbarx<-5:
    secbarx=-5
  elif secbarx>screen_width-secbar_high-4:
    secbarx=screen_width-secbar_high-4
    
  #ball
  ball_speed2=ball_speed
  if ballx>screen_width-35:
    if bally-bary<bar_high and bally-bary>-20:
      if ballx>0 and ballx<screen_width-33:
        score+=1
        ballx_change=-ball_speed2
  elif ballx<10:
    if bally-bary<bar_high and bally-bary>-20:
      if ballx>0 and ballx<screen_width-33:
        score+=1
        ballx_change=ball_speed2
  elif bally>screen_high-60:
     if ballx-secbarx<secbar_high and ballx-secbarx>-10:
       if bally>0 and bally<screen_high-58:
         score+=1
         bally_change=-ball_speed2
  elif bally<10:
    if ballx-secbarx<secbar_high and ballx-secbarx>-10:
       if bally>0 and bally<screen_high-58:
         bally_change=ball_speed2
         score+=1

  if ballx<-10 or ballx>screen_width:
    game_over=True
  elif bally<-10 or bally>screen_high:
    game_over=True

  if game_over:
    game_over_text()
  else:
    ballx+=ballx_change
    bally+=bally_change 
    secbarx+=secbar_change 
    bary+=bar_change
    bar(bary)
    secbar(secbarx)
    ball(ballx,bally)
    
  show_score()
  owner(o_font)
  pygame.display.update()


pygame.quit() 


        
