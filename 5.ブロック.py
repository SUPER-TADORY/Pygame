#import sys
import sys
import pygame
from random import randint
from pygame.locals import QUIT,K_RIGHT,K_LEFT,KEYDOWN,KEYUP,Rect
from math import sin,cos,radians


pygame.init()
#↓
pygame.key.set_repeat(5,5)
SURFACE=pygame.display.set_mode=((600,800))
#↓
FPSCLOCK=pygame.time.Clock()


BOX_rectlist=[]
#↓ループごとにも逐一初期化しないといけない
ball_matchlist=(False,False)
ball_hankei=10
bar_touch=False

def box_atari_hanntei(ball_pos):
    #↓ボールの円周上に100個の点を生成し、それぞれの箱と重なり合うか確認。重なり合ったらball_matchでx,y方向どちらに跳ね返るべきかを決め、箱を消す
    ball_poslist=[]
    for num in range(100):
        ball_poslist.append((pos[0]+ball_hankei*cos(radians(3.6*num)),pos[1]+ball_hankei*sin(radians(3.6*num))))
    for box_rect in BOX_rectlist:
        i=BOX_rectlist.index(box_rect)
        for pos_ in ball_poslist:
            if box_rect.collidepoint(pos_)==True:
                if min(abs(box_rect.left-pos_[0]),abs(box_rect.right-pos_[0]))>min(abs(box_rect.top-pos_[1]),abs(box_rect.bottom-pos_[1])):
                    ball_matchlist[0]=True
                elif min(abs(box_rect.left-pos_[0]),abs(box_rect.right-pos_[0]))<min(abs(box_rect.top-pos_[1]),abs(box_rect.bottom-pos_[1])):
                    ball_matchlist[1]=True
                elif min(abs(box_rect.left-pos_[0]),abs(box_rect.right-pos_[0]))==min(abs(box_rect.top-pos_[1]),abs(box_rect.bottom-pos_[1])):
                    ball_matchlist=(True,True)
                del BOX_rectlist[i]
                break

def bar_atari_hanntei(ball_pos,bar_rect):
    for num in range(100):
        ball_poslist.append((pos[0]+ball_hankei*cos(radians(3.6*num)),pos[1]+ball_hankei*sin(radians(3.6*num))))
    for pos_ in ball_poslist:
            if bar_rect.collidepoint(pos_)==True:
                ball_matchlist[1]=True
                bar_touch=True
                break
            
def wall_atari_hanntei(ball_pos):
    if ball_pos[0]<=ball_hankei and ball_pos[0]+ball_hankei>=600:
        ball_matchlist[0]=True
    elif ball_pos[1]<=ball_hankei:
        ball_matchlist[1]=True
    
def paint():
    SURFACE.fill((0,0,0))
    gameover_font=pygame.font.Sysfont(None,36)
    message=gameover_font.render("GAMEOVER!!!",)

def main():
    #↓なんかボタン押したらスタートにしたい
    start_=False
    bar_touch=False
    bar_speed=40
    ball_x_speed=bar_speed
    ball_y_speed=10
    #↓矩形を動かしたいときは、Rect.move_ip()を使う
    bar_rect=Rect(100,30,0,100)
    ball_pos=(bar_rect.center,100+all_hankei)

    gameover_font=pygame.font.Sysfont(None,36)
    message=gameover_font.render("GAMEOVER!!!",(0,0))
    message_rect=message.get_rect()
    message_rect.center=(300,400)
    
    while 1:
        #↓逐一初期化しないと、毎ループ反転してしまう
        ball_matchlist=(False,False)
        game_over=False
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                #↓
                key=event.key
                start_=True

        

        if game_over==False:
            #↓まず、押されたキーに応じてバーを動かさないといけない
            if key==K_RIGHT:
                bar_rect.move_ip(bar_speed,0)
            elif key==K_LEFT:
                bar_rect.move_ip(bar_speed*(-1),0)
            #↓バーが画面外に出ないようにする
            bar_rect.center[0]=max(50,mix(bar_rect.center[0],550))
            bar_rect.center[1]=max(50,mix(bar_rect.center[1],750))

            box_atari_hanntei(ball_pos)
            wall_atari_hanntei(ball_pos)
            bar_atari_hanntei(ball_pos,bar_rect)

            if ball_matchlist[0]==True:
                ball_x_speed*=-1
            if ball_matchlist[1]==True:
                ball_y_speed*=-1

            if bar_touch==True:
                if key==K_RIGHT:
                    ball_pos[0]+=bar_speed
                elif key==K_LEFT:
                      ball_pos[0]+=bar_speed*(-1)
            else:
                ball_pos[0]+=ball_x_speed
            ball_pos[1]+=ball_y_speed   


            #↓ゲームオーバーの判定はif game_over==False:の中で行う
            if  ball_matchlist[1]<70:
                game_over=True

        
        SURFACE.fill((0,0,0))
        pygame.draw.rect(SURFACE,(0,0,0),bar_rect)
        for box in BOX_rectlist:
            pygame.draw.rect(SURFACE,(randint(50,255),randint(50,255),randint(50,255)),bar_box)
        pygame.draw.circle(SURFACE,(0,0,0),ball_pos,ball_hankei)

        if game_over:
            SURFACE.blit(message,message_rect,area=None, special_flags = 0)

        #↓忘れない
        pygame.display.update()
        FPSCLOCK.tick(5)

            
        
            
                
if __name__=="__main__":
    main()

