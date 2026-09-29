import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flip = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)  # 左右反転
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)  # こうかとんの初期位置
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        # kk_rct.x -= 1
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_flip, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        vx=-1#横
        vy=0#縦

        key_lst = pg.key.get_pressed()

        if key_lst[pg.K_LEFT]:
            vx -= 1

        if key_lst[pg.K_RIGHT]:
            vx += 2

        if key_lst[pg.K_UP]:
            vy -= 1

        if key_lst[pg.K_DOWN]:
            vy += 1

        # 計算した移動量で1回だけ動かす
        kk_rct.move_ip(vx, vy)
        screen.blit(kk_img, kk_rct)  # こうかとんの位置
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()