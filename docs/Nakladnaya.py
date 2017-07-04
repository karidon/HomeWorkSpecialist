#!/usr/bin/python3
# -*- coding: utf-8 -*-


import logging
import helpers as hlp

from datetime import datetime
from Position import Position


class Nakladnaya(object):
    def __init__(self):
        self.__Created = datetime.now()
        self.__Positions = []

    @property  # свойство
    def number(self):
        '''Number nakladnaya'''
        return self.__Number

    @number.setter
    @hlp.info_value
    @hlp.value_not_none
    def number(self, value):
        '''Изменение номера накладной'''
        self.__Number = value

    @number.deleter
    def number(self):
        logging.info('Number {0} deleted'.format(self.number))
        del self.__Number

    address = property(lambda self: self.__Addreess)  # Адресс доставки

    @address.setter
    @hlp.warn_value
    @hlp.value_not_none
    def address(self, value):
        '''Изменения адреса'''
        logging.warning('Address changed')

    responser = property(lambda self: self.__Responser)

    @responser.setter
    @hlp.trace_value(logging.ERROR - 1)
    @hlp.value_not_none
    def responser(self, value):
        '''Исполнитель'''
        self.__Responser = value

    @responser.deleter
    @hlp.info_value
    @hlp.value_not_none
    def responser(self, value):
        '''Изменения исполнителя'''
        self.__Responser = value

    def append(self, *args, **kwargs):
        '''Добоволяем позицию'''
        if isinstance(args[0], Position):   #TODO 1: Надо разобраться
            P = args[0]
        else:
            P = Position(*args, **kwargs)
        self.__Positions.append(P)
