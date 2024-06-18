# coding: utf-8

import pygame
import logger

pygame.init()


# GUI父类
class GUI:
    def __init__(self, log: logger.Logger):
        self.log = log
        width, height = 800, 600
        background = (255, 255, 255)
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(background)
        pygame.display.set_caption('GravityGame')
        pygame.display.set_icon(pygame.image.load('../lib/image/icon.jpg'))
        self.log.info('GUI init')

    # 事件处理
    def __event_handler(self, event, min_axis, max_axis, msg=""):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 320 < pos[0] < 500 and 300 < pos[1] < 370:
                self.log.info(f'MOUSEBUTTONDOWN_EVENT {msg} x: {pos[0]}, y: {pos[1]}')
                return 0
            # # 设置
            # elif 0 < pos[0] < 50 and 0 < pos[1] < 50:
            #     self.log.info(f'MOUSEBUTTONDOWN_EVENT {msg} x: {pos[0]}, y: {pos[1]}')
            #     return 1


# 游戏主界面
class Game(GUI):
    def __init__(self, log):
        super().__init__(log)

    def __splitline(self):
        pygame.draw.line(self.screen, (0, 0, 0), (600, 0), (600, 0), 1)

    def mainloop(self):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                # 退出
                if event.type == pygame.QUIT:
                    self.log.info('Index quit')
                    pygame.quit()
                    return


class Index(GUI):
    def __init__(self, log):
        super().__init__(log)
        self.__bg()
        self.__draw()
        self.log.info('Index init')

    # 背景
    def __bg(self):
        bgi = pygame.image.load('../lib/image/bg.jpg')
        self.screen.blit(bgi, (0, 0))
        self.log.info('Index bg')

    # 绘制
    def __draw(self):
        # 标题
        head_text = pygame.font.Font(None, 100)
        head_text_surface = head_text.render('GravityGame', True, (240, 80, 20))
        self.screen.blit(head_text_surface, (200, 100))
        self.__start_button()
        self.__settings_image()
        self.log.info('Index head text')

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

        self.log.info('Index start button')

    # 设置图标
    def __settings_image(self):
        sgsi = pygame.image.load('../lib/image/settings.png')
        self.screen.blit(sgsi, (0, 0))

        self.log.info('Index settings image')

    def mainloop(self):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                res = self.__event_handler(event, (320, 300), (500, 370), msg='STARTGAME')
                res2 = self.__event_handler(event, (0, 0), (50, 50), msg='SETTINGS')
                if (res is not None) or (res2 is not None):
                    return res

                # 退出
                if event.type == pygame.QUIT:
                    self.log.info('Index quit')
                    pygame.quit()
                    return


def run(log):
    index = Index(log)
    res = index.mainloop()
    if res == 0:
        game = Game(log)
        game.mainloop()
