import random
import re
from modules import module_util
from modules import module_process
from modules import module_send


def HeavyFunc_Resources(text, chat_id, vk_session, replied_text=""):
    spacebar = text.find(' ')
    if spacebar > -1:
        resources = module_process.generate_resources(text[spacebar + 1:].lower())
        resources = module_process.resource_string_format(resources)
        module_send.send(resources, chat_id, vk_session)


def HeavyFunc_Ingredients(text, chat_id, vk_session, replied_text=""):
    spacebar = text.find(' ')
    if spacebar > -1:
        ingredients = module_process.generate_ingredients(text[spacebar + 1:].lower())
        ingredients = module_process.resource_string_format(ingredients)
        module_send.send(ingredients, chat_id, vk_session)


def HeavyFunc_Koobrii(text, chat_id, vk_session, replied_text=""):
    if text[7:].isdigit():
        amount = module_process.generate_koobrii(int(text[7:]))
        module_send.send('Осколки кубрия х{0}'.format(amount), chat_id, vk_session)


def Func_Counter(text, chat_id, vk_session, replied_text=""):
    if replied_text != "":
        spacebar = text.find(' ')
        if spacebar > -1:
            respond = module_util.count(replied_text, text[spacebar + 1:].lower())
            module_send.send(respond, chat_id, vk_session)


def HeavyFunc_Random(text, chat_id, vk_session, replied_text=""):
    checking = text.split(' ')
    edge = list(map(int, re.findall(r'\d+', text)))
    if (len(edge) == 1) and (len(checking) == 2):
        e1 = edge[0]
        module_send.send(
            '!Случайное число из диапазона [' + '0' + '...' + str(e1) +
            '] выпало на ' + str(random.randint(0, e1)), chat_id, vk_session)
    elif (len(edge) == 2) and (len(checking) == 3):
        e1 = edge[0]
        e2 = edge[1]
        module_send.send(
            '!Случайное число из диапазона [' + str(e1) + '...' + str(e2) +
            '] выпало на ' + str(random.randint(e1, e2)), chat_id, vk_session)
    elif (len(edge) == 3) and (len(checking) == 4):
        e1 = edge[0]
        e2 = edge[1]
        e3 = edge[2]
        if e1 > 500:
            e1 = 500
        if e2 > 500:
            e2 = 500
        if e3 > 500:
            e3 = 500
        temp = random.randint(e2, e3)
        n_sum = temp
        num_list = str(temp)
        for i in range(e1 - 1):
            temp = random.randint(e2, e3)
            n_sum += temp
            num_list += " + " + str(temp)

        module_send.send(
            '!Случайные числа из диапазона [' + str(e2) + '...' + str(e3) +
            '] выпали на (' + num_list + ') = ' + str(n_sum), chat_id, vk_session)


def Func_Kva(text, chat_id, vk_session, replied_text=""):
    module_send.kva(random.randint(1, 100), chat_id, vk_session)


def func_repost(post_id, vk_session, chat_id=2000000009):
    module_send.repost(post_id, chat_id, vk_session)


def Func_rules(param, chat_id, session, replied_text=""):
    spacebar = param.find(' ')
    if spacebar > -1:
        param = param[param.find(' ') + 1:]
        rule = module_util.getrule(param)
    else: rule = module_util.getrule('a')
    module_send.send(rule, chat_id, session)


def Func_shop(name, chat_id, session, replied_text=""):
    spacebar = name.find(' ')
    if spacebar > -1:
        name = name[name.find(' ') + 1:]
        shop, image = module_util.readshop(name)
        image = 'photo-172386457_' + image
        module_send.send_attachment(shop, chat_id, image, session)

def HeavyFunc_randomSort(text, chat_id, session, replied_text=""):
    checking = text.split(' ')
    edge = list(map(int, re.findall(r'\d+', text)))
    if (len(edge) == 2) and (len(checking) == 3):
        e1 = edge[0]
        e2 = edge[1]
        num_list = []
        for i in range(e1, e2+1):
            num_list.append(i)

        random.shuffle(num_list)
        out_list = str(num_list[0])

        for x in range(1, len(num_list)):
            out_list += ", " + str(num_list[x])

        module_send.send(
            'Случайный порядок диапазона [' + str(e1) + '...' + str(e2) +
            '] определён так: ' + out_list, chat_id, session)


commands = {
    'ква': Func_Kva,
    'ингры': HeavyFunc_Ingredients,
    'ресы': HeavyFunc_Resources,
    'рандом': HeavyFunc_Random,
    'кубрий': HeavyFunc_Koobrii,
    'счёт': Func_Counter,
    'счет': Func_Counter,
    'правила': Func_rules,
    'магазин': Func_shop,
    'порядок': HeavyFunc_randomSort
}

