from timecount import TimeCounter
from sound_ctrl import ChimeRing
import time
import datetime
from enum import Enum

class TimerMode(Enum):
    TIMER = 0
    GAME = 1000 # 放置ゲーの生産量と目標値を入れると自動的にタイマーを設定する
    ALARM = 2000 # 時刻を指定するモード
    CRON = 3000 # CRON記述で実行

class CommandTimerArugument():
    def __init__(self) -> None:
        # Always Option
        self.ring = None
        self.silent = None
        self.sound = ""
        self.repeat = False
        self.scount = 3
        
        # timer mode
        self.mode = TimerMode.TIMER
        self.sec = 0
        self.min = 0
        self.hour = 0
    
        # game mode
        self.prod = 1
        self.mass = 10
    
    def fromargparse(self, parser):
        for key, val in parser.__dict__.items():
            self.__dict__[key] = val
            if key == "mode":
                self.mode = TimerMode[val.upper()]

        if self.silent is None:
            self.silent = True
        if self.ring is True:
            self.silent = False
        
        if self.mode == TimerMode.GAME:
            self.calc_prod_mass()
    
    def calc_prod_mass(self):
        self.sec = self.mass / self.prod



def get_h_m_s(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return h, m, s

class CommandTimer():
    def __init__(self, p :CommandTimerArugument) -> None:
        self.p = p
        self.timecount = TimeCounter()
        self.is_silent = p.silent
        self.sound_file = p.sound
        self.sound_count = p.scount
        if not self.sound_file is None:
            self.chime = ChimeRing(self.sound_file)
        else:
            self.chime = ChimeRing()
        self.target_sec = p.sec + p.min * 60 + p.hour * 3600
        self.hour, self.min, self.sec = get_h_m_s(self.target_sec)
        self.__start_datetime = datetime.datetime.now()
        self.is_repreat = p.repeat
    
    def __update(self):
        time = self.timecount.update()
        # print(time)
        if time >= self.target_sec:
            return True
        return False
    
    def __maintimer(self):
        self.timecount.reset()
        self.timecount.start()
        while True:
            if self.__update():
                self.timecount.pause()
                self.end_timer_silent()
                if not self.is_silent:
                    self.end_timer_sound()
                break
            time.sleep(0.2)
    
    def run(self):
        self.__maintimer()
        while self.is_repreat:
            self.__maintimer()
    
    def end_timer_silent(self):
        print(f"Time is End. Elapsed {self.hour:}:{self.min:02}:{self.sec:02} At:{self.__start_datetime.isoformat()}")
    
    def end_timer_sound(self):
        self.chime.chime(self.sound_count)
