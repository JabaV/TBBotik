import random
import re
import vk_api
import module_send
import module_porcess
import module_player_util

def handle_message(text, chat_id, vk_session):
    if text.lower() == "ква":
        module_send.kva(random.randint(1,100), chat_id, vk_session)

    elif (text.lower() == '%команды') or (text.lower() == '%лист команд') or (text.lower() == '%список команд'):
        module_send.send('[СПИСОК КОМАНД]:\n' \
                'Ингры/Ингредиенты:\n' \
                '[обычные/редкие/эпические/мифические/легендарные/' \
                'эпик/мифик/лег]\n\n'
                'Ресы/Ресурсы (бой/босс/финал)')

    elif text.lower().startswith('кубрий'):
        if text[7:].isdigit():
            amount = module_porcess.generate_koobrii(int(text[7:]))
            module_send.send('Осколки кубрия х{0}'.format(amount), chat_id, vk_session)

    elif text.lower().startswith('ресы') or text.lower().startswith('ресурсы'):
        spacebar = text.find(' ')
        resources = module_porcess.generate_resources(text[spacebar+1:].lower())
        resources = module_porcess.resource_string_format(resources)
        module_send.send(resources, chat_id, vk_session)

    elif text.lower().startswith('ингры') or text.lower().startswith('ингредиенты'):
        spacebar = text.find(' ')
        ingredients = module_porcess.generate_ingredients(text[spacebar+1:].lower())
        ingredients = module_porcess.resource_string_format(ingredients)
        module_send.send(ingredients, chat_id, vk_session)

        # ДАЛЬШЕ ИДЁТ ОЧЕНЬ СТРАШНО
    elif text.lower().startswith("ранд"):
        edge = list(map(int, re.findall(r'\d+', text)))
        if len(edge) == 1:
            e1 = edge[0]
            module_send.send(
                '!Случайное число из диапазона [' + '0' + '...' + str(e1) +
                '] выпало на ' + str(random.randint(0, e1)), chat_id, vk_session)
        elif len(edge) == 2:
            e1 = edge[0]
            e2 = edge[1]
            module_send.send(
                '!Случайное число из диапазона [' + str(e1) + '...' + str(e2) +
                '] выпало на ' + str(random.randint(e1, e2)), chat_id, vk_session)
        elif len(edge) == 3:
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

            # дальше снова нормально


def handle_replied(text, replied_text, chat_id, vk_session):
    if text.lower().startswith('счёт') or text.lower().startswith('счет'):
        spacebar = text.find(' ')
        respond = module_player_util.count(replied_text, text[spacebar + 1:].lower())
        module_send.send(respond, chat_id, vk_session)