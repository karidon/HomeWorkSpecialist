#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress  # подавляет исключения


class Position(object):
    def __init__(self, title, quantity, **kwargs):
        self.__Title = title  # Наименование товара
        self.__Quantity = quantity  # Колличество товара

        # Если не заданно значение
        with suppress(KeyError):  # подавляет исключение
            self.__Unit = kwargs['unit']  # Единица измерения товара
        with suppress(KeyError):
            self.__Price = kwargs['price']  # Цена товара

        try:
            # Если не указана сумма
            self.__Summa = kwargs['summa']  # Сумма товара
        except KeyError:
            try:
                # Если неуказан price
                self.__Summa = self.quantity * self.price
            except AttributeError as Exc:
                raise ValueError('Price or summa have to be specified') from Exc

    title = property(lambda self: self.__Title)
    quantity = property(lambda self: self.__Quantity)
    unit = property(lambda self: self.__Unit)
    price = property(lambda self: self.__Price)
    summa = property(lambda self: self.__Summa)
