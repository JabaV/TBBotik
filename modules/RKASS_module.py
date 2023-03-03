import sqlite3
from vk_api.keyboard import *
from vk_api.utils import get_random_id

sq = sqlite3

kbd = VkKeyboard(one_time=True)
kbd.add_button('Проверить', color=VkKeyboardColor.PRIMARY)
kbd.add_button('Нет', color=VkKeyboardColor.POSITIVE)


def menu(sender, vk_session):
    vk_session.method('messages.send', {
        'peer_id': sender,
        'message': 'Хотите начать проверку?',
        'random_id': get_random_id(),
        'keyboard': kbd.get_keyboard()
    })


def inspection_user_send(self, xt, uid):
    try:
        self.conn = sq.connect("characters.db")
        self.cursor = self.conn.cursor()

        self.execute("INSERT OR IGNORE INTO 'characters' ('character', 'status', 'owner_id') VALUES (?, ?, ?)",
                     (str(xt), str('Ожидание проверки'), uid))
        penis = self.cursor.execute("SELECT * FROM 'characters'")
        print(penis.fetchall())

        self.conn.commit()

    except sq.Error as error:
        print('Error', error)

    finally:
        if self.conn:
            self.conn.close()
