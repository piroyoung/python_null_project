import time
from pir.utils.signal_handler import *
from pir.utils.logger import *

if __name__ == '__main__':
    while True:
        LOGGER.info(SignalHandler.term)
        time.sleep(1)
        if SignalHandler.term is True:
            LOGGER.info('Process has been terminated. signal id: {0}'.format(SignalHandler.num))
            break
