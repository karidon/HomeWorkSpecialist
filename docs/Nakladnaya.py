#!/usr/bin/python3
# -*- coding: utf-8 -*-


import logging
import helpers as hlp

from datetime import datetime


class Nakladnaya(object):
    def __init__(self):
        self.__Created = datetime.now()

    @property  # свойство
    def number(self):
        '''Number nakladnaya'''
        return self.__Number

    @number.setter
    @hlp.value_not_none
    def number(self, value):
        '''Изменение номера накладной'''
        logging.info('Number changed from {0} to {1}'.format(self.number, value))  # запись в логи
        self.__Number = value

    @number.deleter
    def number(self):
        logging.info('Number {0} deleted'.format(self.number))
        del self.__Number

    address = property(lambda self: self.__Addreess)  # Адресс доставки

    @address.setter
    @hlp.value_not_none
    def address(self, value):
        '''Изменения адреса'''
        logging.warning('Address changed')

    @property
    def responser(self):
        '''Исполнитель'''
        return self.__Responser

    @responser.setter
    @hlp.value_not_none
    def responser(self, value):
        '''Изменения исполнителя'''
        logging.info('Number changed from {0} to {1}'.format(self.responser, value))  # запись в логи
        self.__Responser = value
