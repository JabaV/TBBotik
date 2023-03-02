import random


def generate_resources(difficulty):
    resource = ''
    match difficulty:
        case 'бой':
            resource = generate_fight()
        case 'босс':
            resource = generate_boss()
        case 'финал':
            resource = generate_final()
    if resource != '':
        return resource
    else:
        return 'Ошибка в написании сложности'


def generate_fight():
    res = {
        'Ткань х': random.randint(0, 3),
        'Железо х': random.randint(0, 4),
        'Дерево х': random.randint(0, 5),
        'Кожа Хиджакуры х': random.randint(0, 4),
        'Кварц х': random.randint(0, 4),
        'Медь х': random.randint(0, 3),
        'Пламенный кристалл х': random.randint(0, 2),
        'Бальдар х': random.randint(0, 2),
        'Рубинит х': random.randint(0, 2),
    }
    return  res


def generate_boss():
    res = {
        'Ткань х': random.randint(1, 5),
        'Железо х': random.randint(1, 4),
        'Дерево х': random.randint(1, 6),
        'Пламенный кристалл х': random.randint(0, 2),
        'Йельский патник х': random.randint(0, 2),
        'Итодол х': random.randint(0, 3),
        'Ланк х': random.randint(1, 4)
    }
    return res


def generate_final():
    res = {
        'Пламенный кристалл х': random.randint(1, 3),
        'Йельский патник х': random.randint(1, 3),
        'Итодол х': random.randint(1, 3),
        'Ланк х': random.randint(1, 4),
        'Аделит x': random.randint(1, 2),
        'Рунный камень х': random.randint(0, 2),
        'Тёмная сталь х': random.randint(-1, 1)
    }
    return res


def resource_string_format(res):
    s = ''
    for x in res:
        if res[x] > 0:
            s += str(x) + str(res[x]) + '\n'
    if s == '':
        return 'Ничего не выпало'
    else:
        return s


def generate_ingredients(rarity):
    ingredients = ''


def generate_usual():
    res = {
        'Вырванный глаз х': random.randint(1, 6),
        'Клык волка х': random.randint(1, 6),
        'Жаба х': random.randint(1, 6),
        'Сушёные грибы х': random.randint(0, 2),
        'Пряности х': random.randint(1, 4)
    }
    return res


def generate_rare():
    res = {
        'Огнецвет х': random.randint(1, 3),
        'Сера х': random.randint(1, 4),
        'Серный концентрат х': random.randint(0, 4)
    }
    return res


def generate_epic():
    res = {
        'Лунный свет х': random.randint(0, 2),
        'Солнечный свет х': random.randint(0, 2),
        'Кровь виверны х': random.randint(0, 1),
        'Кристалльная кровь х': random.randint(0, 2),
        'Вода из волшебного колодца х': random.randint(0, 2),
        'Сок живого дерева х': random.randint(0, 2),
        'СтРаННый ГРиБ х': random.randint(0, 5),
        'Чёрная роза х': random.randint(0, 3)
    }
    return res


def generate_mythic():
    res = {
        'Слюна горного козла х': random.randint(0, 1),
        'Пузырёк магмы х': random.randint(0, 2),
        'Пещерный корень х': random.randint(0, 2)
    }
    return res


def generate_legendary():
    res = {'Огневишня х': 0, 'Волчий глаз х': 0}
    chance = random.randint(1, 4)
    if (chance == 1):
        ing = random.randint(0, 1)
        if ing == 0:
            res['Огневишня х'] = 1
        else:
            res['Волчий глаз х'] = 1
    return res


def generate_koobrii(c):
    res = 0
    for _ in range(c):
        if 1 <= random.randint(1, 100) <= 15:
            res += 1
    return res
