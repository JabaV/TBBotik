from webserver import keep_alive
import os
import vk_api
from modules import message_handler
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
secter = os.environ['token']

keep_alive()
vk_session = vk_api.VkApi(token=str(secter))
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


    # elif (event.type == VkBotEventType.WALL_POST_NEW) & (event.obj['post_type'] == 'post'):
