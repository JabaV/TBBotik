from modules import module_commands


def handle_message(text, chat_id, vk_session, replied_text=""):
    parsed = str(text).split(' ')
    if parsed[0].lower() in module_commands.commands:
        module_commands.commands[parsed[0].lower()](text, chat_id, vk_session, replied_text)
    elif text[:3].lower() == 'ква':
        module_commands.commands[text[:3].lower()](text, chat_id, vk_session, replied_text)

