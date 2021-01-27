#####画像ファイルがないからこのままでは動かないことに注意！！！

import sys
from random import randint
import pygame
from pygame.locals import QUIT,Rect,KEYDOWN,K_SPACE


pygame.init()
pygame.key.set_repeat(5,5)
#↑キーリピートが有効になっている場合、キーが押しっぱなしの状態だと何度も pygame.KEYDOWNイベントが発生します。
SURFACE=pygame.display.set_mode((800,600))
#↑pygame.display.set_mode(resolution=(0,0), flags=0, depth=0): return Surface
#↑resolution引数を設定しなかったり(0, 0)を設定した場合に、pygameが SDLのバージョン1.2.10以降を使用していると、作成されたSurfaceはパソコンのモニターと同じ大きさとなります。
FPSCLOCK=pygame.time.Clock()


def main():
    #↓walls,ship_y,velocity,score,slopeの変数設定
    walls=80
    ship_y=250
    velocity=0
    score=0
    slope=randint(1,6)
    #↓文字のフォント、画像を設定
    sysfont=pygame.font.Sysfont(None,36)
    #画像ファイルを入れないと動かない
    ship_image=pygame.image.load("ファイル名")
    bang_image=pygame.image.load("ファイル名")
    #↓リストを作成し、初期の空洞を座標、サイズ設定しながらfor文でリスト内に追加
    holes=[]
    for xpos in range(walls):
        holes.append(Rect(xpos*10),100,10,400)
    #↓gameoverを判定するbool型変数をfalseに初期設定する
    game_over=False

    #↓mainloop
    while True:
        #↓スペースキーが押されているかどうかの変数をFalseに初期設定
        is_space_down=False
        #
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:
                    is_space_down=True
        #船を移動
        if not game_over:
            score+=10
            #↓加速度を設定し、座標に反映
            velocity+=-3 if is_space_down else 3
            ship_y+=velocity
        #洞窟をスクロール
        edge=holes[-1]
        test=edge.move(0,slope)
        if test.top<0 or test.bottom>600:
            slope=randint(1,6)*(-1 if slope>0 else 1)
            #↓傾斜切り替えごとに空洞を小さくする仕様にする
            edge.infrate_ip(0,-20)
        edge.move_ip(0,slope)
        holes.append(edge)
        del holes[0]
        holes=[x.move(-10,0) for x in holes]
        #船のゲームオーバー判定
        if ship_y<holes[0].top or ship_y>holes[0].bottom:
            game_over=True

        #画面描画
        #↓空洞の描画
        for hole in holes:
            pygame.draw.rect(SURFACE,(0,0,0),hole)
        #↓船の描画
        SURFACE.blit(ship_image,(0,ship_y))
        #↓文字を生成して、描画する
        score_image=sysfont.render("score is {}".format(score),False,(0,0,255))
        SURFACE.blit(score_image,(600,20))
        if game_over:
            SURFACE.blit(bang_image,ship_y-40)

        #↓while文の最後にpygame.display.update()を忘れない
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__=="__main__":
    main()
        
            
        
        
        
                
                
    
    
