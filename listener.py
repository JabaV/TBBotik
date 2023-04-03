from webserver import keep_alive
import os
import vk_api
from modules import message_handler
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from modules import RKASS_module
from modules import module_send

secter = 'd9ebdf5b1a8498ec9bc3279df4d0ed8799649193e3a111a6e350d7c366b6641e798b4c555cb877dd63201'  # os.environ[
# 'token'] # не забудь заменить на token

keep_alive()
vk_session = vk_api.VkApi(token=str(secter))  #
longpoll = VkBotLongPoll(vk_session, 206394583)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            chat_id = event.object.message['peer_id']
            msg = event.object.message['text']
            if 'reply_message' in event.object.message:
                r_text = event.object.message['reply_message']['text']
                message_handler.handle_replied(msg, r_text, chat_id, vk_session)
            else:
                message_handler.handle_message(msg, chat_id, vk_session)
        if event.from_user:
            msg = event.object.message['text']
            chat_id = event.object.message['peer_id']
            uid = event.object.message['from_id']
            stscheck = RKASS_module.status_receive(uid)
            print(stscheck)
            # RKASS_module.menu(uid, vk_session)
            if msg.lower() == 'хочу проверку':
                if stscheck == 0:
                    RKASS_module.status_change(uid)
                    module_send.send('Отправьте карточку персонажа текстом', chat_id, vk_session)
                else:
                    print('123')
            if msg != ('Да' or 'Нет'):
                print(msg)
                if stscheck == 1:
                    RKASS_module.inspection_user_send(msg, uid)
                    RKASS_module.status_change(uid)
            if msg.lower() == 'список персонажей':
                RKASS_module.list_characters(uid, vk_session)

            if msg.lower().startswith("//кто автор "):
                cid = msg[12:]
                result = RKASS_module.find_author_by_id(cid)
                module_send.send(result, chat_id, vk_session)

            if msg.lower().startswith("//карточка "):
                cid = msg[11:]
                result = RKASS_module.show_character(chat_id, vk_session, cid)

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        # Обработка событий от нажатия на кнопки
        payload = event.obj.payload
        page = payload.get('page', 1)
        direction = payload.get('direction', '')

        if direction == 'prev' and page > 1:
            page -= 1
        elif direction == 'next':
            page += 1

        # Вызываем функцию list_characters с обновленным значением страницы
        RKASS_module.list_characters(uid, vk_session, page=page)

    # elif (event.type == VkBotEventType.WALL_POST_NEW) & (event.obj['post_type'] == 'post'):
