import sys
import pygame as pg
from  settings  import   Settings

def run_game():
    #初始化pygame，设置和屏幕对象
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Allien Invasion")

    #开始游戏主循环
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        pg.display.flip()
run_game()