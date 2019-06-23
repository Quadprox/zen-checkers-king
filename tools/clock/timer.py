from tools.clock import mono as clock, difference, convert
from tools import console


class Timer:

    ID = 0

    @classmethod
    def update_timer_id(cls):
        cls.ID += 1

    def __init__(self):
        self.running = False
        self.update_timer_id()

        # Protected attributes to store and reset session / game values
        self.__started = None
        self.__paused = None
        self.__resumed = None
        self.__skip = 0
        self.__set = None

    @property
    def ring(self):
        time_up = False
        if self.running:
            rem_seconds = convert.list_to_seconds(self.remaining)
            if rem_seconds <= 0:
                time_up = True
        return time_up

    def set(self, seconds: int):
        self.__set = seconds

    def start(self):
        if self.__set is not None:
            self.running = True
            self.__started = clock.now(formatted=False)
        else:
            console.error(
                message='Unable to start Timer: Timer object {object} is already running!'.format(
                    object=self))

    def pause(self):
        self.__paused = clock.now(formatted=False)

    def unpause(self):
        self.__resumed = clock.now(formatted=False)
        seconds_paused = difference.dt(dt_start=self.__paused, dt_end=self.__resumed)
        self.__skip += seconds_paused
        self.__paused = None
        self.__resumed = None

    def stop(self):
        if self.running:
            self.running = False
            self.__started = None
            self.__paused = None
            self.__resumed = None
            self.__skip = 0
            self.__set = None
        else:
            console.error(
                message='Unable to stop Timer: Timer object {object} is not running!'.format(
                    object=self))

    @property
    def elapsed(self):
        if self.running:
            start_time = self.__started
            end_time = clock.now(formatted=False)
            unskipped_time = difference.dt(dt_start=start_time, dt_end=end_time)
            final_time = unskipped_time - self.__skip
            final_time_formatted = convert.seconds_to_list(final_time)
            return final_time_formatted
        else:
            console.error(
                message='Unable to retrieve Timer elapsed time: Timer object {object} is not running!'.format(
                    object=self))

    @property
    def remaining(self):
        start_seconds = convert.dt_to_seconds(self.__started)
        end_seconds = start_seconds + self.__set + self.__skip
        now_seconds = convert.dt_to_seconds(clock.now(formatted=False))
        diff_seconds = end_seconds - now_seconds
        diff_formatted = convert.seconds_to_list(diff_seconds)
        return diff_formatted
