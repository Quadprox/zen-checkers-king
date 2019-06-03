import time
from tools import clock


class Stopwatch:

    def __init__(self):
        self.running = False

        # Protected attributes to store and reset session / game values
        self.__started_at = 0           # time.time() value starting point
        self.__paused_at = 0            # time.time() value paused point
        self.__resumed_at = 0           # time.time() value resumed point
        self.__paused_seconds = 0       # time difference in seconds
        self.__stopped_at = 0           # time.time() value fullstop point

    def __str__(self):
        pass

    def __difference(self):
        if self.running:
            difference = clock.now() - self.__started_at - self.__paused_seconds
        else:
            difference = self.__stopped_at - self.__started_at - self.__paused_seconds
        return difference

    def start(self):
        self.running = True
        self.__started_at = time.time()

    def stop(self):
        self.running = False
        self.__stopped_at = time.time()

    def pause(self):
        self.__paused_at = time.time()

    def resume(self):
        self.__resumed_at = time.time()
        difference = self.__resumed_at - self.__paused_at
        self.__paused_seconds += difference

    def reset(self):
        self.running = False
        self.__started_at = 0
        self.__paused_at = 0
        self.__resumed_at = 0
        self.__paused_seconds = 0
        self.__stopped_at = 0

    def elapsed(self):
        difference = round(self.__difference(), 0)
        time_elapsed = clock.convert(value=difference)
        return time_elapsed
