"""
    #↓船の座標が設定した枠を超えないようにコードしている
    ship[0] = max(-800, min(800, ship[0]))
    ship[1] = max(-800, min(800, ship[1]))
"""

import sys
import pygame
from pygame.locals import QUIT,KEYDOWN,Rect,K_LEFT,K_RIGHT,K_SPACE
from random import randint
from math import

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE=pygame.display.set_mode(())
FPSCLOCK=pygame.time.Clock()

#テトリスの横10行縦20行
EXIST_POS_LIST=[]

#↓ブロックごとのサブクラスと、それのスーパークラスを作ろうとした。
"""
class super_class():
    def __init__(self,pos):
        self.center_pos=pos
        self.box_pos_list=[]
        move=True

    #とりあえずうごかすだけで、積み重なって止まるコードを含んでいない
    def move(self,key):
        if key==K_RIGHT:
            for i in self.box_pos_list:
                if i[0]+1>10:
                    move=False
                else:
                    move=True
                    
            if move:
                for i in self.box_pos_list:
                    i[0]+=1
                    i[1]+=1
            else:
                for i in self.box_pos_list:
                    i[1]+=1
                    
        if key==K_LEFT:
            for i in self.box_pos_list:
                if i[0]-1<1:
                    move=False
                else:
                    move=True

            if move:
                for i in self.box_pos_list:
                    i[0]-=1
                    i[1]+=1
            else:
                for i in self.box_pos_list:
                    i[1]+=1        
        
    def lotate(self):
        #右回転
        test_list=self.box_pos_list.copy()
        
    
class stick(super_class):
    def __init__(self):
"""

