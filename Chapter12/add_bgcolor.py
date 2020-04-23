import sys
import pygame

def run_game():
    """游戏窗口添加背景色"""

    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Allen Invasion")

    #设置背景色
    bg_color = (230,230,230)

    #开始游戏主循环
    while True:
        # 监听鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都会绘制屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()





