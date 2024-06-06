import asyncio
import random
import re
from modules import module_util
from modules import module_process
from modules import module_send


async def HeavyFunc_Resources(text, chat_id: int, vk_session, replied_text=''):
    spb = text.frind(' ')
    if spb > -1:
        resources = module_process.generate_resources(text[spb+1:].lower())
        resources = module_process.resource_string_format(resources)
        task_send = asyncio.create_task(module_send.send(resources, chat_id, vk_session))
        await task_send


async def HeavyFunc_Ingredients(text, chat_id, vk_session, replied_text=""):
    spacebar = text.find(' ')
    if spacebar > -1:
        ingredients = module_process.generate_ingredients(text[spacebar + 1:].lower())
        ingredients = module_process.resource_string_format(ingredients)
        task_send = asyncio.create_task(module_send.send(ingredients, chat_id, vk_session))
        await task_send


async def HeavyFunc_Koobrii(text, chat_id, vk_session, replied_text=""):
    if text[7:].isdigit():
        amount = module_process.generate_koobrii(int(text[7:]))
        task_send = asyncio.create_task(module_send.send('Осколки кубрия х{0}'.format(amount), chat_id, vk_session))
        await task_send


async def func_finder(text, chat_id, vk_session, replied_text=""):
    if replied_text != "":
        spacebar = text.find(' ')
        if spacebar > -1:
            respond = module_util.count(replied_text, text[spacebar + 1:].lower())
            task_send = asyncio.create_task(module_send.send(respond, chat_id, vk_session))
            await task_send


async def HeavyFunc_Random(text, chat_id, session, replied_text=''):
    check = text.split(' ')
    edge = list(map(int, re.findall(r'\d+', text)))
    match (len(check)):
        case 2:
            task_send = asyncio.create_task(module_send.send(f'!Случайное число из диапазона [0...{str(edge[0])} выпало'
                                                             f' на {str(random.randint(0, edge[0]))}', chat_id, session))
            await task_send
        case 3:
            task_send = asyncio.create_task(module_send.send(f'!Случайное число из диапазона [{str(edge[0])}...{str(edge[1])}]'
                                                             f' выпало на {str(random.randint(edge[0], edge[1]))}', chat_id,
                                                             session))
            await task_send
        case 4:
            n_sum = 0
            num_list = str(random.randint(edge[1], edge[2]))
            for _ in edge:
                if _ > 500:
                    _ = 500
            for _ in edge:
                temp = random.randint(edge[1], edge[2])
                n_sum += temp
                num_list = ' + ' + str(temp)
            task_send = asyncio.create_task(module_send.send(f'!Случайные числа из диапазона [{str(edge[1])}'
                                                             f'...{str(edge[2])}]'
                                                             f' выпали на ({num_list}) = {str(n_sum)}', chat_id,
                                                             session))
            await task_send


async def func_kva(text, chat_id, session, replied_text=''):
    task = asyncio.create_task(module_send.send(random.randint(1, 100), chat_id, session))
    await task


async def func_repost(post_id, session, chat_id=2000000009):
    task = asyncio.create_task(module_send.repost(post_id, session, chat_id))


async def func_rules(param, chat_id, session, replied_text=''):
    spb = param.find(' ')
    if spb > -1:
        param = param[param.find(' ') + 1:]
        task = asyncio.create_task(module_util.getrule(param))
        rule = await task
    else:
        task = asyncio.create_task(module_util.getrule('a'))
        rule = await task
    task = asyncio.create_task(module_send.send(rule, chat_id, session))
    await task


async def func_shop(text, chat_id, session, replied_text=''):
    spb = text.find(' ')
    if spb > -1:
        name = text[text.find(' ') + 1:]
        task = asyncio.create_task(module_util.readshop(name))
        shop, image = await task
        image = 'photo-172386457_' + image
        task = asyncio.create_task(module_send.send_attachment(shop, chat_id, image, session))
        await task


commands = {
    'ква': func_kva,
    'ингры': HeavyFunc_Ingredients,
    'ресы': HeavyFunc_Resources,
    'рандом': HeavyFunc_Random,
    'кубрий': HeavyFunc_Koobrii,
    'счёт': func_finder,
    'счет': func_finder,
    'правила': func_rules,
    'магазин': func_shop
}


