#! /usr/bin/env python3

HOURS: int = 24


class CourtScheduler:
    """予約管理クラス"""
    _has_instance = None

    def __new__(cls):
        if not cls._has_instance:
            cls._has_instance = super(
                CourtScheduler, cls).__new__(cls)
            cls.__initialize()
        return cls._has_instance

    def __init__(self):
        if __name__ == '__main__':
            self.booking: list = self.__new__()

    @classmethod
    def __initialize(cls) -> list:
        """
        予約台帳の初期化をする
        Returns:
           1ページも埋まっていない本
        """
        cls.booking = list()
        for __ in range(HOURS):
            cls.booking += " "
        return cls.booking

    @classmethod
    def schedule(cls, hour: int, person: str) -> None:
        """
        予約者が指定する時間に予約を入れる
        Args:
            hour (int): 予約希望時間
            person (str): 予約希望者
        """
        cls.booking[hour] = person


class Receptionist:
    """予約受付クラス"""

    # 営業開始時間〜終了時間
    START: int = 9
    END: int = 20

    def __init__(self, name: str) -> None:
        """
        予約受付係の設定をする
        Args:
            name (str): 予約受付係の名前
        """
        self.name: str = name

    def make_reservation(self, hour: int, person: str) -> None:
        """
        予約が受付できるか確認する
        Args:
            hour (int): 予約者の予約希望時間
            person (str): 予約希望者
        """
        court_scheduler = CourtScheduler()
        if (hour <= 0) or (hour > HOURS - 1):
            message = "指定時間が間違っています"
        elif (self.END < hour) or (hour < self.START):
            message = "営業時間外です"
        else:
            if court_scheduler.booking[hour] == " ":
                court_scheduler.schedule(hour, person)
                message = f"{self.name}が{hour}時に{person}くんの予約を入れました"
            else:
                person2 = court_scheduler.booking[hour]
                message = f"{hour}時は既に{person2}くんの予約が入っております\n"
                message += f"あぁっと{person}くんふっ飛ばされた!!"
        print(message)


class Main:
    """メイン処理クラス"""
    receptionistA: Receptionist = Receptionist("A")
    receptionistB: Receptionist = Receptionist("B")

    receptionistA.make_reservation(9, "日向")
    receptionistA.make_reservation(12, "マーガス")
    receptionistA.make_reservation(18, "新田")
    receptionistB.make_reservation(10, "大空")
    receptionistB.make_reservation(11, "岬")
    receptionistB.make_reservation(12, "森崎")

    print()
    receptionistC: Receptionist = Receptionist("ゴールポスト")
    receptionistC.make_reservation(12, "森崎")


if __name__ == '__main__':
    Main()
