from vk_api.utils import get_random_id


def send(text, chat_id, vk_session):
    vk_session.method('messages.send', {
        'peer_id': chat_id,
        'message': text,
        'random_id': get_random_id()
    })


def repost(post_id, chat_id, vk_session):
    vk_session.method('messages.send', {
        'peer_id': chat_id,
        'attachment': 'wall-172386457_' + post_id,
        'message': 'Новый пост в группе:',
        'random_id': get_random_id()
    })


def kva(c, chid, vk_session):
    if c != 1:
        txt = 'Ква'
        attch = ''
    else:
        txt = 'Джекпот'
        attch = 'audio474499147_456517029'
    vk_session.method(
        'messages.send', {
            'peer_id': chid,
            'message': txt,
            'random_id': get_random_id(),
            'attachment': attch
        })

