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

        pygame.display.flip()

    def __bg(self):
        bgi = pygame.image.load('../lib/image/bg.jpg')
        self.screen.blit(bgi, (0, 0))

    def __draw(self):
        pass

    @staticmethod
    def mainloop():
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

if __name__ == '__main__':
    Index().mainloop()

