#!/usr/bin/python3
# -*- coding: utf-8 -*-


import logging

from datetime import datetime


class Nakladnaya(object):

    def __init__(self):
        self.__Created = datetime.now()


    @property                   #свойство
    def number(self):
        '''Number nakladnaya'''
        return self.__Number

    @number.setter
    def number(self, value):
        '''Изменение номера накладной'''
        if value  is None:
            raise ValueError('None is not allowed for property value')
        logging.info('Number changed from {0} to {1}'.format(self.number, value))       # запись в логи
        self.__Number = value

    @number.deleter
    def number(self):
        logging.info('Number {0} deleted'.format(self.number))
        del self.__Number

        # 0.38