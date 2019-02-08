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


class GuitarFactory(Neck, Fingerboard, Body):

    neck: Union[TelecasterNeck, LesPaulNeck]
    fingerboard: Union[TelecasterFingerboard, LesPaulFingerboard]
    body: Union[TelecasterBody, LesPaulBody]

    neck = Neck.feature()
    fingerbord = Fingerboard.feature()
    body = Body.feature()

    def create_neck(self) -> str:





