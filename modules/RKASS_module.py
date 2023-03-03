from vk_api.keyboard import *
from vk_api.utils import get_random_id

kbd = VkKeyboard(one_time=True)
kbd.add_button('Эймил Джемилов', color=VkKeyboardColor.PRIMARY)
kbd.add_button('Эймил Джемилов2', color=VkKeyboardColor.POSITIVE)


def menu(sender, vk_session):
    vk_session.method('messages.send', {
        'peer_id': sender,
        'random_id': get_random_id(),
        'keyboard': kbd.get_keyboard()
    })
