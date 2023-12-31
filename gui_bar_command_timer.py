import PySimpleGUI as sg
from enum import Enum

from command_timer import CommandTimer, CommandTimerArugument
import time

class GUIParts(Enum):
    BAR_Progress    = "ProgressBar"
    BT_Exit         = "button_exit"

class Colors(Enum):
    NONE   = '#DDDDDD'
    WHITE  = '#ffffff'
    SILVER = '#DDDDDD'
    GRAY   = '#AAAAAA'
    BLACK  = '#111111'
    RED    = '#FF4131'
    MAROON = '#85144B'
    YELLOW = '#FFDC00'
    OLIVE  = '#3D9979'
    LIME   = '#01FF70'
    GREEN  = '#2ECC40'
    AQUA   = '#7FDBFF'
    TEAL   = '#39CCCC'
    BLUE   = '#0074D9'
    NAVY   = '#001F3F'
    FUCHSIA= '#F012BE'
    PURPLE = '#B10DC9'


class GUIBarCommandTimer(CommandTimer):
    def __init__(self, p: CommandTimerArugument) -> None:
        super().__init__(p)
        self.pre_time = 0

    def run(self):
        layout_main = [ [
                sg.Button("Exit",   key=GUIParts.BT_Exit),
                sg.ProgressBar(100, key=GUIParts.BAR_Progress, orientation='h', size=(1200, 50)),
            ],]
        self.window = sg.Window("Bar Timer", layout_main, 
            size=(1200,50), grab_anywhere=True, resizable=True, no_titlebar=True,
        )
        try:
            r = self.__maintimer()
            while self.is_repreat:
                r = self.__maintimer()
            while True:
                if not r:
                    break
                event,value = self.window.read(timeout=50)
                if event in (None, sg.WIN_CLOSED):
                    break
                elif event == GUIParts.BT_Exit:
                    self.is_repreat = False
                    break
        except KeyboardInterrupt:
            print("Intrrupt Timer")
        finally:
            self.window.close()

    def __maintimer(self):
        event,value = self.window.read(timeout=50)
        self.window[GUIParts.BAR_Progress].update(0, max=self.target_sec, bar_color=("GREEN", "WHITE"))
        self.timecount.pause()
        self.pre_time = 0
        self.timecount.reset()
        self.timecount.start()
        while True:
            event,value = self.window.read(timeout=50)
            if event in (None, sg.WIN_CLOSED):
                return False
            elif event == GUIParts.BT_Exit:
                self.is_repreat = False
                return False

            elif event == sg.TIMEOUT_KEY:
                if self.__update():
                    self.timecount.pause()
                    if not self.is_silent:
                        self.end_timer_sound()
                    return True
    
    def __update(self):
        etime = self.timecount.update()
        # print(time)
        diff = etime-self.pre_time
        # bar_color_80per = ("GREEN", "WHITE")
        # bar_color_20per = ("YELLOW", "WHITE")
        # bar_color_10per = ("RED", "WHITE")
        bar_color_80per = (Colors.OLIVE.value, Colors.SILVER.value)
        bar_color_20per = (Colors.YELLOW.value, Colors.SILVER.value)
        bar_color_10per = (Colors.RED.value, Colors.SILVER.value)
        # if diff >= 1 or etime >= self.target_sec:
        percent = etime / self.target_sec
        if percent < 0.8:
            bar_color = bar_color_80per
        elif percent <= 0.9:
            bar_color = bar_color_20per
        elif percent > 0.9:
            bar_color = bar_color_10per
        self.window[GUIParts.BAR_Progress].update(etime, max=self.target_sec, bar_color=bar_color)
        self.pre_time = etime
        if etime >= self.target_sec:
            return True
        return False

