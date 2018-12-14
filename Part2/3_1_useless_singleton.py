#! /usr/bin/env python3

HOURS: int = 24
BOOKING: list = []
for i in range(HOURS):
    BOOKING += " "


# パターン未適用の場合
class Scheduler:
    """予約管理クラス"""

    def __init__(self):
        self.hours = HOURS

    @staticmethod
    def schedule():
        return BOOKING

    @staticmethod
    def schedule(hour: int, person: str):
        BOOKING[hour - 1] = person


class Receptionist(Scheduler):
    """予約受付クラス"""

    # 予約開始-終了時間
    START: int = 9
    END: int = 20

    def __init__(self, name: str):
        super(Receptionist, self).__init__()
        self.name: str = name
        self.scheduler = Scheduler()

    def make_reservation(self, hour: int, person: str):
        if (hour < 0) or (hour > self.scheduler.hours-1):
            message = "指定時間が間違っています"
        elif (self.END < hour) or (hour < self.START):
            message = "営業時間外です"
        else:
            if BOOKING[hour-1] == " ":
                self.scheduler.schedule(hour, person)
                message = f"{self.name}が{hour}時に{person}さんの予約を入れました"
            else:
                message = f"{hour}時は既に予約が入っております\nあぁっと{person}君ふっ飛ばされた!!"
        print(message)


class Main:
    """メイン処理クラス"""
    scheduler = Scheduler()
    receptionistA = Receptionist("A")
    receptionistB = Receptionist("B")

    receptionistA.make_reservation(9, "日向")
    receptionistA.make_reservation(12, "マーガス")
    receptionistA.make_reservation(18, "新田")
    receptionistB.make_reservation(10, "大空")
    receptionistB.make_reservation(11, "岬")
    receptionistB.make_reservation(12, "森崎")


if __name__ == "__main__":
    Main()
