import random
import re


def count(msg, template):
    if template == 'шизов':
        return 'Ноль \nЦелковый\nПолушка\nЧетвертушка\nОсьмушка\nПодувичок\nМедичок\nСеребрячок\nЗолотничок' \
               '\nДевятичок\nДесятичок'
    else:
        encountered = str.count(msg, template)
        return 'Найдено совпадений: {0}'.format(encountered)

