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
    def event_handler(self, event, min_axis, max_axis, msg=""):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if min_axis[0] < pos[0] < max_axis[0] and min_axis[1] < pos[1] < max_axis[1]:
                self.log.info(f'MOUSEBUTTONDOWN_EVENT {msg} x: {pos[0]}, y: {pos[1]}')
                return msg


# 游戏主界面
class Game(GUI):
    def __init__(self, log):
        super().__init__(log)
        self.mass_choose_s = False
        self.mass_choose_b = False
        self.__splitline()
        self.__bg()
        self.__back()
        self.__mass()
        self.log.info('game gui init')
        # pygame.draw.line(self.screen, (0, 0, 0), (0, 100), (30, 100), 2)

        # rect = pygame.Rect(605, 100, 80, 80)
        # pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)

    # 画分割线
    def __splitline(self):
        pygame.draw.line(self.screen, (0, 0, 0), (600, 0), (600, 600), 2)

    # 游戏背景图片
    def __bg(self):
        gbg = pygame.image.load('../lib/image/game_bg.jpg')
        self.screen.blit(gbg, (0, 0))

    # 返回图片
    def __back(self):
        backi = pygame.image.load('../lib/image/back.png')
        self.screen.blit(backi, (610, 0))

    # 砝码图片
    def __mass(self):
        # 小砝码
        weighti = pygame.image.load('../lib/image/red_mass.jpg')
        self.screen.blit(weighti, (660, 20))

        # 大砝码
        weighti = pygame.image.load('../lib/image/red_mass_big.jpg')
        self.screen.blit(weighti, (660, 130))

    # 砝码放置事件
    def __mass_p_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 30 + 1
            y = pos[1] // 40 + 1

            if 12 <= x <= 20:
                self.log.info(f'MOUSEBUTTONDOWN_MASSEVENT x: {x}, y: {y} MOUSEX: {pos[0]} MOUSEY: {pos[1]}')
                return x, y
            else:
                self.log.info(f'MOUSEBUTTONDOWN_MASSEVENT x: {x}, y: {y} MOUSEX: {pos[0]} MOUSEY: {pos[1]} TOO BIG OR SMALL')

    # 砝码显示
    def __mass_display(self, x, y):
        # weighti = pygame.image.load('../lib/image/red_mass.jpg')
        # self.screen.blit(weighti, (30 * x, 40 * y))
        # 显示小砝码
        if self.mass_choose_s:
            self.log.info(f'DISPLAY_MASSEVENT_SMALL x: {x}, y: {y}')
            pygame.draw.circle(self.screen, (255, 0, 0), (30 * x - 15, 40 * y - 20), 10, 3)
        # 显示大砝码
        elif self.mass_choose_b:
            self.log.info(f'DISPLAY_MASSEVENT_BIG x: {x}, y: {y}')
            pygame.draw.circle(self.screen, (255, 0, 0), (30 * x - 15, 40 * y - 20), 10, 0)

    # 砝码选择
    def __mass_choose(self, event_type):
        # 小砝码
        if event_type == 'small':
            self.log.info('MASS-CHOOSE-SMALL')
            # 如果小砝码已选择，就不选择小砝码
            if self.mass_choose_s:
                pygame.draw.circle(self.screen, (255, 255, 255), (700, 60), 48, 5)
                self.mass_choose_s = False
                self.log.info('MASS_CHOOSE_S IS FALSE')
                return

            # 选择小砝码
            self.mass_choose_s = True
            self.log.info('MASS_CHOOSE_S IS TRUE')
            pygame.draw.circle(self.screen, (255, 255, 0), (700, 60), 48, 5)

            # 如果大砝码已选择，就不选择大砝码
            if self.mass_choose_b:
                pygame.draw.circle(self.screen, (255, 255, 255), (700, 170), 48, 5)
                self.mass_choose_b = False
                self.log.info('MASS_CHOOSE_B IS FALSE')
        # 大砝码
        elif event_type == 'big':
            self.log.info('MASS-CHOOSE-BIG')
            # 如果大砝码已选择，就不选择大砝码
            if self.mass_choose_b:
                pygame.draw.circle(self.screen, (255, 255, 255), (700, 170), 48, 5)
                self.mass_choose_b = False
                self.log.info('MASS_CHOOSE_B IS FALSE')
                return

            # 选择大砝码
            self.mass_choose_b = True
            self.log.info('MASS_CHOOSE_B IS TRUE')
            pygame.draw.circle(self.screen, (255, 255, 0), (700, 170), 48, 5)

            # # 如果小砝码已选择，就不选择小砝码
            if self.mass_choose_s:
                pygame.draw.circle(self.screen, (255, 255, 255), (700, 60), 48, 5)
                self.mass_choose_s = False
                self.log.info('MASS_CHOOSE_S IS FALSE')

    def mainloop(self):
        while True:
            pygame.display.update()  # 刷新
            for event in pygame.event.get():
                res = self.__mass_p_event(event)
                mcr = self.event_handler(event, (660, 20), (740, 100), msg="MASSCHOOSEEVENT")  # 检测小砝码是否被选择
                mcrb = self.event_handler(event, (660, 130), (740, 210), msg="MASSCHOOSEBIGEVENT")  # 检测大砝码是否被选择
                if res is not None:
                    x, y = res
                    self.__mass_display(x, y)
                if mcr == 'MASSCHOOSEEVENT':
                    self.__mass_choose('small')  # 选择小砝码
                elif mcrb == 'MASSCHOOSEBIGEVENT':
                    self.__mass_choose('big')  # 选择大砝码

                # back
                res = self.event_handler(event, (610, 0), (660, 50), 'BACKTOINDEX')
                if res is not None:
                    if res == 'BACKTOINDEX':
                        return 2

                # 退出
                if event.type == pygame.QUIT:
                    self.log.info('game quit')
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
                res = self.event_handler(event, (320, 300), (500, 370), msg='STARTGAME')
                res2 = self.event_handler(event, (0, 0), (50, 50), msg='SETTINGS')
                if (res is not None) or (res2 is not None):
                    if res == 'STARTGAME':
                        return 0
                    elif res == 'SETTINGS':
                        return 1

                # 退出
                if event.type == pygame.QUIT:
                    self.log.info('Index quit')
                    pygame.quit()
                    return


def run(log):
    index = Index(log)
    res = index.mainloop()
    if res == 0:
        log.info('start game')
        game = Game(log)
        game.mainloop()
