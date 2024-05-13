from webserver import keep_alive
import vk_api
from modules import module_handler
from modules import module_logger
from time import sleep
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Read tokens from the file
with open("data", "r") as data:
    contents = data.readlines()

secter = contents[0].strip()
another = contents[1].strip()

# Initialize VK sessions
vk_session = vk_api.VkApi(token=secter)
reserve = vk_api.VkApi(token=another)
current = vk_session

def listen(session):
    longpoll = VkBotLongPoll(session, 172386457)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user and event.object.message['peer_id'] in [372894745, 222366400]:
                if event.object.message['text'] == 'stfu':
                    exit()
            if event.from_chat or event.from_user:
                chat_id = event.object.message['peer_id']
                msg = event.object.message['text']
                r_text = event.object.message.get('reply_message', {}).get('text', "")
                module_handler.handle_message(msg, chat_id, session, r_text)
        elif event.type == VkBotEventType.WALL_POST_NEW and event.obj['post_type'] == 'post':
            post_id = event.obj['id']
            module_handler.handle_post(post_id, session)

while True:
    try:
        print("Starting listening")
        listen(current)
    except Exception as e:
        error_msg = str(e)
        if "Connection aborted" in error_msg:
            current = reserve if current == vk_session else vk_session
            module_logger.Log(f"Switched key to {'reserve' if current == reserve else 'main'}, now sleep")
            sleep(10)
        else:
            module_logger.Log(e)
            sleep(10)

