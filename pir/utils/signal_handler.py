import signal


class SignalHandler:
    term = False
    num = 0

    @classmethod
    def terminate_handler(cls, num, stack):
        cls.term = True
        cls.num = num


signal.signal(signal.SIGINT, SignalHandler.terminate_handler)
signal.signal(signal.SIGHUP, SignalHandler.terminate_handler)
signal.signal(signal.SIGTERM, SignalHandler.terminate_handler)
