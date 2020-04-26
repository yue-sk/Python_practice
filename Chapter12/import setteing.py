import pygame
# noinspection PyUnresolvedReferences
from settings import Settings
# noinspection PyUnresolvedReferences
from ship import Ship
# noinspection PyUnresolvedReferences
import game_functions as gf



def run_game():
    #初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame .display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Allien Invasion")

    #创建一个飞船
    #创建这个名称的时候，实例的名字不可以和类的名字一致
    ship = Ship(screen)

    #开始游戏主循环
    while True:
       gf.check_events()

       #每次循环时都重绘屏幕
       screen.fill(ai_settings.bg_color)
       ship.blitme()

       #让最近绘制的屏幕可见
       pygame.display.flip()
run_game()