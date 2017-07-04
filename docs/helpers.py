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



# декоратор принимает один аргумент
def trace_value(loglevel=logging.DEBUG):
    '''

    :param loglevel: принимает уровень ошибки
    :return:
    '''

    def tracing_method(method):
        def traced_method(self, value):
            pname = method.__name__
            old = getattr(self, pname)
            msg = 'Property \'{pname}\' will be changed ' \
                  'from \'{old}\' to \'{value}\''.format(**locals())  # **locals() - все переменные
            logging.log(loglevel, msg)

            return method(self, value)

        traced_method.__name__ = method.__name__
        return traced_method

    return tracing_method


debug_value = trace_value(logging.DEBUG)
info_value = trace_value(logging.INFO)
warn_value = trace_value(logging.WARNING)