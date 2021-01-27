import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN

#↓グローバル変数を設定
WIDTH=20
HEIGHT=15
SIZE=50
NUM_OF_BOMBS=20
EMPTY=0
BOMB=1
OPENED=2
OPEN_COUNT=0
CHECKED=[[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
 
pygame.init()
SURFACE=pygame.display.set_mode([WIDTH*SIZE,HEIGHT*SIZE])
FPSCLOCK=pygame.time.Clock()

def num_of_bomb(field,x_pos,y_pos):
    """周囲にある爆弾の数を返す"""
    count=0
    for y_pos_num in range(-1,2):
        for x_pos_num in range(-1,2):
        #↓ミス：これは明らかにアウト、渡された引数は変数ではないので、新しく変数を設定して代入しないといけない
            #x_pos+=x_pos_num
            #y_pos+=y_pos_num
            #↓正解
            xpos,ypos=(x_pos+x_pos_num,y_pos+y_pos_num)
        #↓ミス：指定したマスが格子内にあるかを判定しないといけないのと、xpos,yposを使わないといけない
            #if field[y_pos][x_pos]==BOMB:
            #↓正解
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
               count+=1
    return count
            
def open_tile(field,x_pos,y_pos):
    """タイルをオープン"""
    global OPEN_COUNT
    if CHECKED[x_pos][y_pos]==True:
       return
       
    CHECKED[x_pos][y_pos]==True
    
    #↓この初期化コードは必要ではない
    count=0
    for y_pos_num in range(-1,2):
        for x_pos_num in range(-1,2):
            #↓ミス：上と同じで、引数は変数でないので、新しく変数を用意して代入しないといけない
            #x_pos+=x_pos_num
            #y_pos+=y_pos_num
            #↓正解
            xpos,ypos=(x_pos+x_pos_num,y_pos+y_pos_num)
            #↓ミス：以下、xpos,yposを使わないといけない
            #if 0=<x_pos<WIDTH and 0=<y_pos<HEIGHT and field[y_pos][x_pos]==EMPTY:
            #↓正解
            if 0=<x_pos<WIDTH and 0=<y_pos<HEIGHT and field[ypos][xpos]==EMPTY:
               field[ypos][xpos]==OPENED
               #↓抜け
               OPEN_COUNT+=1
               #
               count=num_of_bomb(field,xpos,ypos)
               #↓わからなかった：押した自分自身だと、同じ操作を二回してしまうことになる
               #if count==0 and
               #↓正解
               if count == 0 and not (xpos == x_pos and ypos == y_pos):
                  open_tile(field,xpos,ypos)
                    
def main():
    """メインルーチン"""
    smallfont=pygame.font.SysFont(None,36)
    largefont=pygame.font.SysFont(None,72)
    message_clear=largefont.render("!!CLEARED!!",True,(0,255,225))
    message_over=largefont.render("GAMEOVER!!",True,(0,255,225))
    message_rect=message_clear.get_rect()
    message_rect.center=(WIDTH*SIZE/2,HEIGHT*SIZE/2)
    game_over=False
    field=[[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]
    #爆弾を設置
    count=0
    while count<NUM_OF_BOMBS:
        xpos,ypos=randint(0,WIDTH1),randint(0,HEIGHT1)
        if field[ypos][xpos]==EMPTY:
            field[ypos][xpos]=BOMB
            count+=1
            
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                xpos,ypos=floor(event.pos[0]/SIZE),floor(event.pos[1]/SIZE)
                if field[ypos][xpos]==BOMB:
                   game_over=True
                else:
                   open_tile(field,xpos,ypos)

    #描画
         SURFACE.fill((0,0,0))
         for　ypos　in　range(HEIGHT):
            for xpos in range(WIDTH):
                tile=field[ypos][xpos]
                rect=(xpos*SIZE,ypos*SIZE,SIZE,SIZE)
                if tile==EMPTY or tile==BOMB:
                    pygame.draw.rect(SURFACE,(192,192,192),rect)
                    if game_over and tile==BOMB:
                        pygame.draw.ellipse(SURFACE,(225,225,0),rect)
                elif tile==OPENED:
                    count=num_of_bomb(field,xpos,ypos)
                    if count>0:
                        num_image=smallfont.render("{}".format(count),True,(255,255,0))
                        SURFACE.blit(num_image,(xpos*SIZE+10,ypos*SIZE+10))

     #線の描画
         for index in range(0,WIDTH*SIZE,SIZE):
             pygame.draw.line(SURFACE,(96,96,96),(index,0),(index,HEIGHT*SIZE))
         for index in range(0,HEIGHT*SIZE,SIZE):
             pygame.draw.line(SURFACE,(96,96,96),(0,index),(WIDTH*SIZE,index))

     #メッセージの描画
         if OPEN_COUNT==WIDTH*HEIGHTNUM_OF_BOMBS:
             SURFACE.blit(message_clear,message_rect.topleft)
         elif game_over:
             SURFACE.blit(message_over,message_rect.topleft)
             
         pygame.display.update()
         FPSCLOCK.tick(15)

if __name__ =="__main__":
    main()

   




 






 

 
