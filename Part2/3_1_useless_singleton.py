#! /usr/bin/env python3

HOURS: int = 24


class CourtScheduler:
    """予約管理クラス"""

    def __init__(self) -> None:
        self.__initialize()

    def __initialize(self) -> list:
        """
        予約台帳を初期化する
        Returns:
            list: HOURS分の空き枠がある予約台帳
        """
        self.booking: list = list()
        for _ in range(HOURS):
            self.booking += " "
        return self.booking

    def schedule(self, hour: int, person: str) -> None:
        """
        予約者が指定する時間に予約を入れる
        Args:
            hour (int): 予約希望時間
            person (str): 予約希望者
        """
        self.booking[hour]: object = person


class Receptionist:
    """予約受付クラス"""

    # 営業開始時間〜終了時間
    START: int = 9
    END: int = 20

    def __init__(self, name: str, scheduler: CourtScheduler) -> None:
        """
        予約受付係の設定をする
        Args:
            name (str): 予約受付係の名前
        """
        self.name: str = name
        self.court_scheduler: CourtScheduler = scheduler
        self.hours: int = HOURS

    def make_reservation(self, hour: int, person: str) -> None:
        """
        予約が受付できるか確認する
        Args:
            hour (int): 予約者の予約希望時間
            person (str): 予約希望者
        """
        if (hour <= 0) or (hour > self.hours - 1):
            message = "指定時間が間違っています"
        elif (self.END < hour) or (hour < self.START):
            message = "営業時間外です"
        else:
            if self.court_scheduler.booking[hour] == " ":
                self.court_scheduler.schedule(hour, person)
                message = f"{self.name}が{hour}時に{person}くんの予約を入れました"
            else:
                person2 = self.court_scheduler.booking[hour]
                message = f"{hour}時は既に{person2}くんの予約が入っております\n"
                message += f"あぁっと{person}くんふっ飛ばされた!!"
        print(message)


class Main:
    """メイン処理クラス"""
    court_scheduler: CourtScheduler = CourtScheduler()
    receptionistA: Receptionist = Receptionist("A", court_scheduler)
    receptionistB: Receptionist = Receptionist("B", court_scheduler)

    receptionistA.make_reservation(9, "日向")
    receptionistA.make_reservation(12, "マーガス")
    receptionistA.make_reservation(18, "新田")
    receptionistB.make_reservation(10, "大空")
    receptionistB.make_reservation(11, "岬")
    receptionistB.make_reservation(12, "森崎")

    print()
    goal_post: CourtScheduler = CourtScheduler()
    receptionistC = Receptionist("ゴールポスト", goal_post)
    receptionistC.make_reservation(12, "森崎")


if __name__ == '__main__':
    Main()
