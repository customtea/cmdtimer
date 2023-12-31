from command_timer import CommandTimer, CommandTimerArugument
from tqdm import tqdm, TqdmWarning
import warnings
import time

warnings.filterwarnings("ignore", category=TqdmWarning)


def get_h_m_s(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return h, m, s

class TerminalBarCommandTimer(CommandTimer):
    def __init__(self, p :CommandTimerArugument) -> None:
        super().__init__(p)
        self.pre_time = 0
        self.progress_bar = tqdm(total=self.target_sec)
        self.progress_bar.set_description("Remain Time")
        self.progress_bar.bar_format = "{l_bar}{bar} |[{elapsed}<{remaining}]"

    
    def __update(self):
        time = self.timecount.update()
        # print(time)
        diff = time-self.pre_time
        # if diff >= 1:
        self.progress_bar.update(diff)
        self.pre_time = time
        if time >= self.target_sec:
            return True
        return False
    
    def __maintimer(self):
        self.timecount.pause()
        self.timecount.reset()
        self.pre_time = 0
        self.timecount.start()
        self.progress_bar.reset()
        while True:
            if self.__update():
                self.timecount.pause()
                if not self.is_silent:
                    self.end_timer_sound()
                break
            time.sleep(0.2)
    
    def run(self):
        try:
            self.__maintimer()
            while self.is_repreat:
                self.__maintimer()
        except KeyboardInterrupt:
            print("Intrrupt Timer")
            return
        finally:
            self.progress_bar.close()
    
    def end_timer_sound(self):
        self.chime.chime(self.sound_count)
