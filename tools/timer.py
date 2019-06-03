from tools import clock
import time


class Timer:

    def __init__(self):
        self.running = False

        # Protected attributes to store and reset session / game values
        self.__started_at = 0           # time.time() value starting point
        self.__paused_at = 0            # time.time() value paused point
        self.__resumed_at = 0           # time.time() value resumed point
        self.__paused_seconds = 0       # time difference in seconds
        self.__ring_at = 0              # time.time() value fullstop point

    def __str__(self):
        pass

    def __difference_elapsed(self):
        difference = 0
        if self.running:
            difference = clock.now() - self.__started_at - self.__paused_seconds
        return difference

    def __difference_remaining(self):
        difference = 0
        if self.running:
            difference = (self.__ring_at + self.__paused_seconds) - clock.now()
        return difference

    @property
    def time_is_up(self):
        status = False
        if self.__difference_remaining() <= 0:
            status = True
        return status

    @property
    def time_set(self):
        seconds = 0
        if self.__ring_at != 0:
            seconds = int(self.__ring_at - self.__started_at)
        return seconds

    def start(self):
        if self.__ring_at != 0:
            self.running = True
            self.__started_at = time.time()

    def stop(self):
        self.running = False
        self.reset()

    def pause(self):
        if self.running:
            self.__paused_at = time.time()
        else:
            print()

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
        self.__ring_at = 0

    def time_elapsed(self):
        difference = round(self.__difference_elapsed(), 0)
        time_elapsed = clock.convert(value=difference)
        return time_elapsed

    def time_remaining(self):
        difference = round(self.__difference_remaining(), 0)
        time_remaining = clock.convert(value=difference)
        return time_remaining

    def set(self, seconds):
        self.__ring_at = clock.now() + seconds
        self.running = True
