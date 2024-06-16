# coding: utf-8

import datetime
import config
import os

class Logger:
    def __init__(self, mode=2):
        self.config = config.Config('../conf/logger.cfg')
        self.rpath = self.config.read('path', 'root_path')
        self.mode = mode

    @property
    def __path(self):
        now_time = datetime.datetime.now()
        dir_rlist = os.listdir(self.rpath)
        if not str(now_time.year) in dir_rlist:
            os.mkdir(os.path.join(self.rpath, str(now_time.year)))
        ty_dir = os.path.join(self.rpath, str(now_time.year))
        if not str(now_time.month) in os.listdir(ty_dir):
            os.mkdir(os.path.join(self.rpath, str(now_time.year), str(now_time.month)))
        return os.path.join(self.rpath, str(now_time.year), str(now_time.month), f'{str(now_time.day)}.log')

    def __save(self, msg, end='\n'):
        with open(self.__path, mode='at', encoding='utf-8') as log:
            log.write(f'{msg}{end}')

    def debug(self, msg):
        if self.mode == 1 or self.mode == 3:
            print(f'\033[32m{datetime.datetime.now()} [DEBUG] {msg}\033[0m')

    def info(self, msg):
        now_time = datetime.datetime.now()
        if self.mode == 1 or self.mode == 3:
            print(f'{now_time} [INFO] {msg}')
        if self.mode == 2 or self.mode == 3:
            self.__save(f'{now_time} [INFO] {msg}')

    def warning(self, msg):
        now_time = datetime.datetime.now()
        if self.mode == 1 or self.mode == 3:
            print(f'\033[33m{now_time} [WARNING] {msg}\033[0m')
        if self.mode == 2 or self.mode == 3:
            self.__save(f'{now_time} [WARNING] {msg}')

    def error(self, msg):
        now_time = datetime.datetime.now()
        if self.mode == 1 or self.mode == 3:
            print(f'\033[31m{now_time} [ERROR] {msg}\033[0m')
        if self.mode == 2 or self.mode == 3:
            self.__save(f'{now_time} [ERROR] {msg}')

    def critical(self, msg):
        now_time = datetime.datetime.now()
        if self.mode == 1 or self.mode == 3:
            print(f'\033[1;31m{now_time} [CRITICAL] {msg}\033[0m')
        if self.mode == 2 or self.mode == 3:
            self.__save(f'{now_time} [CRITICAL] {msg}')


if __name__ == '__main__':
    logger = Logger(mode=3)
    logger.debug('hello')
    logger.info('hello')
    logger.warning('hello')
    logger.error('hello')
    logger.critical('hello')