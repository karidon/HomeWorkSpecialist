#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

def value_not_none(method):
    def checked_method(self, value):  # не имеет значение это перменная
        if value is None:
            raise ValueError('\'None\' is not allowed for property value')
        return method(self, value)

    checked_method.__name__ = method.__name__
    return checked_method




# Значение свойство такогота будет измено на значение такоето
# и что это ifo, error , warning
# logging.log(logging.debug, text)


# 1.10


def loging_war(method):
    def checked_method(self, value):
        logging.log(1, )