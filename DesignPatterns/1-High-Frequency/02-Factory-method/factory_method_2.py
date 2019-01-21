#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import List

# クライアント側でいくつも DataObjectを生成する場合、その1では毎回 DbMode を指定する必要がある
# 毎回 DbMode を指定するなら同一のインスタンスを毎回指定しているにすぎない
# クライアント側では DbMode を意識せずに複数インスタンス化できるように変更する


class DbMode(Enum):
    STANDALONE: int = auto()
    NETWORKING: int = auto()


class DataObject(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @staticmethod
    def create() -> object:
        return FileDataObject()

    @abstractmethod
    def fetch_data_object(self, id_num: int) -> str:
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        self.data_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def fetch_data_object(self, id_num) -> str:
        return self.data_list[id_num]


class DbDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        pass

    def fetch_data_object(self, id_num: int) -> str:
        pass


class DataObjectFactory:
    # オブジェクト生成の責任を負う

    @staticmethod
    def create(data_type: DbMode):
        if data_type == DbMode.STANDALONE:
            return FileDataObject()
        if data_type == DbMode.NETWORKING:
            return DbDataObject()


class Client:

    def __init__(self) -> None:
        self.factory = DataObjectFactory()
        self.data_object = self.factory.create(DbMode.STANDALONE)  # ここで DbMode を指定する

    def operating(self, id_num: int) -> str:
        person = self.data_object.fetch_data_object(id_num)
        return person


if __name__ == '__main__':
    client: Client = Client()

    i: int = 0
    while True:
        try:
            print(client.operating(i), end="")
            i += 1
        except IndexError:
            break

    row: str = client.operating(2)
    print("\n")
    print(row)
