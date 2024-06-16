# coding: utf-8

import pygame
pygame.init()

class Index:
    def __init__(self):
        width, height = 800, 600
        background = (255, 255, 255)
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(background)
        pygame.display.set_caption('GravityGame')
        self.__bg()
        self.__draw()

    # 背景
    def __bg(self):
        bgi = pygame.image.load('../lib/image/bg.jpg')
        self.screen.blit(bgi, (0, 0))

    # 绘制
    def __draw(self):
        # 标题
        head_text = pygame.font.Font(None, 100)
        head_text_surface = head_text.render('GravityGame', True, (240, 80, 20))
        self.screen.blit(head_text_surface, (200, 100))
        self.__start_button()
        self.__settings_image()

    # 开始按钮
    def __start_button(self):
        # 画长方形
        start_button = pygame.Rect(320, 300, 180, 70)
        pygame.draw.rect(self.screen, (30, 30, 30), start_button)

        # 写字
        start_text = pygame.font.SysFont("SimSun", 30)
        # start_text = pygame.font.Font("SimSun", 50)
        start_text_surface = start_text.render('开始游戏', True, (255, 255, 255))
        self.screen.blit(start_text_surface, (350, 320))

    # 设置图标
    def __settings_image(self):
        sgsi = pygame.image.load('../lib/image/settings.png')
        self.screen.blit(sgsi, (0, 0))

    @staticmethod
    def mainloop():
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

if __name__ == '__main__':
    Index().mainloop()

