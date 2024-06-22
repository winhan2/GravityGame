# coding: utf-8

import config

con = config.Config('../conf/mass.cfg')

class Weight:
    def __init__(self, x, y, wtype):
        self.x: int = x
        self.y: int = y
        self.wtype = wtype
        if wtype == 's':
            self.mass: int = int(con.read('small_mass', 'mass'))
        elif wtype == 'b':
            self.mass: int = int(con.read('big_mass', 'mass'))


class WeightGravity:
    def __init__(self):
        self.__weights: [Weight, ...] = []

    def add_weight_gravity(self, weight_gravity):
        self.__weights.append(weight_gravity)

    def get_weight_gravity(self, mode='a'):
        """
        :param mode:
        a: all gravity
        s: small gravity
        b: big gravity

        xm x, m: a weight gravity
        :return: weights gravity
        """
        if mode == 'a':
            return [i.x * i.y for i in self.__weights]
        elif mode == 's':
            return [i.x * i.y for i in self.__weights if i.wtype == 's']
        elif mode == 'b':
            return [i.x * i.y for i in self.__weights if i.wtype == 'b']
        elif 'xm' in mode:
            x, m = mode[3:].split(',')
            x = int(x)
            m = int(m)
            return x * m


if __name__ == '__main__':
    w = Weight(1, 2, 's')
    wg = WeightGravity()
    wg.add_weight_gravity(w)
    print(wg.get_weight_gravity('xm 1,1'))