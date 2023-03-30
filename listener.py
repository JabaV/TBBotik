from webserver import keep_alive
import os
import vk_api
from modules import message_handler
from modules import module_logger
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
secter = os.environ['token']

keep_alive()
vk_session = vk_api.VkApi(token=str(secter))
longpoll = VkBotLongPoll(vk_session, 206394583)
vk = vk_session.get_api()

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    chat_id = event.object.message['peer_id']
                    msg = event.object.message['text']
                    
                    r_text = event.object.message['reply_message']['text']
                    message_handler.handle_message(msg, chat_id, vk_session, r_text)
            # elif (event.type == VkBotEventType.WALL_POST_NEW) & (event.obj['post_type'] == 'post'):
    except Exception as e:
        module_logger.Log(e)
