import asyncio
import random

from module_data_access import grbq, gibq, grbqr, gra

rr = random.randint


# TODO: resources random by rarity, boss random uses choose and random shift in scales
async def generate_resources(difficulty: str) -> str:
    resource = ''
    resource = ''
    match difficulty:
        case 'бой':
            task_gen = asyncio.create_task(generate_fight())
            resource = await task_gen
        case 'босс':
            resource = generate_boss()
        case 'финал':
            resource = generate_final()
    if resource != '':
        return resource
    else:
        return 'Ошибка в написании сложности'


async def generate_fight() -> dict:
    task_get = asyncio.create_task(grbq(1))
    task_get2 = asyncio.create_task(grbq(2))
    res = {}
    temp = await task_get
    temp2 = await task_get2
    temp = temp + temp2
    for r in temp:
        res[r[0] + ' x'] = rr(r[2] + rr(-1, 1), r[3] + rr(-1, 1))
    return res


async def generate_boss() -> dict:
    task_get = asyncio.create_task(grbqr(5))
    res = {}
    rr = random.randint
    temp = await task_get
    while len(temp) > 9:
        temp.remove(random.choice(temp))
    for r in temp:
        res[r[0] + ' x'] = rr(r[2] + 1, r[3] + rr(-1, 1))
    return res


async def generate_final() -> dict:
    task_get = asyncio.create_task(grbq(5))
    task_get2 = asyncio.create_task(grbq(4))
    task_get3 = asyncio.create_task(grbq(3))
    res = {}
    temp = await task_get
    temp2 = await task_get2
    temp3 = await task_get3
    temp2 = temp2 + temp3
    while len(temp2) > 6:
        temp.remove(random.choice(temp))
    for r in temp2:
        res[r[0] + ' x'] = rr(r[2] + 1, r[3] + rr(-1, 1))
    a = random.choice(temp)
    res[a[0] + ' x'] = rr(a[2], a[3])
    return res


async def resource_string_format(res) -> str:
    s = ''
    for x in res:
        if x == 'Казионит x':
            del res[x]
        if res[x] > 0:
            s += str(x) + str(res[x]) + '\n'
    if s == '':
        return 'Ничего не выпало'
    else:
        return s


async def generate_ingredients(rarity):
    ingredients = ''
    match rarity:
        case 'обычные':
            ingredients = generate_usual()
        case 'редкие':
            ingredients = generate_rare()
        case 'эпик':
            ingredients = generate_epic()
        case 'мифик':
            ingredients = generate_mythic()
        case 'миф':
            ingredients = generate_mythic()
        case 'лег':
            ingredients = generate_legendary()
    if ingredients != '':
        return ingredients
    else:
        return 'null'


async def generate_usual() -> dict:
    task_get = asyncio.create_task(gibq(1))
    res = {}
    temp = await task_get
    for i in temp:
        res[i[0] + ' x'] = rr(1 + rr(-1, 1), 4 + rr(-1, 1))
    return res


async def generate_rare() -> dict:
    task_get = asyncio.create_task(gibq(2))
    res = {}
    temp = await task_get
    for i in temp:
        res[i[0] + ' x'] = rr(1 + rr(-1, 1), 3 + rr(-1, 1))
    return res


async def generate_epic() -> dict:
    task_get = asyncio.create_task(gibq(3))
    res = {}
    temp = await task_get
    for i in temp:
        res[i[0] + ' x'] = rr(1 + rr(-1, 1), 3 + rr(-1, 1))
    return res


async def generate_mythic() -> dict:
    task_get = asyncio.create_task(gibq(4))
    res = {}
    temp = await task_get
    for i in temp:
        res[i[0] + ' x'] = rr(1 + rr(-1, 1), 2 + rr(-1, 1))
    return res


async def generate_legendary() -> dict:
    task_get = asyncio.create_task(gibq(5))
    res = {}
    temp = await task_get
    chance = rr(1, 2)
    if chance == 1:
        res[random.choice(temp)[0] + ' x'] = 1
    return res


async def generate_koobrii(c: int) -> int:
    res = 0
    for _ in range(c):
        if 1 <= rr(1, 100) <= 15:
            res += 1
    return res



