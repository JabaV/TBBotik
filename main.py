import vk_api
import asyncio
from time import sleep
from modules import module_logger, module_handler
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

data = open("data", 'r')
print('File opened')
contents = data.readlines()
data.close()
print("Closed")

secter = contents[0].strip('\n')
another = contents[1].strip('\n')

vk_session = vk_api.VkApi(token=str(secter))
reserve = vk_api.VkApi(token=str(another))

current = vk_session


async def listen(session):
    longpoll = VkBotLongPoll(session, 172386457)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user and event.object.message['peer_id'] == 372894745 or event.object.message['peer_id'] == 222366400:
                if event.object.message['text'] == 'stfu':
                    exit()
            if event.from_chat or event.from_user:
                chat_id = event.object.message['peer_id']
                msg = event.object.message['text']
                r_text = ""
                if 'reply_message' in event.object.message:
                    r_text = event.object.message['reply_message']['text']
                task_handle = asyncio.create_task(module_handler.handle_message(msg, chat_id, session, r_text))
                await task_handle
        elif (event.type == VkBotEventType.WALL_POST_NEW) & (event.obj['post_type'] == 'post'):
            post_id = event.obj['id']
            task_handle = asyncio.create_task(module_handler.handle_post(post_id, session))
            await task_handle


async def main():
    flag = True
    global current
    while flag:
        try:
            print('Started listening')
            task_listen = asyncio.create_task(listen(current))
            await task_listen
        except Exception as e:
            if str(e).__contains__("Connection aborted") or str(e).__contains__("Max retries"):
                if current == vk_session:
                    global reserve
                    current = reserve
                    module_logger.Log("Switched key to reserve")
                else:
                    global vk_session
                    current = vk_session
                    module_logger.Log("Switched key to main")
            else:
                module_logger.Log(e)
                sleep(10)


asyncio.run(main())
