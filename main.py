from webserver import keep_alive
import random
import os
import re
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
secter = os.environ['token']

keep_alive()
vk_session = vk_api.VkApi(token= str(secter))
longpoll = VkBotLongPoll(vk_session, 206394583)
vk = vk_session.get_api()

flag = True


def send(text, chid):
  vk_session.method('messages.send', {
    'peer_id': chid,
    'message': text,
    'random_id': get_random_id()
  })


def kva(chid):
  c = random.randint(1, 100)
  if c != 1:
    txt = 'Ква'
    attch = ''
  else:
    txt = 'Джекпот'
    attch = 'audio474499147_456517029'
  vk_session.method(
    'messages.send', {
      'peer_id': chid,
      'message': txt,
      'random_id': get_random_id(),
      'attachment': attch
    })


for event in longpoll.listen():
  if event.type == VkBotEventType.MESSAGE_NEW:
    if event.from_chat:
      chid = event.object.message['peer_id']
      msg = event.object.message['text']
      if msg.lower() == 'ква':
        kva(chid)
      if msg.lower() == '%команды' or msg.lower(
      ) == '%лист команд' or msg.lower() == '%список команд':
        text = '[СПИСОК КОМАНД]:\n' \
               'Ингры/Ингредиенты:\n' \
               '[обычные/редкие/эпические/мифические/легендарные]\n' \
               '[эпик/мифик/лег]\n'
        send(text, chid)
      """if msg.lower().startswith('титан'):
        c = 6
        amount = msg[c:]
        temp = 0
        res = 0
        s = ''
        if amount.isdigit():
          amount = int(amount)
          for _ in range(amount):
            temp = random.randint(1, 100)
            if 1 <= temp <= 15:
              res += 1
          if res == 0:
            send('Ничего не выпало.', chid)
          else:
            s = 'Осколок Титанита x' + str(res)
          send(s, chid)
      if msg.lower().startswith('титанит'):
        c = 8
        amount = msg[c:]
        temp = 0
        res = 0
        s = ''
        if amount.isdigit():
          amount = int(amount)
          for _ in range(amount):
            temp = random.randint(1, 100)
            if 1 <= temp <= 15:
              res += 1
          if res == 0:
            send('Ничего не выпало.', chid)
          else:
            s = 'Осколок Титанита x' + str(res)
          send(s, chid)
      if msg.lower().startswith('ресурсы') or msg.lower().startswith(
          'ресы'):  # Главная логика бота.Генератор Ресурсов.
        res = {}
        if msg.lower().startswith('ресурсы'):
          c = 8
        elif msg.lower().startswith('ресы'):
          c = 5
          difficult = msg[
            c:]  # Аргумент генератора."Сложность" сделанная в качестве разных аргументов для
          # генерации.
          if difficult == "бой":
            res = {
              'Ткань х': random.randint(1, 6),
              'Железо х': random.randint(1, 8),
              'Дерево х': random.randint(1, 6),
              'Обычные осколки х': random.randint(1, 4),
              'Редкие осколки х': random.randint(1, 4)
            }
            s = ''
            for x in res:
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            send(s, chid)
          if difficult == 'босс':
            if random.randint(1, 100) <= 15:
              a = 1
            else:
              a = 0
            res = {
              'Ткань х': random.randint(1, 7),
              'Железо х': random.randint(1, 12),
              'Дерево х': random.randint(1, 9),
              'Тёмная ткань х': random.randint(0, 6),
              'Сжиженная биомасса х': random.randint(0, 3),
              'Очень редкие осколки х': random.randint(1, 4),
              'Эпические осколки х': random.randint(0, 4),
              'Чертёж Крафтовой Рунической Матрицы х': a
            }
            s = ''
            for x in res:
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            send(s, chid)
          if difficult == 'финал':
            if random.randint(1, 5) == 1:
              a = 1
            else:
              a = 0
            res = {
              'Ткань х': random.randint(1, 14),
              'Железо х': random.randint(1, 17),
              'Дерево х': random.randint(1, 12),
              'Тёмная ткань х': random.randint(2, 7),
              'Сжиженная биомасса х': random.randint(1, 3),
              'Эпические осколки х': random.randint(0, 6),
              'Мифические осколки х': random.randint(0, 2),
              'Легендарные осколки х': random.randint(0, 1),
              'Чертёж Великой Рунической Матрицы x': a
            }
            s = ''
            for x in res:
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            send(s, chid)"""

      if msg.lower().startswith('ингредиенты') or msg.lower().startswith(
          'ингры'):
        res = {}
        if msg.lower().startswith('ингредиенты'):
          c = 12
        elif msg.lower().startswith('ингры'):
          c = 6
          rarity = msg[c:]
          if rarity == "обычные":
            res = {
              'Вырванный глаз х': random.randint(1, 6),
              'Клык волка х': random.randint(1, 6),
              'Жаба х': random.randint(1, 6),
              'Сушёные грибы х': random.randint(0, 2),
              'Пряности х': random.randint(1, 4)
            }
            s = ''
            for x in res:
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            if s == '':
              send('[ВАМ НЕ ПОВЕЗЛО.]', chid)
            else:
              send(s, chid)

          if rarity == 'редкие':
            res = {
              'Огнецвет х': random.randint(1, 5),
              'Серный концентрат х': random.randint(0, 4)
            }
            s = ''
            for x in res:
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            if s == '':
              send('[ВАМ НЕ ПОВЕЗЛО.]', chid)
            else:
              send(s, chid)

          if rarity == 'эпические' or rarity == "эпик":
            res = {
              'Лунный свет х': random.randint(0, 2),
              'Солнечный свет х': random.randint(0, 2),
              'Кровь виверны х': random.randint(0, 1),
              'Кристалльная кровь х': random.randint(0, 2),
              'Вода из волшебного колодца х': random.randint(0, 2),
              'Сок живого дерева х': random.randint(0, 2),
              'СтРаННый ГРиБ х': random.randint(1, 4),
              'Чёрная роза х': random.randint(0, 3)
            }
            s = ''
            for x in res:
              ch = random.randint(1, 2)
              if ch == 1:
                res[x] = 0
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            if s == '':
              send('[ВАМ НЕ ПОВЕЗЛО]', chid)
            else:
              send(s, chid)

          if rarity == 'мифические' or rarity == "мифик":
            res = {
              'Слюна горного козла х': random.randint(0, 1),
              'Пузырёк магмы х': random.randint(0, 2),
              'Пещерный корень х': random.randint(0, 2)
            }
            s = ''
            for x in res:
              ch = random.randint(1, 2)
              if x == 'Слюна горного козла х':
                ch = random.randint(1, 4)
                if ch != 4:
                  res[x] = 0
              if ch == 1:
                res[x] = 0
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            if s == '':
              send('[ВАМ НЕ ПОВЕЗЛО.]', chid)
            else:
              send(s, chid)

          if rarity == "легендарные" or rarity == "лег":
            res = {'Огневишня х': 0, 'Волчий глаз х': 0}
            s = ''
            for x in res:
              ing = random.randint(0, 1)
              if ing == 0:
                res['Огневишня х'] = 1
              else:
                res['Волчий глаз х'] = 1
              if res[x] != 0:
                s += str(x) + str(res[x]) + "\n"
            if s == '':
              send('[ВАМ НЕ ПОВЕЗЛО.]', chid)
            else:
              send(s, chid)
      if msg.lower().startswith("ранд"):
        edge = list(map(int, re.findall(r'\d+', msg)))
        if len(edge) == 1:
          e1 = edge[0]
          send(
            '!Случайное число из диапазона [' + '0' + '...' + str(e1) +
            '] выпало на ' + str(random.randint(0, e1)), chid)
        elif len(edge) == 2:
          e1 = edge[0]
          e2 = edge[1]
          send(
            '!Случайное число из диапазона [' + str(e1) + '...' + str(e2) +
            '] выпало на ' + str(random.randint(e1, e2)), chid)
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

          send(
            '!Случайные числа из диапазона [' + str(e2) + '...' + str(e3) +
            '] выпали на (' + num_list + ') = ' + str(n_sum), chid)

      if msg.lower().startswith('счёт') or msg.lower().startswith('счет'):
        if 'reply_message' in event.object.message:
          txt = event.object.message['reply_message']['text']
          find = msg[5:]
          if find.lower() == 'шизов':
            send(
              'Ноль \nЦелковый\nПолушка\nЧетвертушка\nОсьмушка\nПодувичок\nМедичок\n'
              'Серебрячок\nЗолотничок\nДевятичок\nДесятичок', chid)
          else:
            haha = str.count(txt, find)
            send('Найдено совпадений: {0}'.format(haha), chid)