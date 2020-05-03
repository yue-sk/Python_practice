import  sys
import  pygame

class   Settings():
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

class cat():
    def __init__(self,screen):
        """初始化对象并设置其初始位置"""
        self.screen = screen

        self.image = pygame.image.load('image/cat.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.conterx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def run_game():
    pygame.init()
    ai_settings  = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width))
    pygame.display.set_caption("Cat")

    #开始主循环
    while True:
        check_events()

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        cat.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()

