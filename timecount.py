import time

class TimeCounter:
    """
    経過時間をカウントするクラス
    
    Attributes
    ----------
    __pre_time : float
        エポック時間を浮動小数点にしたもの（time.time()の実行結果そのもの）
    is_pause : bool
        一時停止状態にあるかどうかのフラグ．
        一時停止中はカウンタが停止
        復帰時に時刻をpre_timeに保存して復帰する．以降の時刻は復帰点を基に計算される
    __elapsed_second : float
        時間差分を足し込んで，経過時間としている．
        エポック時間を浮動小数点化したものなので，浮動小数点まで含まれる
    """
    def __init__(self) -> None:
        self.__pre_time: float = time.time()
        self.is_pause: bool = False
        self.__elapsed_second: float = 0
    
    def update(self) -> float:
        """
        経過時間の更新と取得
    
        Returns
        -------
        elapsed_second : float
            経過秒数
        """
        curtime = time.time()
        if not self.is_pause:
            self.__elapsed_second += curtime - self.__pre_time
        self.__pre_time = curtime
        return self.__elapsed_second
    
    def reset(self) -> None:
        """
        計測のリセット
        """
        if self.is_pause:
            self.is_pause = True
            self.__elapsed_second = 0
    
    def pause(self) -> None:
        """
        計測の一時停止
        """
        self.is_pause = True
    
    def resume(self) -> None:
        """
        計測の復帰
        """
        self.is_pause = False
        self.__pre_time = time.time()
    
    def start(self) -> None:
        """resumeのエイリアス
        """
        self.resume()
    
    def isPause(self) -> bool:
        """
        一時停止状態を返すゲッター（変数がPublicなので微妙）
        """
        return self.is_pause