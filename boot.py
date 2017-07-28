import sys
import time
import config
import logging
import scanner
from concurrent.futures import ThreadPoolExecutor


def create_logger():
    root = logging.getLogger()
    root.setLevel(config.LOG_LEVEL)

    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
    return root


def on_scan_complete(f):
    print 'done ' + str(f.result(0))

if __name__ == '__main__':
    logger = create_logger()
    pool = ThreadPoolExecutor(config.THREAD_POOL_SIZE)
    while True:
        f = pool.submit(scanner.scan, logger)
        f.add_done_callback(on_scan_complete)
        time.sleep(1)


