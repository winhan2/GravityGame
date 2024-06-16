# coding: utf-8

import logger
import gui

l = logger.Logger()

def main():
    l.info("starting")
    ui = gui.Index(l)
    ui.mainloop()
    l.info("exiting")


if __name__ == '__main__':
    main()