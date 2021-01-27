import sys
import pygame
from pygame.locals import QUIT,KEYDOWN,K_SPACE,K_RIGHT,K_LEFT,Rect
from random import randint
from math import sin,cos,radians


pygame.init()
pygame.key.set_repeat(5,5)
SURFACE=pygame.display.set_mode((800,800))
FPSCLOCK=pygame.time.Clock()

#↓なるべくグローバル変数を定義しないで済むコードを書きたい。定義したクラス内で、描画まで完結すればよい
ASTEROID_COUNT=4
ASTEROID_SPEED=30
ASTEROID_DIV_SPEED=10
ASTEROID_SIZE=50

#ここで、隕石の初期リストを作る
ASTEROID_LIST=[]
"""
count_=0
while 1:
    x,y=randint(800),randint(800)
    if 350<x<550 or 350<y<550:
        continue
    else:
        div=math.radians(randint(360))
        #可変座標は必ずタプル型でなくリスト型で定義！
        ASTEROID_LIST.append({"pos":[x,y],"div":div,"size":ASTEROID_SIZE})
        count_+=1
        if count>=ASTEROID_COUNT:
            break
#
"""
SPACE_ROTATESPEED=5
LASOR_POSLIST=[]
LASOR_LIMIT_COUNT=10
LASOR_SPEED=50


#↓(重要)隕石一つ一つをアステロイドオブジェクトにしたいのに、クラス内でまとめて作るのはおかしい！！！！！
"""
class Asteroid():
#隕石を回転させながら移動させるコードが未完！
    def __init__(self,x,y,div,index_inlist):
        self.posx=x
        self.posy=y
        self.div=div
        self.i=index_inlist

    def move_asteroid(self):
        ASTEROID_LIST[self.i]["div"]=self.div+ASTEROID_DIV_SPEED
        if 0 < self.posx+ASTEROID_SPEED*math.cos(ASTEROID_LIST[self.i]["div"]) < 800 and 0 < self.posy+ASTEROID_SPEED*math.sin(ASTEROID_LIST[self.i]["div"]) < 800
           ASTEROID_LIST[self.i]["pos"][0]=self.posx+ASTEROID_SPEED*math.cos(ASTEROID_LIST[self.i]["div"])
           ASTEROID_LIST[self.i]["pos"][1]=self.posy+ASTEROID_SPEED*math.sin(ASTEROID_LIST[self.i]["div"])
        #隕石が画面外に出たら、反対側に戻す
        if self.posx+ASTEROID_SPEED*math.cos(ASTEROID_LIST[self.i]["div"])<=0 or self.posx+ASTEROID_SPEED*math.cos(ASTEROID_LIST[self.i]["div"])>=800
           ASTEROID_LIST[self.i]["pos"][0]=abs(self.pos[0]+ASTEROID_SPEED*math.cos(ASTEROID_LIST[self.i]["div"])-800)
        if self.posy+ASTEROID_SPEED*math.sin(ASTEROID_LIST[self.i]["div"])<=0 or self.posy+ASTEROID_SPEED*math.sin(ASTEROID_LIST[self.i]["div"])>=800
           ASTEROID_LIST[self.i]["pos"][1]=abs(self.pos[1]+ASTEROID_SPEED*math.sin(ASTEROID_LIST[self.i]["div"])-800)

    def split(self,index):
        #↑indexはレーザーに当たった隕石のリスト内の番号
        del.ASTEROID_LIST(index)
        #↓レーザーと衝突したら、どの様に分裂するのかが未完。(二つに分裂する)
        ASTEROID_LIST.append({"pos":[x,y],"div":,"size":ASTEROID_SIZE/2})
        ASTEROID_LIST.append({"pos":[x,y],"div":,"size":ASTEROID_SIZE/2})

    def draw(self):
        rock_rectlist=[]
        rock_image=pygame.image.load("rock.png")
        for dic in ASTEROID_LIST:
            rock_rectlist.append(Rect(dic["pos"][0],dic["pos"][1],dic["size"],dic["size"]))
        for rect in rock_rectlist:
            SURFACE.blit(rock_image,rect)
"""
class Asteroid():
    def __init__(self,x,y,div,size):
        self.rect=Rect(x,y,size,size)
        self.posx=x
        self.posy=y
        self.div=div
        self.size=size
        
    def move_asteroid(self):
        self.div+=ASTEROID_DIV_SPEED
        x_=self.posx+ASTEROID_SPEED*cos(radians(self.div))
        y_=self.pos+ASTEROID_SPEED*sin(radians(self.div))
        if 0<x_ and x_<800 and 0<y_ and y_<800:
           self.rect.move_ip(ASTEROID_SPEED*cos(radians(self.div)),ASTEROID_SPEED*sin(radians(self.div))) 
        if x_<=0 or x_>=800:
           self.rect.move_ip(abs(x_-800),0)
        if y_<=0 or y_>=800:
           self.rect.move_ip(0,abs(x_-800))

    #↓(重要)ここでは、分割するかの是非のみを考え、分割後の処理はクラス外で行う方が良い
    def split(self):
        split=False
        for rasor in LASOR_POSLIST:
            if rasor[1].colliderect(self.rect):
               split=True
        return split

    def draw(self):
        rock_image=pygame.image.load("rock.png")
        rotated_asteroid=pygame.transform.rotate(self.rect,self.div)
        rotated_asteroid.center=self.rect.center
        SURFACE.blit(rock_image,rotated_asteroid)

