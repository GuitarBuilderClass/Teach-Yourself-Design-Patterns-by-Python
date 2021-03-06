#! /usr/bin/env python3
from enum import Enum, auto
from typing import Union


class GuitarType(Enum):
    Telecaster: int = auto()
    LesPaul: int = auto()


# Telecaster の材をクラス化する
class TelecasterNeck:

    def feature(self) -> str:
        return "Maple, C Shape"


class TelecasterFingerboard:
    def feature(self) -> str:
        return "Maple, 7.25\" R"


class TelecasterBody:
    def feature(self) -> str:
        return "Swamp Ash"


# Les Paul の材をクラス化する
class LesPaulNeck:

    def feature(self) -> str:
        return "Mahogany, Slim taper shape"


class LesPaulFingerboard:
    def feature(self) -> str:
        return "Rosewood 12\" R"


class LesPaulBody:
    def feature(self) -> str:
        return "Mahogany and Maple"


class GuitarFactory:
    """Factory クラスから材を呼び出せるようにする"""

    # Telecaster の材を呼び出す
    def choice_telecaster_neck(self) -> TelecasterNeck:
        return TelecasterNeck()

    def choice_telecaster_fingerboard(self) -> TelecasterFingerboard:
        return TelecasterFingerboard()

    def choice_telecaster_body(self) -> TelecasterBody:
        return TelecasterBody()

    # Les Paul の材を呼び出す
    def choice_les_paul_neck(self) -> LesPaulNeck:
        return LesPaulNeck()

    def choice_les_paul_fingerboard(self) -> LesPaulFingerboard:
        return LesPaulFingerboard()

    def choice_les_paul_body(self) -> LesPaulBody:
        return LesPaulBody()


class Order:
    """Client 側のクラス"""

    def __init__(self, type: GuitarType) -> None:
        self.type: Enum = type

    def create_guitar(self) -> str:
        """
        オーダーに合わせて Fender か Gibson タイプを組み立てる
        Returns:
            str: 完成品の構成材

        """
        neck: Union[TelecasterNeck, LesPaulNeck]
        fingerboard: Union[TelecasterFingerboard, LesPaulFingerboard]
        body: Union[TelecasterBody, LesPaulBody]

        factory: GuitarFactory = GuitarFactory()

        if self.type == GuitarType.Telecaster:
            neck = factory.choice_telecaster_neck()
            fingerboard = factory.choice_telecaster_fingerboard()
            body = factory.choice_telecaster_body()

        if self.type == GuitarType.LesPaul:
            neck = factory.choice_les_paul_neck()
            fingerboard = factory.choice_les_paul_fingerboard()
            body = factory.choice_les_paul_body()

        # return で早めに返したいが、共通部分を括りたい気持ちも強い
        use_neck: str = neck.feature()
        use_fingerboard: str = fingerboard.feature()
        use_body: str = body.feature()

        return (f"{self.type.name} のネックは {use_neck}、" +
                f"フィンガーボードは {use_fingerboard}、" + f"ボディは {use_body} でできています。")


if __name__ == '__main__':
    order = Order(GuitarType.Telecaster)
    print(order.create_guitar())
