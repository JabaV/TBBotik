import sqlite3
from vk_api.keyboard import *
from vk_api.utils import get_random_id

sq = sqlite3

kbd = VkKeyboard(one_time=True)
kbd.add_button('Проверить', color=VkKeyboardColor.PRIMARY)
kbd.add_button('Нет', color=VkKeyboardColor.POSITIVE)
conn = sq.connect("modules/characters.db")
cursor = conn.cursor()


def menu(sender, vk_session):
    vk_session.method('messages.send', {
        'peer_id': sender,
        'message': 'Хотите начать проверку?',
        'random_id': get_random_id(),
        'keyboard': kbd.get_keyboard()
    })

def status_change(uid):
    try:
        cursor.execute("")

def inspection_user_send(xt, uid):
    try:

        cursor.execute("INSERT OR IGNORE INTO 'characters' ('character', 'status', 'owner_id') VALUES (?, ?, ?)",
                     (str(xt), str('Ожидание проверки'), uid))
        penis = cursor.execute("SELECT * FROM 'characters'")
        print(penis.fetchall())

        conn.commit()


    except sq.Error as error:
        print('Error', error)

    finally:
        if conn:
            conn.close()
