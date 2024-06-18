# coding: utf-8

import logger
import gui

l = logger.Logger()

def main():
    l.info("starting")
    gui.run(l)
    l.info("exiting")


if __name__ == '__main__':
    main()