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

        pygame.display.flip()

    @staticmethod
    def mainloop():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

if __name__ == '__main__':
    Index().mainloop()

