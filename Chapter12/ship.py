import pygame

class Ship():
    """初始化飞船并获取其初始位置"""
    def __init__(self,screen):
        #指定要将飞船绘制到什么地方
        self.screen = screen

        #加载飞船图形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.conterx = self.screen_rect.conterx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置放置飞船"""
        self.screen.blit(self.image,self.rect)
