def count(msg, template):
    if template == 'шизов':
        return 'Ноль \nЦелковый\nПолушка\nЧетвертушка\nОсьмушка\nПодувичок\nМедичок\nСеребрячок\nЗолотничок' \
               '\nДевятичок\nДесятичок'
    else:
        encountered = str.count(msg, template)
        return 'Найдено совпадений: {0}'.format(encountered)


def readshop(name):
    name = name.lower()
    string = 'Не существует'
    image = ''
    match (name):
        case 'лавка':
            with open('Files/stall.txt', 'r', encoding='utf-8') as shop:
                string = shop.read()
            with open('Files/stall_image.txt', 'r', encoding='utf-8') as shop:
                image = shop.read()
    return string, image


def readrules(line):
    respond = ''
    with open('Files/Rules.txt', 'r', encoding='utf-8') as Rule:
        for _ in range(line):
            respond = Rule.readline()
    return respond


def getrule(param):
    respond = ''
    param = param.lower()
    match (param):
        case 'общие':
            respond = readrules(2)
        case 'глоссарий'|'глоссария':
            respond = readrules(3)
        case 'персов'|'классов'|'классы':
            respond = readrules(4)
        case 'рангов'|'ранги':
            respond = readrules(5)
        case 'общения'|'флуда'|'флуд':
            respond = readrules(6)
        case 'магазина'|'магазин':
            respond = readrules(7)
        case 'вещей'|'итемов'|'итемы'|'вещи':
            respond = readrules(8)
        case 'рынка'|'рынок'|'базар'|'базара':
            respond = readrules(9)
        case 'рейдов'|'рейды'|'рейд'|'данж'|'данжи'|'данжей':
            respond = readrules(10)
        case 'лора'|'лор':
            respond = readrules(11)
        case 'зелий'|'зельеварения'|'зелья':
            respond = readrules(12)
        case 'пвп'|'кодекс'|'кодекс чести':
	        respond = readrules(14)
        case _:
            respond = readrules(1)
    return respond