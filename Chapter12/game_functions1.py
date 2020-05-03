import pygame
import sys


def check_events(ship):
    """响应响应按键和鼠标事件"""
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type ==pygame.KEYDOWN:
            if event == pygame.K_RIGHT:
                #向右移动飞船
                ship.rect.conterx += 1