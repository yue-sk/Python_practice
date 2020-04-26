import pygame
# noinspection PyUnresolvedReferences
from settings import Settings
# noinspection PyUnresolvedReferences
from ship import Ship
# noinspection PyUnresolvedReferences
import game_functions as gf

#开始游戏主循环
while  True:
    gf.check_evenets()
    gf.update_screen(ai_settings,screen,ship)

run_game()
