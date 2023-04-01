from modules import module_commands


def handle_message(text, chat_id, vk_session, replied_text=""):
    if text[:3].lower() in module_commands.commands:
        print(text[:3].lower())
        module_commands.commands[text[:3].lower()](text, chat_id, vk_session, replied_text)

