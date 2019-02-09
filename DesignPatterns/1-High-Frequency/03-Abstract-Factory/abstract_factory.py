#! /usr/bin/env python3
from enum import Enum, auto
from typing import Union


class GuitarType(Enum):
    Telecaster: int = auto()
    LesPaul: int = auto()


class Neck:

    def feature(self) -> str:
        pass


class Fingerboard:

    def feature(self) -> str:
        pass


class Body:

    def feature(self) -> str:
        pass


# Telecaster の材をクラス化する
class TelecasterNeck(Neck):

    def feature(self) -> str:
        return "Maple, C Shape"


class TelecasterFingerboard(Fingerboard):
    def feature(self) -> str:
        return "Maple, 7.25\" R"


class TelecasterBody(Body):
    def feature(self) -> str:
        return "Swamp Ash"


# Les Paul の材をクラス化する
class LesPaulNeck(Neck):

    def feature(self) -> str:
        return "Mahogany, Slim taper shape"


class LesPaulFingerboard(Fingerboard):
    def feature(self) -> str:
        return "Rosewood 12\" R"


class LesPaulBody(Body):
    def feature(self) -> str:
        return "Mahogany and Maple"


class GuitarFactory:

    def choice_neck(self) -> Union[TelecasterNeck, LesPaulNeck]:
        pass

    def choice_fingerboard(
            self) -> Union[TelecasterFingerboard, LesPaulFingerboard]:
        pass

    def choice_body(self) -> Union[TelecasterBody, LesPaulBody]:
        pass


class TelecasterFactory(GuitarFactory):

    def choice_neck(self) -> TelecasterNeck:
        return TelecasterNeck()

    def choice_fingerboard(self) -> TelecasterFingerboard:
        return TelecasterFingerboard()

    def choice_body(self) -> TelecasterBody:
        return TelecasterBody()


class LesPaulFactory(GuitarFactory):

    def choice_neck(self) -> LesPaulNeck:
        return LesPaulNeck()

    def choice_fingerboard(self) -> LesPaulFingerboard:
        return LesPaulFingerboard()

    def choice_body(self) -> LesPaulBody:
        return LesPaulBody()


class Order(GuitarFactory):

    def __init__(self, factory):
        factory: Union[TelecasterFactory, LesPaulFactory]

        if factory == GuitarType.Telecaster:
            factory = TelecasterFactory()
        elif factory == GuitarType.LesPaul:
            factory = LesPaulFactory()

        self.neck: Union[TelecasterNeck, LesPaulNeck]
        self.fingerboard: Union[TelecasterFingerboard, LesPaulFingerboard]
        self.body: Union[TelecasterBody, LesPaulBody]

        self.neck = factory.choice_neck()
        self.fingerboard = factory.choice_fingerboard()
        self.body = factory.choice_body()

    def make_guitar(self):
        return self.neck, self.fingerboard, self.body


if __name__ == '__main__':
    # ギターの種類を Order クラスの責任で指定
    guitar: GuitarType = GuitarType.Telecaster
    order: Order = Order(guitar)

    neck: str = order.neck.feature()
    fingerboard: str = order.fingerboard.feature()
    body: str = order.body.feature()
    print(f"{guitar.name}のネックは{neck}、" +
          f"フィンガーボードは{fingerboard}、" +
          f"ボディは{body}でできています。")
