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
            print(str(respond))
    return respond


def getrule(param):
    respond = ''
    param = param.lower()
    match (param):
        case 'общие':
            respond = readrules(2)
        case 'глоссарий':
            respond = readrules(3)
        case 'персов':
            respond = readrules(4)
        case 'рангов':
            respond = readrules(5)
        case 'общения':
            respond = readrules(6)
        case 'магазина':
            respond = readrules(7)
        case 'вещей':
            respond = readrules(8)
        case 'рынка':
            respond = readrules(9)
        case 'рейдов':
            respond = readrules(10)
        case 'лора':
            respond = readrules(11)
        case 'зелий':
            respond = readrules(12)
        case _:
            respond = readrules(1)
    return respond