class tetris():
    global EXIST_POS_LIST
    
    #初期ポスは欄外にならないように、端は避ける！
    def __init__(self,pos=[5,0],which_type):
        self.center_pos=pos
        self.type=which_type
        #この時点で、形を生成する
        self.item_pos_list=[pos]
        #0が棒,1が四角,2がL字,3が逆L字,4がZ,5が逆Z,6がト字
        if which_type==0:
            self.item_pos_list.extend([[pos[0],pos[1]+1],[pos[0],pos[1]-1],[pos[0],pos[1]-2]])
        elif which_type==1:
            self.item_pos_list.extend([[pos[0]+1,pos[1]],[pos[0],pos[1]-1],[pos[0]+1,pos[1]-1]])
        elif which_type==2:
            self.item_pos_list.extend([[pos[0],pos[1]+1],[pos[0]+1,pos[1]+1],[pos[0],pos[1]-1]])
        elif which_type==3:
            self.item_pos_list.extend([[pos[0],pos[1]+1],[pos[0]-1,pos[1]+1],[pos[0],pos[1]-1]])
        elif which_type==4:
            self.item_pos_list.extend([[pos[0]+1,pos[1]],[pos[0],pos[1]-1],[pos[0]-1,pos[1]-1]])
        elif which_type==5:
            self.item_pos_list.extend([[pos[0]-1,pos[1]],[pos[0],pos[1]-1],[pos[0]+1,pos[1]-1]])
        elif which_type==6:
            self.item_pos_list.extend([[pos[0],pos[1]-1],[pos[0]+1,pos[1]],[pos[0]-1,pos[1]]])
            
        #↓ブロックが動かなくなったらそのインスタンスを消去したいので、その判定のための変数
        self.vanish=False

    #下についてから少しだけ左右に動けるコードは実装していない
    def move_stop(self,key):
        #↓moveでブロックが下端に来るのを防いでいる moveの初期化を忘れずに!!!
        move=True
        for i in self.item_pos_list:
           if i[1]+1>20:
              move=False
        #↓既存のブロックと重ならないかテストしている
        test=EXIST_POS_LIST.copy()
        test.extend(self.item_pos_list)
        if len(set(test))==len(test) and move==True:
            if key==K_RIGHT:
              move_right=True
              for i in self.item_pos_list:
                  if i[0]+1>10:
                     move_right=False
              if move_right:
                 for i in self.item_pos_list:
                    i[0]+=1
                    i[1]+=1
            elif key==K_LEFT:
              move_left=True
              for i in self.item_pos_list:
                  if i[0]-1<1:
                     move_left=False
              if move_left:
                 for i in self.item_pos_list:
                    i[0]-=1
                    i[1]+=1
            else:
               for i in self.item_pos_list:
                  i[1]+=1
        #↓既存のブロックと重なったか、下端に達した場合の処理
        elif set(test)!=len(test) or move==False:
            EXIST_POS_LIST.extend(self.item_pos_list)
            self.vanish=True
            
    def rotate(self):
        #↓回転して枠外に出るか,既存のブロックと重なるかどうかをテストを作って審議している
        count_=0
        rotate=True
        test_list=self.item_pos_list.copy()
        for i in test_list:
            test_list[count][0]=self.center_pos[0]+(i[1]-self.center_pos[1])
            test_list[count][1]=self.center_pos[1]-(i[0]-self.center_pos[0])
            if test_list[count][0]>=1 and test_list[count][0]<=10 and test_list[count][1]<=20
               rotate=False
            count+=1
        
        #重なるかどうかは集合の数と元のリストの数が一致するかで判断する
        test=EXIST_POS_LIST.copy()
        test.extend(test_list)
        
        if rotate and len(set(test))==len(test):
           for i in test_list:
           self.item_pos_list[count][0]=self.center_pos[0]+(i[1]-self.center_pos[1])
           self.item_pos_list[count][1]=self.center_pos[1]-(i[0]-self.center_pos[0])
        
    @classmethod
    def remove_and_rebuild:
        #↓リストインリスト内のindexとy座標が1ズレていることに注意！！！yがnなら indexはn-1
        order_list=[[] for x in range(20)]
        #↓y座標ごとに座標を分けていく
        for i in EXIST_POS_LIST:
           order_list.insert(i[1]-1,i)
        #↓リストインリスト内で、数が10個の物があれば、それが横一列揃っていることになる。横一列揃ったy座標は消去リストに入れる。
        vanish_y_list=[]
        y=1
        for i in order_list:
           if len(i)==10:
              vanish_y_list.append(y)
           y+=1
        #↓既存ブロックリストのうち、消去リスト内のy座標を持つ座標を消去かつ、消去リスト内で最小のy座標よりも小さいy座標を持つ座標はy座標を消去リストの数だけ足す
        for m in EXIST_POS_LIST:
            for n in vanish_y_list:
                if m[1]==n:
                   EXIST_POS_LIST.remove(m)
            if m[1]<min(vanish_y_list):
               m[1]+=len(vanish_y_list)
    
    def block_first_draw(self):
        for i in self.item_pos_list:
           pygame.draw.rect(SURFACE,(30*self.type,30/(self.type+1,30*(self.type/3))),Rect(),1)
    def block_next_draw(self):
        pygame.draw.rect(SURFACE,(30*self.type,30/(self.type+1,30*(self.type/3))),Rect(),1)
#def block_yield(tetris):
    

def main():
   block_type_list=[randint(0,6),randint(0,6)]
   block_first=tetris([5,0],block_type_list[0])
   exist_block_list=[block_first,tetris([],block_type_list[1])]
   game_over=False
   while 1:
      for event in pygame.event.get():
         if event.type==QUIT:
            pygame.quit()
            sys.exit()
         if event.type==KEYDOWN:
            key=event.key
      
      #ゲームオーバー判定未完
      if not game_over:
         if key==K_SPACE:
            exist_block_list[0].rotate()
         exist_block_list[0].move_stop(key)
         if block_first.vanish:
            exist_block_list.pop(0)
            exist_block_list.pop(1)
            block_type_list.pop(0)
            block_type_list.append(randint(0,6))
            exist_block_list.append(tetris([5,0],block_type_list[0])
            exist_block_list.append(tetris([5,0],block_type_list[1])
         tetris.remove_and_rebuild()
         
      SURFACE.fill((0,0,0))
      exist_block_list[0].block_first_draw()
      exist_block_list[1].block_next_draw()
            
      pygame.display.update()
      FPSCLOCK.tick(3)

if __name__=="__main__":
   main()






       
