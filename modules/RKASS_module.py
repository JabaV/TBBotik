import sqlite3
from vk_api.keyboard import *
from vk_api.utils import get_random_id

sq = sqlite3

kbd = VkKeyboard(one_time=True)
kbd.add_button('Да', color=VkKeyboardColor.PRIMARY)
kbd.add_button('Нет', color=VkKeyboardColor.POSITIVE)
conn = sq.connect("modules/characters.db")
cursor = conn.cursor()


def menu(chat_id, vk_session):
    vk_session.method('messages.send', {
        'peer_id': chat_id,
        'message': 'Хотите начать проверку?',
        'random_id': get_random_id(),
        'keyboard': kbd.get_keyboard()
    })

def status_change(uid):
    try:
        stscheck = cursor.execute("SELECT sts FROM 'status' WHERE chat_id = uid")
        if stscheck == 0:
            cursor.execute("UPDATE sts FROM 'status' WHERE chat_id = uid VALUES (1)")
        elif stscheck == 1:
            cursor.execute("UPDATE sts FROM 'status' WHERE chat_id = uid VALUES (0)")

        conn.commit()
        return stscheck
    except sq.Error as error:
        print('Error', error)
    finally:
        if conn:
            conn.close()

def status_receive(uid):
    stscheck = cursor.execute("SELECT sts FROM 'status' WHERE chat_id = uid")
    if stscheck == None:
        cursor.execute("INSERT INTO 'status' ('chat_id', 'sts') VALUES (?, 1)", uid)
        stscheck = cursor.execute("SELECT sts FROM 'status' WHERE chat_id = uid")
    conn.commit()
    return stscheck

def inspection_user_send(txt):
    try:
        cursor.execute("INSERT OR IGNORE INTO 'characters' ('character', 'status') VALUES (?, ?)",
                     (str(txt), str('Ожидание проверки')))
        penis = cursor.execute("SELECT * FROM 'characters'")
        print(penis.fetchall())

        conn.commit()


    except sq.Error as error:
        print('Error', error)

    finally:
        if conn:
            conn.close()
