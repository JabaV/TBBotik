import sqlite3
from modules import module_send
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
        stscheck = cursor.execute("SELECT sts FROM 'status' WHERE chat_id = ?", (uid,))
        stsc = stscheck.fetchone()
        if stsc[0] == 0:
            cursor.execute("UPDATE 'status' set sts = ? WHERE chat_id = ?", (1, uid))
        elif stsc[0] == 1:
            cursor.execute("UPDATE 'status' set sts = ? WHERE chat_id = ?", (0, uid))

        conn.commit()
        return stsc[0]
    except sq.Error as error:
        print('Error', error)

def status_receive(uid):
    try:
        stscheck = cursor.execute("SELECT sts FROM 'status' WHERE chat_id = ?", (uid,))
        stsc = stscheck.fetchall()
        if not stsc:
            cursor.execute("INSERT INTO 'status' ('chat_id', 'sts') VALUES (?, 1)", (uid,))
            conn.commit()
            return 1
        else:
            return stsc[0][0]
    except sq.Error as error:
        print('Error', error)

def inspection_user_send(txt, uid):
    try:
        cursor.execute("INSERT INTO 'characters' ('character', 'status', 'owner_id') VALUES (?, ?, ?)", (txt, 'Ожидание проверки', uid))
        cursor.execute("SELECT character, status FROM 'characters'")
        results = cursor.fetchall()
        conn.commit()

    except sq.Error as error:
        print('Error', error)

def list_characters(chat_id, vk_session):
    try:
        # Получаем данные персонажей из базы данных
        cursor.execute("SELECT id, character FROM 'characters'")
        results = cursor.fetchall()

        # Формируем сообщение со списком персонажей
        message = "Список персонажей:\n\n"
        for i, (id, character) in enumerate(results, start=1):
            message += "{0}】 [ID:{1}] {2}\n".format(i, id, character.split('\n')[0])

        # Отправляем сообщение пользователю
        vk_session.method('messages.send', {
            'peer_id': chat_id,
            'message': message,
            'random_id': get_random_id()
        })
    except sq.Error as error:
        print('Error', error)

def find_author_by_id(cid):
    try:
        cursor.execute("SELECT character FROM 'characters' WHERE id = ?", (cid))
        result = cursor.fetchone()
        cursor.execute("SELECT owner_id FROM 'characters' WHERE id = ?", (cid))
        usid = cursor.fetchone()
        if not result:
            return "Автор не найден"
        else:
            character = result[0].split("\n")[0]
            print(character)
            print(usid)
            vk_link = f"https://vk.com/id{usid[0]}"
            return f"Автором {character} является {vk_link}"
    except sq.Error as error:
        print("Error", error)
        return "Произошла ошибка"
    
def show_character(chat_id, vk_session, cid):
    try:
        cursor.execute("SELECT character FROM 'characters' WHERE id = ?", (cid,))
        result = cursor.fetchone()
        if not result:
            module_send.send('Персонаж не найден', chat_id, vk_session)
        else:
            character_text = result[0]
            module_send.send(character_text, chat_id, vk_session)
    
    except sq.Error as error:
        print('Error', error)