from tools.clock import mono as clock, difference, convert, operate


class Stopwatch:

    def __init__(self):
        self.running = False
        self.paused = False

        # Protected attributes to store and reset session / game values
        self.__started = None
        self.__paused = None
        self.__resumed = None
        self.__skip = 0
        self.__stopped = None

    def start(self):
        self.running = True
        self.__started = clock.now(formatted=False)

    def pause(self):
        self.paused = True
        self.__paused = clock.now(formatted=False)

    def unpause(self):
        self.paused = False
        self.__resumed = clock.now(formatted=False)
        seconds_paused = difference.dt(dt_start=self.__paused,
                                       dt_end=self.__resumed)
        self.__skip += seconds_paused
        self.__paused = None
        self.__resumed = None

    def stop(self):
        self.__stopped = clock.now(formatted=False)
        self.running = False

    def reset(self):
        if self.running:
            self.stop()
        self.__started = None
        self.__paused = None
        self.__resumed = None
        self.__skip = 0
        self.__stopped = None

    def elapsed(self):
        if self.__started is not None:
            start_time = self.__started
            pause_time = self.__paused
            end_time = self.__stopped
            if self.running:
                end_time = clock.now(formatted=False)
            if not self.paused:
                unskipped_time = difference.dt(dt_start=start_time, dt_end=end_time)
                final_time = unskipped_time - self.__skip
                final_time_formatted = convert.seconds_to_list(final_time)
            else:
                final_time = difference.dt(dt_start=start_time, dt_end=pause_time)
                final_time_formatted = convert.seconds_to_list(final_time)
            return final_time_formatted
