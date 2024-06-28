# coding: utf-8

import config

con = config.Config('../conf/mass.cfg')
big_mass = int(con.read('big_mass', 'mass'))
small_mass = int(con.read('small_mass', 'mass'))

def calc(x, mtype):
    if mtype == 'small':
        return x * small_mass
    elif mtype == 'big':
        return x * big_mass