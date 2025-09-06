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
        'Ткань х': random.randint(0, 2),
        'Железо х': random.randint(0, 2),
        'Дерево х': random.randint(0, 3),
        'Кожа Хиджакуры х': random.randint(0, 2),
        'Кварц х': random.randint(0, 2),
        'Медь х': random.randint(0, 2),
        'Пламенный кристалл х': random.randint(-2, 1),
        'Бальдар х': random.randint(-1, 1),
        'Рубинит х': random.randint(-1, 1)
    }
    return res


def generate_boss():
    res = {
        'Ткань х': random.randint(1, 5),
        'Железо х': random.randint(1, 4),
        'Дерево х': random.randint(1, 6),
        'Пламенный кристалл х': random.randint(-1, 2),
        'Йельский патник х': random.randint(0, 2),
        'Дозер х': random.randint(0, 2),
        'Итодол х': random.randint(0, 3),
        'Ланк х': random.randint(0, 2),
        'Тёмная частица x': random.randint(0, 1),
        'Рунный камень х': random.randint(-1, 1)
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
    match rarity:
        case 'обычные':
            ingredients = generate_usual()
        case 'редкие' | 'рар':
            ingredients = generate_rare()
        case 'эпик':
            ingredients = generate_epic()
        case 'миф' | 'мифик':
            ingredients = generate_mythic()
        case 'лег':
            ingredients = generate_legendary()
    if ingredients != '':
        return ingredients
    else:
        return 'null'


def generate_usual():

    done = False

    while not done:
        res = {
            'Вырванный глаз х': random.randint(-2, 2),
            'Клык волка х': random.randint(-2, 2),
            'Жаба х': random.randint(-2, 2),
            'Сушёные грибы х': random.randint(-2, 2),
            'Пряности х': random.randint(-2, 2),
            'Вода из горячих источников х': random.randint(-2, 2)
        }

        for i in res.keys():
            if res[i] > 0:
                done = True
                break

    return res


def generate_rare():

    done = False

    while not done:
        res = {
            'Огнецвет х': random.randint(0, 2),
            'Сера х': random.randint(-2, 3),
            'Серный концентрат х': random.randint(-2, 2),
            'Красная воронка х': random.randint(-2, 2),
            'Засохший мох х': random.randint(-2, 2),
            'Красный кристалл х': random.randint(-2, 1),
            'Волос с подмыхи гиганта х': random.randint(-2, 2)
        }

        for i in res.keys():
            if res[i] > 0:
                done = True
                break

    return res


def generate_epic():

    done = False
    while not done:

        res = {
            'Лунный свет х': random.randint(-2, 1),
            'Солнечный свет х': random.randint(-2, 2),
            'Кровь виверны х': random.randint(-1, 1),
            'Кристалльная кровь х': random.randint(-2, 2),
            'Вода из волшебного колодца х': random.randint(-4, 2),
            'Сок живого дерева х': random.randint(-3, 2),
            'СтРаННый ГРиБ х': random.randint(-2, 2),
            'Чёрная роза х': random.randint(-1, 3)
        }

        for i in res.keys():
            if res[i] > 0:
                done = True
                break
    return res


def generate_mythic():
    res = {
        'Слюна горного пиздюля х': random.randint(-1, 1),
        'Пузырёк магмы х': random.randint(0, 2),
        'Пещерный корень х': random.randint(-1, 2)
    }
    return res


def generate_legendary():
    res = {'Огневишня х': 0, 'Волчий глаз х': 0}
    chance = random.randint(1, 2)
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

