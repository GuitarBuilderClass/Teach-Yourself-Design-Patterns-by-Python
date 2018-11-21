#usr/bin/env/ python3


# レンタルビデオ店からビデオを借りるクラス(class Video)
class Video(object):

    def __init__(self, title: str, recorded_minute: int):
        """
        ビデオの情報をデータ化する
        :param title: ビデオタイトル
        :param recorded_minute: 収録話数
        """
        self._title = title
        self._recorded_minute = recorded_minute

    def video(self, title: str):
        """
        ビデオタイトルをセットする
        :param title: ビデオタイトル
        :return: None
        """
        self.title = title

    def calc(self, days: int) -> int:
        """
        料金計算
        :param days: 貸出日数
        :return: ビデオの貸出料金
        """
        return 50 * days