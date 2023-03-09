import time

log = open("error_log.txt", "a+", encoding='utf-8')


def Log(error):
    log.write("[" + str(time.time()) + "]" + str(error))
