# 创建一个蓝色背景的窗口


import sys
import pygame

def run_game():
    pygame.init()

    #创建一个屏幕对象
    screen = pygame.display.set_mode((1200,800))
    #不活屏幕中的对象
    pygame.display.set_caption("Alien Invasion")
    bg_color = (0,0,255)

    #开始游戏主循环
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        #每次循环都填充颜色
        screen.fill(bg_color)

    #让最近的绘制的屏幕可见
    pygame.display.flip()


run_game()

