#! /usr/bin/env python3


class CourtScheduler:

    HOURS: int = 24

    def __init__(self) -> None:
        self.__initialize()

    @classmethod
    def __initialize(cls) -> list:
        cls.__schedule: list = list()
        for _ in range(cls.HOURS):
            cls.__schedule += " "
        return cls.__schedule

    @classmethod
    def schedule(cls) -> list:
        return cls.__schedule

    @classmethod
    def schedule(cls, hour: int, person: str) -> None:
        cls.__schedule[hour] = person


class Receptionist:
    START: int = 9
    END: int = 20

    def __init__(self, name: str) -> None:
        self.name: int = name
        self.court_scheduler = CourtScheduler
        self.hours = self.court_scheduler.HOURS

    def make_reservation(self, hour: int, person: str) -> None:
        if (hour < 0) or (hour > self.hours-1):
            message = "指定時間が間違っています"
        elif (self.END < hour) or (hour < self.START):
            message = "営業時間外です"
        else:
            for _ in self.court_scheduler.schedule:
                print(_, end=", ")
            if self.court_scheduler.schedule[hour-1] == " ":
                self.court_scheduler.schedule(hour, person)
                message = f"{self.name}が{hour}時に{person}さんの予約を入れました"
            else:
                message = f"{hour}時は既に予約が入っております\nあぁっと{person}君ふっ飛ばされた!!"
        print(message)


class Main:
    """メイン処理クラス"""
    court_scheduler: CourtScheduler = CourtScheduler()
    receptionistA = Receptionist("A")
    receptionistB = Receptionist("B")

    receptionistA.make_reservation(9, "日向")
    receptionistA.make_reservation(12, "マーガス")
    receptionistA.make_reservation(18, "新田")
    receptionistB.make_reservation(10, "大空")
    receptionistB.make_reservation(11, "岬")
    receptionistB.make_reservation(12, "森崎")


if __name__ == '__main__':
    Main()
