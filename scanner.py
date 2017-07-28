import time

x = 0


def scan(logger):
    logger.debug('start')
    time.sleep(3)
    logger.debug('finish')
    global x
    x += 1
    return x
