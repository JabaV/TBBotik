from webserver import keep_alive
import vk_api
from modules import module_handler
from modules import module_logger
from time import sleep
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

data = open("data", "r")
print("File opened")
contents = data.readlines()
data.close()
print("Closed")

secter = contents[0].strip('\n')
another = contents[1].strip('\n')

# keep_alive()

vk_session = vk_api.VkApi(token=str(secter))
reserve = vk_api.VkApi(token=str(another))

current = vk_session


def listen(session):
    longpoll = VkBotLongPoll(session, 172386457)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat or event.from_user:
                chat_id = event.object.message['peer_id']
                msg = event.object.message['text']
                r_text = ""
                if 'reply_message' in event.object.message:
                    r_text = event.object.message['reply_message']['text']
                module_handler.handle_message(msg, chat_id, session, r_text)
        elif (event.type == VkBotEventType.WALL_POST_NEW) & (event.obj['post_type'] == 'post'):
            post_id = event.obj['id']
            module_handler.handle_post(post_id, session)


while True:
    try:
        print("Starting listening")
        listen(current)
    except Exception as e:
        if str(e).__contains__("Connection aborted"):
            if current == vk_session:
                current = reserve
                module_logger.Log("Switched key to reserve, now sleep")
                sleep(10)
            else:
                current = vk_session
                module_logger.Log("Switched key to main, now sleep")
                sleep(10)
        else:
            module_logger.Log(e)
            sleep(10)
