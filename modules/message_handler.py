from modules import module_commands


def handle_message(text, chat_id, vk_session, replied_text=""):
    if text[:2].lower() in module_commands.commands:
        module_commands.commands[text[:2]](text, chat_id, vk_session, replied_text)