#↓こっちのクラスは、船をいちいちインスタンスで作る必要がないので、クラスメソッドを使う
class Space_Ship():
    #↓(重要)クラス変数の読み込みはクラス内でも、クラス名.変数名である事に注意！！！
    div=0
    rect=Rect(400,400,80,80)
    
    @classmethod
    def rotate(self,key):
        if key==K_RIGHT:
            Space_Ship.div+=SPACE_ROTATESPEED
        if key==K_LEFT:
            Space_Ship.div-=SPACE_ROTATESPEED
        
            
    def lasor_yield(self,key):
        if key==K_SPACE:
           if len(LASOR_POSLIST)>=LASOR_LIMIT_COUNT:
               #↓Rectの座標とサイズ逆にしないこと！！！
              LASOR_POSLIST.append((Rect(400+40*cos(Space_Ship.div),400+40*sin(Space_Ship.div),5,5),Space_Ship.div))

    def lasor_move(self):
        for lasor in LASOR_POSLIST:
            lasor[0].move_ip(LASOR_SPEED*cos(lasor[1]),LASOR_SPEED*sin(lasor[1]))
        """
        #↓隕石にレーザーが当たったかどうか調べる
        rock_rectlist=[]
        for dic in ASTEROID_LIST:
            rock_rectlist.append(Rect(dic["pos"][0],dic["pos"][1],dic["size"],dic["size"]))
        for rock in rock_rectlist:
            for lasor in LASOR_POSLIST:
                if rock.colliderect(lasor):
        """
                    
    def draw(self):
        #まず、船の描画
        ship_image=pygame.image.load("ship.png")
        rotated_rect=pygame.transform.rotate(Space_Ship.rect,Space_Ship.div)
        rotated_rect.center=(400,400)
        SURFACE.blit(ship_image,rotated_rect)
        #次に、レーザーの描画
        for lasor in LASOR_POSLIST:
            pygame.draw.rect(SURFACE,(255,255,0),lasor[0])

def main():
    global ASTEROID_LIST,LASOR_POSLIST,SPACE_DIV

    game_over=False
    bang_image=pygame.image.load("bang.png")
    bg_image=pygame.image.load("bg.png")
    
    bang_font=pygame.font.SysFont(None,30)
    message=bang_font.render("GAME OVER!!!",True,(255,0,0))
    message_rect=message.get_rect()
    message_rect.center=(400,400)

    #アステロイドリストにアステロイドオブジェクトを一つずつ作り、格納して初期のリストを作る
    for _ in range(4):
        count_=0
        while 1:
            x,y=randint(800),randint(800)
            if 350<x<550 or 350<y<550:
                continue
            else:
                div=randint(360)
                ASTEROID_LIST.append(Asteroid(x,y,div,ASTEROID_SIZE))
                count_+=1
                if count>=ASTEROID_COUNT:
                   break
    #
    
    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                ASTEROID_SIZE.rotate(event.key)
                ASTEROID_SIZE.lasor_yield(event.key)

        if not game_over:
            Space_Ship.lasor_move()
            cnt=0
            for asteroid in ASTEROID_LIST:
                asteroid.move_asteroid()
                if asteroid.split():
                    del.ASTEROID_LIST(cnt)
                    if asteroid.size>ASTEROID_SIZE/8:
                       #分裂体の角度未完。二つに分裂することに注意！！！
                       ASTEROID_LIST.append(Asteroid(asteroid.posx,asteroid.posx,randint(360),asteroid.size/2))
                       ASTEROID_LIST.append(Asteroid(asteroid.posx,asteroid.posx,randint(360),asteroid.size/2))
                       #
                rotated_rect=pygame.transform.rotate(Space_Ship.rect,Space_Ship.div)
                rotated_rect.center=(400,400)
                if asteroid.rect.colliderect(rotated_rect):
                    game_over=True
                cnt+=1

        #描画
        SURFACE.fill(0,0,0)
        SURFACE.blit(bg_image,SURFACE)
        for asteroid in ASTEROID_LIST:
            asteroid.draw()
        Space_Ship.draw()

        if game_over:
            SURFACE.blit(message,message_rect)
            
if __name__=="__main__":
    main()



                    
