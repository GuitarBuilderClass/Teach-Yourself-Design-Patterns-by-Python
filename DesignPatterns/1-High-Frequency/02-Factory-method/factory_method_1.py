#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from typing import List


class DataObject(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @staticmethod
    def create():
        # Client側は DataObject がどのオブジェクトを呼んでいるか意識する必要がなくなる
        # Client内で複数 DataObject を呼び出している場合はその全てを修正する必要があるが
        # このコードでは create の戻り値を変更するだけで全体の修正が可能になる
        return FileDataObject()

    @abstractmethod
    def fetch_user(self, id_num: int) -> str:
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        super().__init__()
        self.user_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.user_list.append(line)

    def fetch_user(self, id_num: int) -> str:
        return self.user_list[id_num]


class DBDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        super().__init__()

    def fetch_user(self, id_num: int) -> str:
        pass


class Client:
    def __init__(self) -> None:
        self.data_object: DataObject = DataObject.create()


if __name__ == '__main__':

    client: DataObject = Client().data_object

    i = 0
    while True:
        try:
            print(client.fetch_user(i), end="")
            i += 1
        except IndexError:
            break

    user: str = client.fetch_user(1)
    print("\n")
    print(user)
