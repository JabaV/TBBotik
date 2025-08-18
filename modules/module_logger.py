import datetime

log = open("error_log.txt", "a+", encoding='utf-8')


def Log(error):
    print("[" + str(datetime.datetime.now().date()) + "] " + str(error))
    log.write("[" + str(datetime.datetime.now().date()) + "] " + str(error) + "\n")
    log.flush()
