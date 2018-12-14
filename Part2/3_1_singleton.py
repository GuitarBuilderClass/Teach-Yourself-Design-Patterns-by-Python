#! /usr/bin/env python3


class CourtScheduler:
    """予約管理クラス"""
    HOURS: int = 24

    def __init__(self) -> None:
        self.__initialize()

    @classmethod
    def __initialize(cls) -> list:
        """
        予約台帳を初期化する
        Returns:
            list: HOURS分の空き枠がある予約台帳
        """
        cls.booking: list = list()
        for _ in range(cls.HOURS):
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
        self.hours: int = CourtScheduler.HOURS

    def make_reservation(self, hour: int, person: str) -> None:
        """
        予約が受付できるか確認する
        Args:
            hour (int): 予約者の予約希望時間
            person (): 予約希望者

        """
        if (hour <= 0) or (hour > self.hours - 1):
            message = "指定時間が間違っています"
        elif (self.END < hour) or (hour < self.START):
            message = "営業時間外です"
        else:
            if CourtScheduler.booking[hour] == " ":
                CourtScheduler.schedule(hour, person)
                message = f"{self.name}が{hour}時に{person}君の予約を入れました"
            else:
                person2 = CourtScheduler.booking[hour]
                message = f"{hour}時は既に{person2}君の予約が入っております\n"
                message += f"あぁっと{person}君ふっ飛ばされた!!"
        print(message)


class Main:
    """メイン処理クラス"""
    court_scheduler: object = CourtScheduler()
    receptionistA: object = Receptionist("A")
    receptionistB:object = Receptionist("B")

    receptionistA.make_reservation(9, "日向")
    receptionistA.make_reservation(12, "マーガス")
    receptionistA.make_reservation(18, "新田")
    receptionistB.make_reservation(10, "大空")
    receptionistB.make_reservation(11, "岬")
    receptionistB.make_reservation(12, "森崎")


    receptionistC: object = Receptionist("ゴールポスト")
    receptionistC.make_reservation(12, "森崎")


if __name__ == '__main__':
    Main()
