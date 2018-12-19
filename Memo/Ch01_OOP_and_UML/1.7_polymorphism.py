#! /usr/bin/env python3

from abc import ABCMeta, abstractmethod


class RentalItem(metaclass=ABCMeta):

    def __init__(self, title: str, minutes: int) -> None:
        self._title = title
        self._minutes = minutes
        self.fee: int = 0

    @abstractmethod
    def calc_fee(self, days: int) -> int:
        pass

    @property
    def title(self) -> str:
        return f"タイトルは「{self._title}」"


class Video(RentalItem):

    def calc_fee(self, days: int) -> None:
        self.fee = 120 * days


class DVD(RentalItem):

    def calc_fee(self, days: int) -> None:
        self.fee = 240 * days


class CD(RentalItem):

    def calc_fee(self, days: int) -> int:
        pass


class JapaneseCD(CD):

    def calc_fee(self, days: int) -> None:
        if days >= 7:
            self.fee = 200 * days
        else:
            self.fee = 320 * days


class ImportCD(CD):

    def calc_fee(self, days: int) -> None:
        if days >= 3:
            self.fee = 220 * days
        else:
            self.fee = 350 * days


rental1 = JapaneseCD("Japanese-pop-music", 4)
rental1.calc_fee(3)


print(rental1.title)
print(rental1.fee)
